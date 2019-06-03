<template>
	<div class='border border-blue-600 rounded'>
		<div class='flex'>
			<div class='bg-blue-600 flex-initial text-lg px-2 pb-1 text-white 
				flex items-center'>
				<InformationIcon />
			</div>
			<div class='flex-1 px-2 py-1 text-blue-700'>
				<h3 v-if='title' class='font-bold break-all md:break-normal'>
					{{ title }}
				</h3>
				<p class='break-all md:break-normal'>{{ msg }}</p>
				<slot />
			</div>
		</div>
	</div>
</template>

<script>
import InformationIcon from 'icons/Information'

export default {
	name: "Info",
	components: {
		InformationIcon
	},
	props: {
		title: String,
		msg: String,
	}
}
</script>

<style scoped>
</style>
