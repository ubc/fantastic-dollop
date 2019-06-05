<template>
	<div>
		<h3 class='text-4xl'>{{ course.$.name }}</h3>
		<p class='text-gray-700 hidden md:block'>{{ course.$.description }}</p>

		<ul class="flex my-3">
			<li class="">
				<router-link :to='{name:"examsList", params:"$route.params"}'
					>Exams</router-link>
			</li>
			<li class="">
				<router-link :to='{name:"enrolment", params:"$route.params"}'
					>Users</router-link>
			</li>
			<li class="">
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
li a {
	@apply p-2
}
.router-link-active {
	@apply border rounded border-blue-400
}
</style>
