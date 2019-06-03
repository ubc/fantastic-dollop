<template>
	<div>

		<!-- content body -->
		<div class="pagePadding flex justify-center">
			<!-- router-view stuff will go into slot -->
			<div class='w-full lg:w-5/6 xl:w-3/4'>
				<slot />
			</div>
		</div>

	</div>
</template>

<script>
export default {
	name: 'DefaultLayout'
}
</script>

<style>
</style>
