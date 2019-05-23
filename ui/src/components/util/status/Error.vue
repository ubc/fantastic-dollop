<template>
	<div class='border border-red-600 rounded'>
		<div class='flex'>
			<div class='bg-red-600 flex-initial text-lg px-2 pb-1 text-white 
				flex items-center'>
				<ErrorIcon />
			</div>
			<div class='flex-1 px-2 py-1 text-red-700'>
				<h3 v-if='title' class='font-bold'>{{ title }}</h3>
				<p>{{ msg }}</p>
			</div>
		</div>
	</div>
</template>

<script>
import ErrorIcon from 'icons/Alert'

export default {
	name: "Error",
	components: {
		ErrorIcon
	},
	props: {
		title: String,
		msg: {
			type: String,
			required: true
		}
	}
}
</script>

<style scoped>
</style>
