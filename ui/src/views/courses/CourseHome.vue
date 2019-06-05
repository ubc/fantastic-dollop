<template>
	<div>
		<h3 class='text-2xl'>{{ course.$.name }}</h3>
		<p class='text-gray-700 hidden md:block'>{{ course.$.description }}</p>
		<Error :msg='errMsg' v-if='errMsg'></Error>

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

import Error from '@/components/util/status/Error'

export default {
	name: 'CourseHome',
	components: {
		Error
	},
	data() { return {
		course: new Course(),
		errMsg: ''
	}},
	mounted() {
		if (this.$route.params.courseId)
			this.course.id = this.$route.params.courseId
		else
			this.errMsg = 'No course ID given!'
		this.course.fetch().then(() => {
			this.errMsg = ''
		}).catch((error) => {
			this.errMsg = 'Failed to retrieve course: ' + error.message
			if (error.response.response.data)
				this.errMsg = "Failed to retrieve course: " +
					error.response.response.data.detail

		})
	}

}
</script>

<style scoped>
</style>
