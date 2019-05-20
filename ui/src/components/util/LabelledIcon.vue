<template>
	<div>
		<slot />
		<span class='hidden md:inline'>
			{{ label }}
		</span>
	</div>
</template>

<script>
export default {
	name: 'LabelledIcon',
	props: {
		label: String
	}
}
</script>

<style scoped>
</style>
