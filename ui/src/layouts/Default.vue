<template>
	<div>

		<!-- content body -->
		<div class="pagePadding flex justify-center">
			<!-- router-view stuff will go into slot -->
			<div class='flex-auto md:flex-initial'>
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
