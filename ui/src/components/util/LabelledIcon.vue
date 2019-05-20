<!-- 
	Idea is to have the labels disappear on mobile devices to save space.
	So the icons, ideally, needs to be easy to figure out by itself.
-->
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
.material-design-icon {
	@apply text-2xl;
}
 
@screen md {
	.material-design-icon {
		@apply text-lg;
	}
}
</style>
