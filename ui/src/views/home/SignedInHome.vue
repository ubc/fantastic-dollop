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
	computed: {
		isSignedIn() {
			return this.$store.getters['auth/isSignedIn']
		}
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
			})
		}
	},
	mounted() {
		// will get rejected with 401 if we try to get courses without being signed in
		// since we only show the sign in page if user isn't signed in and we're using
		// using this home page as a proxy for the sign in page, we need to take some
		// care to make sure errors don't show up on first sign in. Was previously
		// checking for 401 errors and that caused the error message to show up even
		// on initial sign ins
		if (this.isSignedIn) this.getCourses()
	},
	watch: {
		isSignedIn: function (signedIn) {
			// make sure user can see the list of courses once they're signed in
			if (signedIn) this.getCourses()
		}
	}
}
</script>

<style scoped>
</style>
