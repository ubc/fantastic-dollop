<!-- Form for entering course information -->
<template>
	<div>
		<h3 class='text-2xl mb-2'>Configure Exam Source</h3>

		<form class='formVertical mb-3'>
			<!-- Required Fields -->
			<label for='name'>Name</label>
			<input id='name' name='name' required type='text' value='2018w1 math100 midterm 1.pdf'  />
		</form>

		<h5 class='text-lg mb-2'>Pages</h5>
		<div class='border-b border-gray-400'></div>
		<div v-for='page in pages' :key='page.page' class='pt-2 pb-4 my-2 border-b
			border-gray-400 flex'>
			<div class='self-center flex-initial px-4 mr-4'>
				{{ page.page }}	
			</div>
			<div class='border flex-initial mr-4'>
				<a :href='page.scan'>
					<img :src='page.scan' class='h-40' />
				</a>
			</div>
			<div class='self-center flex-auto'>
				<select v-model='page.select' class='border rounded border-gray-500 p-2 bg-gray-100 md:mr-3'>
					<option value='null' disabled selected>-- Select Page Type --</option>
					<option value='1'>Ignore</option>
					<option value='2'>ID Page</option>
					<option value='3'>Question 1</option>
					<option value='4'>Question 2</option>
					<option value='5'>Question 3</option>
					<option value='6'>Question 4</option>
					<option value='7'>Question 5</option>
					<option value='8'>Question 6</option>
					<option value='9'>Question 7</option>
					<option value='10'>Question 8</option>
					<option value='11'>Question 9</option>
					<option value='12'>Question 10</option>
					<option value='13'>Question 11</option>
				</select>
				<button class='btnRegular mt-2 md:mt-0' v-on:click='page.select=13'>
						<AddIcon title='New Question' />
						New Question
				</button>
			</div>
		</div>

		<button type='submit' class='btnPrimary my-3' v-on:click='$router.push("/courses/1/exams/add")'>Save</button>
	</div>
</template>

<script>
import AddIcon from 'icons/Plus'


export default {
	name: 'CourseForm',
	components: {
		AddIcon
	},
	props: {
	},
	data() { return {
		pages: [
			{
				page: 1,
				scan: require('@/assets/exams/image-01.png'),
				select: 2
			},
			{
				page: 2,
				scan: require('@/assets/exams/image-02.png'),
				select: 3
			},
			{
				page: 3,
				scan: require('@/assets/exams/image-03.png'),
				select: 4
			},
			{
				page: 4,
				scan: require('@/assets/exams/image-04.png'),
				select: 5
			},
			{
				page: 5,
				scan: require('@/assets/exams/image-05.png'),
				select: 6
			},
			{
				page: 6,
				scan: require('@/assets/exams/image-06.png'),
				select: 7
			},
			{
				page: 7,
				scan: require('@/assets/exams/image-07.png'),
				select: 8
			},
			{
				page: 8,
				scan: require('@/assets/exams/image-08.png'),
				select: 9
			},
			{
				page: 9,
				scan: require('@/assets/exams/image-09.png'),
				select: 10 
			},
			{
				page: 10,
				scan: require('@/assets/exams/image-10.png'),
				select: 11
			},
			{
				page: 11,
				scan: require('@/assets/exams/image-11.png'),
				select: 12 
			},
			{
				page: 12,
				scan: require('@/assets/exams/image-12.png'),
				select: null 
			}
		]
	}},
	mounted() {
	},
	methods: {
	}
}
</script>

<style>
</style>
