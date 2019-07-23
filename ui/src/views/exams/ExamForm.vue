<!-- Form for entering course information -->
<template>
	<div>
		<h3 class='text-2xl mb-2'>Configure Exam</h3>

		<form class='formVertical mb-3' @submit.prevent='saveExam'>
			<!-- Required Fields -->
			<label for='name'>Name</label>
			<input id='name' name='name' required type='text' v-model='exam.name'  />

			<label for='printId'>Print ID</label>
			<input id='printId' name='printId' type='text' v-model='exam.print_id'
				placeholder='100midterm1' />
			<span class='hint'>Human friendly ID printed on every page.</span>
			<!-- <button type='submit' class='btnRegular my-3'>Save</button> -->
		</form>

		<h5 class='text-xl mb-2'>Exam Sources</h5>
		<ExamSourceTable />

		<h5 class='text-xl mb-2 mt-4'>Exam Specification</h5>
		<ExamSpecificationTable v-on:save='saveExam'/>

	</div>
</template>

<script>

import ExamSourceTable from '@/components/exam/ExamSourceTable'
import ExamSpecificationTable from '@/components/exam/ExamSpecificationTable'


import {Exam} from '@/models/Exam'

export default {
	name: 'CourseForm',
	components: {
		ExamSpecificationTable,
		ExamSourceTable
	},
	props: {
	},
	data() { return {
		exam: new Exam(),
	}},
	methods: {
		saveExam() {
			this.exam.save().then(() => {
				this.$notify({title: "Exam '" + this.exam.name + "' updated.",
					type: 'success'})
				this.$router.push({name: 'examsList', params:
					{ courseId: this.$route.params.courseId }})
			}).catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: 'Failed to save exam.'})
			})
		}
	},
	mounted() {
		let examId = this.$route.params.examId
		let courseId = this.$route.params.courseId

		this.exam.id = examId
		this.exam.course_id = courseId
		this.exam.fetch().catch((error) => {
			this.$store.commit('error/add', {error: error,
				message: "Failed to get exam."})
		})
	}
}
</script>

<style>
</style>
