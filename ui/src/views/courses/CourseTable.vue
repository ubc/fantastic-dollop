<!-- Table that lists courses in the database -->
<template>
	<div>
		<h3 class='text-2xl mb-2'>Courses</h3>
		<router-link :to="{name: 'adminCourseAdd'}" tag="button" class='btnRegular mb-4' v-show='!errMsg'>
			<LabelledIcon label='Add'><AddIcon title='Add a new course' /></LabelledIcon>
		</router-link>

		<Error :msg='errMsg' v-if='errMsg'>
			<button type='button' v-on:click='getCourses' class='btn btnPrimary'>Retry</button>
		</Error>
		<Info :msg='infoMsg' v-if='infoMsg' class='mb-3'>
			<button type='button' v-on:click='infoMsg = ""' class='btn btnRegular'>
				Dismiss</button>
		</Info>

		<div class='border-gray-400 border-t mb-3'>
			<!-- course card -->
			<div v-for="course in courses.models" :course="course" :key="course.id"
				class='py-2 border-b border-gray-400 flex'>
				<!-- course info -->
				<div class='flex-auto mr-3'>
					<h4 class='text-xl font-medium break-all'>{{ course.$.name }}</h4>
					<p class='text-gray-700'>{{ course.$.description }}</p>
				</div>
				<!-- course controls -->
				<div class='flex-initial self-center flex'>
					<router-link tag="button" class='btnRegular mr-2'
						:to="{name:'adminCourseEdit',params:{courseId: course.$.id}}">
						<LabelledIcon label='Edit'>
						<EditIcon title='Edit course' />
						</LabelledIcon>
					</router-link>
					<button class='btnRegular' type='button'
						v-on:click='deleteCourse($event, course)'>
						<LabelledIcon label='Delete'>
						<DeleteIcon title='Delete course' />
						</LabelledIcon>
					</button>
				</div>
			</div>
		</div>

		<div class='flex justify-center my-2' v-show='courses.loading' >
			<Loading class='text-center' />
		</div>
	</div>
</template>

<script>
import AddIcon from 'icons/Plus'
import EditIcon from 'icons/Pencil'
import DeleteIcon from 'icons/Delete'

import {CourseList} from '@/models/Course'

import Error from '@/components/util/status/Error'
import Info from '@/components/util/status/Info'
import LabelledIcon from '@/components/util/LabelledIcon'
import Loading from '@/components/util/status/Loading'

export default {
	name: 'CourseTable',
	components: {
		AddIcon,
		EditIcon,
		Error,
		DeleteIcon,
		Info,
		LabelledIcon,
		Loading,
	},
	data() { return {
		courses: new CourseList(),
		errMsg: '',
		infoMsg: ''
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
		},
		deleteCourse(event, course) {
			let courseName = course.$.name
			course.delete().then(() => {
				this.infoMsg = "Course '" + courseName + "' was deleted."
			}).catch((error) => {
				this.errMsg = "Failed to delete course: " + error.message
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
