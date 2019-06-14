<template>
	<div>
		<h3 class='text-2xl'>{{ course.$.name }}</h3>
		<p class='text-gray-700 hidden md:block'>{{ course.$.description }}</p>

		<ul class="flex my-1">
			<li class="mr-6">
				<router-link :to='{name:"enrolment", params:"$route.params"}'
					>Users</router-link>
			</li>
			<li class="mr-6">
				<a class="text-blue-500 hover:text-blue-800" href="#">Settings</a>
			</li>
		</ul>

		<router-view />
	</div>
</template>

<script>
import {Course} from '@/models/Course'

export default {
	name: 'CourseHome',
	components: {
	},
	data() { return {
		course: new Course()
	}},
	mounted() {
		this.course.id = this.$route.params.courseId
		this.course.fetch().then().catch((error) => {
			this.$store.commit('error/add', {error: error,
				message: 'Failed to retrieve course.'})
		})
	}

}
</script>

<style scoped>
</style>
