<!-- Table that lists courses in the database -->
<template>
	<div>
		<h3 class='text-2xl mb-2'>Courses</h3>
		<router-link :to="{name: 'adminCourseAdd'}" tag="button" class='btnRegular mb-4'>
			<LabelledIcon label='Add'><AddIcon title='Add a new course' /></LabelledIcon>
		</router-link>

		<div class='border-gray-400 border-t mb-3'>
			<p class='text-center text-lg py-1' v-if='courses.models.length == 0'>
			No courses found.
			</p>
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
						:to="{name:'adminCourseEdit', params:{courseId: course.$.id}}">
						<LabelledIcon label='Edit'>
							<EditIcon title='Edit course' />
						</LabelledIcon>
					</router-link>

					<router-link tag="button" class='btnRegular mr-2'
						:to="{name:'adminCourseEnrolment', params:{courseId: course.$.id}}">
						<LabelledIcon label='Enrolment'>
							<EnrolmentIcon title='Course enrolment' />
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
import EnrolmentIcon from 'icons/AccountMultiple'
import DeleteIcon from 'icons/Delete'

import {CourseList} from '@/models/Course'

import LabelledIcon from '@/components/util/LabelledIcon'
import Loading from '@/components/util/status/Loading'

export default {
	name: 'CourseTable',
	components: {
		AddIcon,
		EditIcon,
		EnrolmentIcon,
		DeleteIcon,
		LabelledIcon,
		Loading,
	},
	data() { return {
		courses: new CourseList()
	}},
	methods: {
		getCourses() {
			this.courses.fetch().then().catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: 'Failed to get courses.'})
			})
		},
		deleteCourse(event, course) {
			let courseName = course.$.name
			course.delete().then(() => {
				this.$notify({title: "Course '" + courseName + "' was deleted.",
					type: 'success'})
			}).catch((error) => {
				this.$store.commit('error/add', {error: error,
					message: 'Failed to delete course.'})
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
