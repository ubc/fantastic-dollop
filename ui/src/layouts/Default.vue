<template>
	<div>

		<!-- content body -->
		<div class="flex">
			<!-- content -->
			<div class='flex-1 pagePadding'>
				<div class='flex justify-center'>
					<!-- router-view stuff will go into slot -->
					<slot />
				</div>
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
