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
		</form>

		<h5 class='text-lg mb-2'>Exam Sources</h5>
		<button class='btnRegular mb-2'>
			<UploadIcon title='Upload a new exam' class='text-lg' /> Upload
		</button>

		<div class='border-gray-400 border-t mb-3'>
			<!-- source card -->
			<div v-for='source in sources' :key='source.name'
				class='py-2 border-b border-gray-400 flex'>
				<!-- source info -->
				<div class='flex-auto mr-3'>
					<router-link to='/courses/1/sources/1'>
						<h4 class='break-all'>
							{{ source.name }}
						</h4>
					</router-link>
					<p v-if='source.isConfigured' class='text-sm text-green-600'>
					Configured
					</p>
					<p v-else class='text-sm text-red-600'>
					Not Configured Yet
					</p>
				</div>
				<!-- source controls -->
				<div class='flex-initial self-center flex'>
					<router-link tag='button' class='btnRegular mr-2'
						to='/courses/1/exams/1/sources/1/edit'>
						<LabelledIcon label='Configure'>
							<ConfigureIcon title='Configure source' />
						</LabelledIcon>
					</router-link>
					<button class='btnRegular' type='button'>
						<LabelledIcon label='Delete'>
						<DeleteIcon title='Delete source' />
						</LabelledIcon>
					</button>
				</div>
			</div>
		</div>

		<button type='submit' class='btnPrimary my-3' v-on:click='saveExam()'>Save</button>
	</div>
</template>

<script>
import UploadIcon from 'icons/Upload'
import ConfigureIcon from 'icons/Settings'
import DeleteIcon from 'icons/Delete'

import LabelledIcon from '@/components/util/LabelledIcon'

import {Exam} from '@/models/Exam'

export default {
	name: 'CourseForm',
	components: {
		ConfigureIcon,
		DeleteIcon,
		LabelledIcon,
		UploadIcon
	},
	props: {
	},
	data() { return {
		exam: new Exam(),
		sources: [
			{
				name: "2017w1 math100 midterm 1.pdf",
				isConfigured: true
			},
			{
				name: "2018w1 math100 midterm 1.pdf",
				isConfigured: false
			}
		]
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
		this.exam.id = this.$route.params.examId
		this.exam.course_id = this.$route.params.courseId
		this.exam.fetch().catch((error) => {
			this.$store.commit('error/add', {error: error,
				message: "Failed to get exam."})
		})
	}
}
</script>

<style>
</style>
