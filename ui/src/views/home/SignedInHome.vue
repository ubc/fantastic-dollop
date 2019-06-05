<template>
	<div>
		<h3 class='text-2xl mb-2'>Courses</h3>

		<Error :msg='errMsg' v-if='errMsg'>
			<button type='button' v-on:click='getCourses' class='btn btnPrimary'>Retry</button>
		</Error>

		<div class='border-gray-400 border-t mb-3'>
			<!-- course card -->
			<router-link v-for="course in courses.models" :course="course"
				:key="course.id"
				:to="{name: 'courseHome', params:{courseId: course.$.id}}">
				<div class='py-2 border-b border-gray-400 flex hover:bg-yellow-100'>
					<!-- course info -->
					<div class='flex-auto mr-3'>
						<h4 class='text-xl font-medium break-all'>{{ course.$.name }}</h4>
						<p class='text-gray-700'>{{ course.$.description }}</p>
					</div>
				</div>
			</router-link>
		</div>

	</div>
</template>

<script>
import {CourseList} from '@/models/Course'	

import Error from '@/components/util/status/Error'

export default {
	name: "SignedInHome",
	components: {
		Error
	},
	data() { return {
		courses: new CourseList(),
		errMsg: ''
	}},
	methods: {
		getCourses() {
			this.courses.fetch().then(() => {
				this.errMsg = ""
			}).catch((error) => {
				this.errMsg = "Failed to get courses list: " + error.message
				if (error.response.response.status == 401) {
					this.errMsg = "Session expired, please sign in again and then click retry."
				}
			})
		}
	},
	mounted() {
		this.getCourses()
	}
}
</script>

<style scoped>
</style>
