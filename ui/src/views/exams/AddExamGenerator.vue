<!-- Form for entering course information -->
<template>
	<div>
		<h3 class='text-2xl mb-2'>Midterm 1 </h3>

		<h3 class='text-xl mb-2'>Add Exam Generator</h3>

		<form class='formVertical mb-3'>
			<!-- Required Fields -->
			<label for='name'>Name</label>
			<input id='name' name='name' required type='text' value='Midterm 1'  />
		</form>

		<h5 class='text-lg mb-2'>Pages</h5>
		<button class='btnRegular mb-2 mr-2'>
			<AddIcon title='Add a question' class='text-lg' /> Add Question
		</button>
		<button class='btnRegular mb-2'>
			<AddIcon title='Add other pages' class='text-lg' /> Add Other
		</button>

		<div class='border-gray-400 border-t'></div>
		<div v-for='page in pages' :key='page.name' class='flex border-b border-gray-400 py-1 my-1'>
			<div class='flex-auto self-center'>
			{{ page.name }}
			</div>
			<div class='flex-auto mr-1 self-center'>
				<label> Source
					<select>
						<option>2017w1 math100 midterm 1.pdf</option>
						<option>2018w1 math100 midterm 1.pdf</option>
					</select>
				</label>
				<label v-if='page.hasPageSelect'> Page
					<select>
						<option>1</option>
						<option>2</option>
						<option>3</option>
						<option>4</option>
						<option>5</option>
						<option>6</option>
						<option selected>7</option>
					</select>
				</label>
				<label v-if='page.isQuestion'> Question
					<select v-model='page.question'>
						<option>1</option>
						<option>2</option>
						<option>3</option>
						<option>4</option>
						<option>5</option>
						<option>6</option>
						<option>7</option>
					</select>
				</label>

				<div class='block' v-if='page.isQuestion && page.question != 3'>
					<label> Source
						<select>
							<option>2017w1 math100 midterm 1.pdf</option>
							<option selected>2018w1 math100 midterm 1.pdf</option>
						</select>
					</label>
					<label> Question
						<select v-model='page.question'>
							<option>1</option>
							<option>2</option>
							<option>3</option>
							<option>4</option>
							<option>5</option>
							<option>6</option>
							<option>7</option>
						</select>
					</label>
					<button class='text-sm text-gray-600 ml-2'>
						Remove
					</button>
				</div>

				<div class='block mt-1' v-if='page.isQuestion'>
					<button class='btnRegular'>
						<AddIcon title='Add another source' class='text-lg' /> Add Source
					</button>
				</div>
			</div>
			<div class='flex-auto'>
				<div v-for='image in page.images' :key='image' class='inline-block mr-1'>
					<a :href='image' class=''>
						<img :src='image' class='border border-gray-300 w-20' />
					</a>
				</div>
			</div>
		</div>

		<button type='submit' class='btnPrimary my-3' v-on:click='$router.push("/courses/1/exams/1")'>Save</button>
	</div>
</template>

<script>
import AddIcon from 'icons/Plus'

export default {
	name: 'CourseForm',
	components: {
		AddIcon,
	},
	props: {
	},
	data() { return {
		pages: [
			{
				name: "ID Page",
				images: [
					require('@/assets/exams/image-01.png')
				]
			},
			{
				name: "Other",
				hasPageSelect: true,
				images: [
					require('@/assets/exams/image-01.png')
				]
			},
			{
				name: "Question 1",
				isQuestion: true,
				images: [
					require('@/assets/exams/image-02.png'),
					require('@/assets/exams/image-03.png')
				],
				question: 1
			},
			{
				name: "Question 2",
				isQuestion: true,
				images: [
					require('@/assets/exams/image-04.png'),
					require('@/assets/exams/image-05.png')
				],
				question: 2
			},
			{
				name: "Question 3",
				isQuestion: true,
				images: [
					require('@/assets/exams/image-06.png')
				],
				question: 3
			},
		]
	}},
	mounted() {
	},
	methods: {
	}
}
</script>

<style scoped>
select {
	@apply border rounded border-gray-500 p-2 bg-gray-100;
}
</style>
