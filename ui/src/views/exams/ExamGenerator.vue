<template>
	<div>
		<h3 class='text-2xl'>Midterm 1</h3>
		<h4 class='text-xl mb-2'>Exam Generators</h4>

		<router-link tag='button' class='btnPrimary mb-3'
			to='/courses/1/exams/1/generators/add'>
			<LabelledIcon label='Add'><AddIcon title='Add a new generator' /></LabelledIcon>
		</router-link>

		<div class='border-gray-400 border-t mb-3'>
			<!-- generator card -->
			<div v-for='generator in generators' :key='generator.name'
				class='py-2 border-b border-gray-400 flex'>
				<!-- generator info -->
				<div class='flex-auto mr-3'>
					<router-link to='/courses/1/exams/1/generators'>
						<h4 class='text-xl font-medium break-all'>
							{{ generator.name }}
						</h4>
					</router-link>
				</div>
				<!-- generator controls -->
				<div class='flex-initial self-center flex'>
					<router-link tag='button' class='btnRegular mr-2'
						to='/courses/1/exams/1/generators/add'>
						<LabelledIcon label='Edit'>
						<EditIcon title='Edit generator' />
						</LabelledIcon>
					</router-link>
					<button class='btnRegular' type='button'>
						<LabelledIcon label='Delete'>
						<DeleteIcon title='Delete generator' />
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
		generators: [
			{
				name: '2019S1'
			},
			{
				name: 'test'
			}
		]
	}},
	mounted() {
	}
}
</script>

<style scoped>
</style>
