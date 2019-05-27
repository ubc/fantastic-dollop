<!-- 
	Idea is to have the labels disappear on mobile devices to save space.
	So the icons, ideally, needs to be easy to figure out by itself.
-->
<template>
	<div class='flex'>
		<div class='flex-initial md:pr-1'>
			<slot />
		</div>
		<div class='hidden md:inline md:flex-initial'>
			{{ label }}
		</div>
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
