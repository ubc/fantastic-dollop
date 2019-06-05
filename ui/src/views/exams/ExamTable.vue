<template>
	<div>
		<h4 class='text-xl mb-2'>Exams List</h4>

		<router-link tag='button' class='btnPrimary mb-3'
			to='/courses/1/exams/add'>
			<LabelledIcon label='Add'><AddIcon title='Add a new exam' /></LabelledIcon>
		</router-link>

		<div class='border-gray-400 border-t mb-3'>
			<!-- exam card -->
			<div v-for='exam in exams' :key='exam.name'
				class='py-2 border-b border-gray-400 flex'>
				<!-- exam info -->
				<div class='flex-auto mr-3'>
					<router-link to='/courses/1/exams/1'>
						<h4 class='text-xl font-medium break-all'>
							{{ exam.name }}
						</h4>
					</router-link>
				</div>
				<!-- exam controls -->
				<div class='flex-initial self-center flex'>
					<router-link tag='button' class='btnRegular mr-2'
						to='/courses/1/exams/1/edit'>
						<LabelledIcon label='Edit'>
						<EditIcon title='Edit exam' />
						</LabelledIcon>
					</router-link>
					<button class='btnRegular' type='button'>
						<LabelledIcon label='Delete'>
						<DeleteIcon title='Delete exam' />
						</LabelledIcon>
					</button>
				</div>
			</div>
		</div>

	</div>
</template>

<script>
import AddIcon from 'icons/Plus'
import EditIcon from 'icons/Pencil'
import DeleteIcon from 'icons/Delete'

import LabelledIcon from '@/components/util/LabelledIcon'

export default {
	name: 'CourseHome',
	components: {
		AddIcon,
		EditIcon,
		DeleteIcon,
		LabelledIcon
	},
	data() { return {
		exams: [
			{
				name: 'Midterm 1'
			},
			{
				name: 'Midterm 2'
			},
			{
				name: 'Final'
			}
		]
	}},
	mounted() {
	}
}
</script>

<style scoped>
</style>
