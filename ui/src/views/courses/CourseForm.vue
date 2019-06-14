<!-- Form for entering course information -->
<template>
	<div>
		<h3 class='text-2xl mb-2'>Add Course</h3>

		<Loading v-if='course.loading' />

		<form @submit.prevent='saveCourse' class='formVertical' v-show='!course.loading'>
			<!-- Required Fields -->
			<label for='name'>Name</label>
			<input id='name' name='name' v-model='course.name' spellcheck='false'
				required type='text' class='border' />
			<span v-for="error in course.errors.coursename" v-bind:key="error">{{ error }}</span>

			<label for='description'>Description</label>
			<input id='description' description='description' type='text'
				v-model='course.description' spellcheck='false' class='border' />
			<span v-for="error in course.errors.coursedescription" v-bind:key="error">{{ error }}</span>


			<button type='submit' class='btnPrimary my-3'>Save</button>
		</form>
	</div>
</template>

<script>
import Loading from '@/components/util/status/Loading'
import {Course} from '@/models/Course'


export default {
	name: 'CourseForm',
	components: {
		Loading
	},
	props: {
		courseId: {
			type: Number,
			default: null
		}
	},
	data() { return {
		course: new Course()
	}},
	mounted() {
		if (this.courseId) {
			this.course.id = this.courseId
			this.course.fetch()
		}
	},
	methods: {
		saveCourse: function() {
			this.course.save().then( () => {
				this.$router.push({'name': 'adminCourse'})
			}).catch( (error) => {
				this.$store.commit('error/add', {error: error,
					message: "Failed to save course: " + error.message})
			})
		}
	}
}
</script>

<style>
</style>
