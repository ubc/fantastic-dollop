<!-- Table that lists courses in the database -->
<template>
	<div>
		<router-link :to="{name: 'adminAddUser'}" tag="button" class='btnRegular mb-4' v-show='!errMsg'>
			<LabelledIcon label='Add'><AddIcon title='Add a new user' /></LabelledIcon>
		</router-link>

		<Error :msg='errMsg' v-if='errMsg'>
			<button type='button' v-on:click='getUsers' class='btn btnPrimary'>Retry</button>
		</Error>

		<div class='flex flex-col md:table'>
			<div class='hidden md:table-row'>
				<div class='p-1 font-bold md:pr-2 md:table-cell'>Name</div>
				<div class='p-1 font-bold md:pr-2 md:table-cell'>Created</div>
			</div>
			<div v-for="course in courses.models" :course="course" :key="course.id"
				class='border flex-auto p-1 border rounded mb-2 md:table-row'>
				<!-- info fields -->
				<div class='p-1 md:px-2 md:table-cell'>
					<div class='w-1/2 inline-block md:hidden'>Name</div>
					{{ course.$.name }}
				</div>

				<div class='p-1 md:px-2 md:table-cell'>
					<div class='w-1/2 inline-block md:hidden'>Created</div>
					{{ course.$.created }}
				</div>
				<!-- edit buttons -->
				<div class='flex mt-2 md:p-1 md:table-cell'>
					<div class='flex-1 md:inline-block'>
						<router-link :to="{name: 'adminEditCourse',params:{courseId: course.$.id}}"
							tag="button" class='btnRegular md:mr-2'>
							<LabelledIcon label='Edit'>
							<EditIcon title='Edit course' />
							</LabelledIcon>
						</router-link>
					</div>
					<div class='flex-initial md:inline-block'>
						<button class='btnRegular'>
							<LabelledIcon label='Delete'>
							<DeleteIcon title='Delete course' />
							</LabelledIcon>
						</button>
					</div>
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
import LabelledIcon from '@/components/util/LabelledIcon'
import Loading from '@/components/util/status/Loading'

export default {
	name: 'CourseTable',
	components: {
		AddIcon,
		EditIcon,
		Error,
		DeleteIcon,
		LabelledIcon,
		Loading
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
