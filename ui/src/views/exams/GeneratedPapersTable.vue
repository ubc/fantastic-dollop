<template>
	<div>
		<h3 class='text-2xl mb-2'>Midterm 1 </h3>
		<h3 class='text-xl mb-2'>2018S1</h3>
		<h4 class='text-lg mb-2'>Generated Papers List</h4>

		<input type='number' value='5' class='border border-gray-400 rounded p-2 w-20
			mr-2' />
		<button class='btnPrimary mb-3 mr-4'>
			<LabelledIcon label='Generate'><AddIcon title='Add a new exam' /></LabelledIcon>
		</button>
		<button class='btnRegular'>
			<LabelledIcon label='Download All'>
				<DownloadIcon title='Download all papers' />
			</LabelledIcon>
		</button>

		<div class='border-gray-400 border-t mb-3'>
			<!-- exam card -->
			<div v-for='exam in exams' :key='exam.name'
				class='py-2 border-b border-gray-400 flex'>
				<!-- exam info -->
				<div class='flex-auto mr-3'>
						<p class=''>
							{{ exam.name }}
						</p>
				</div>
				<!-- exam controls -->
				<div class='flex-initial self-center flex'>
					<button class='btnRegular'>
						<LabelledIcon label='Download'>
							<DownloadIcon title='Download paper' />
						</LabelledIcon>
					</button>
				</div>
			</div>
		</div>

	</div>
</template>

<script>
import AddIcon from 'icons/Plus'
import DownloadIcon from 'icons/Download'

import LabelledIcon from '@/components/util/LabelledIcon'

export default {
	name: 'CourseHome',
	components: {
		AddIcon,
		DownloadIcon,
		LabelledIcon
	},
	data() { return {
		exams: [
			{
				name: 'Paper 1'
			},
			{
				name: 'Paper 2'
			},
			{
				name: 'Paper 3'
			}
		]
	}},
	mounted() {
	}
}
</script>

<style scoped>
</style>
