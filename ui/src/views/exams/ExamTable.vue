<template>
	<div>
		<h4 class='text-2xl mb-2'>Exams</h4>

		<form class='formSingle mb-3 border-gray-400 border inline-block pl-2 py-2
			rounded' @submit.prevent='addExam'>
			<label for='examName'>New Exam</label>
			<input id='examName' name='examName' required type='text'
				placeholder='e.g.: Midterm 1' v-model='newExamName' />
			<button class='btnPrimary'>
				<LabelledIcon label='Add'>
					<AddIcon title='Add a new exam' />
				</LabelledIcon>
			</button>
		</form>

		<div class='border-gray-400 border-t mb-3'>
			<!-- exam card -->
			<div v-for='exam in exams.models' :key='exam.name'
				class='py-2 border-b border-gray-400 flex'>
				<!-- exam info -->
				<router-link to='/courses/1/exams/1' class='flex-auto mr-3 hover:bg-yellow-200'>
					<h4 class='text-xl font-medium break-all pl-2'>
						{{ exam.name }}
					</h4>
				</router-link>
				<!-- exam controls -->
				<div class='flex-initial self-center flex'>
					<router-link class='btnRegular mr-2' :to="{name: 'editExam',
						params:{ courseId: $route.params.courseId, examId: exam.id }}">
						<LabelledIcon label='Configure'>
							<ConfigureIcon title='Configure exam' />
						</LabelledIcon>
					</router-link>
					<button class='btnRegular' v-on:click='deleteExam(exam)'>
						<LabelledIcon label='Delete'><DeleteIcon /></LabelledIcon>
					</button>
				</div>
			</div>
		</div>

	</div>
</template>

<script>
import AddIcon from 'icons/Plus'
import ConfigureIcon from 'icons/Tune'
import DeleteIcon from 'icons/Delete'

import LabelledIcon from '@/components/util/LabelledIcon'

import {Exam, ExamList} from '@/models/Exam'

export default {
	name: 'CourseHome',
	components: {
		AddIcon,
		ConfigureIcon,
		DeleteIcon,
		LabelledIcon
	},
	data() { return {
		exams: new ExamList(),
		newExamName: ''
	}},
	methods: {
		getExams() {
			this.exams.set('course_id', this.$route.params.courseId)
			this.exams.fetch().then().catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: "Failed to get exams."})
			})
		},
		addExam() {
			let exam = new Exam()
			exam.name = this.newExamName
			exam.course_id = this.$route.params.courseId;
			exam.save().then( () => {
				this.$notify({title: "New exam '" + this.newExamName + "' was added.",
					type: 'success'})
				this.newExamName = ""
				this.exams.add(exam)
			}).catch( (error) => {
				this.$store.commit('error/add', {error: error,
					message: 'Failed to add exam "'+ this.newExamName +'".'})
			})
		},
		deleteExam(exam) {
			let examName = exam.name
			exam.delete().then( () => {
				this.$notify({title: "Exam '" + examName + "' was deleted.",
					type: 'success'})
			}).catch( (error) => {
				this.$store.commit('error/add', {error: error,
					message: 'Failed to delete exam "'+ examName +'".'})
			})
		}
	},
	mounted() {
		this.getExams()
	}
}
</script>

<style scoped>
</style>
