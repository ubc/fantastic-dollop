<!-- Form for entering course information -->
<template>
	<div>
		<h3 class='text-2xl mb-2'>Add Course</h3>

		<Loading v-if='course.loading' />

		<Error :msg='errMsg' v-if='errMsg'></Error>

		<form @submit.prevent='saveCourse' class='formVertical' v-show='!course.loading'>
			<!-- Required Fields -->
			<label for='name'>Name</label>
			<input id='name' name='name' v-model='course.name' spellcheck='false' class='border' required />
			<span v-for="error in course.errors.coursename" v-bind:key="error">{{ error }}</span>

			<label for='description'>Description</label>
			<input id='description' description='description'
				v-model='course.description' spellcheck='false' class='border' />
			<span v-for="error in course.errors.coursedescription" v-bind:key="error">{{ error }}</span>


			<button type='submit' class='btnPrimary my-3'>Save</button>
		</form>
	</div>
</template>

<script>
import Loading from '@/components/util/status/Loading'
import {Course} from '@/models/Course'
import Error from '@/components/util/status/Error'


export default {
	name: 'CourseForm',
	components: {
		Error,
		Loading
	},
	props: {
		courseId: {
			type: Number,
			default: null
		}
	},
	data() { return {
		course: new Course(),
		errMsg: ''
	}},
	mounted() {
		if (this.courseId) {
			console.log("fetching course")
			this.course.id = this.courseId
			this.course.fetch()
			console.log(this.course)
		}
	},
	methods: {
		saveCourse: function() {
			this.course.save().then( () => {
				this.$router.push({'name': 'adminCourse'})
			}).catch( (error) => {
				this.errMsg = "Failed to save course: " + error.message
			})
		}
	}
}
</script>

<style>
</style>
