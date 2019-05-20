<!-- 
	Idea is to have the labels disappear on mobile devices to save space.
	So the icons better be good.
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
	@apply text-xl;
}
 
@screen md {
	.material-design-icon {
		@apply text-base;
	}
}
</style>
