<template>
	<div>
		<!-- content body -->
		<div class="flex">
			<!-- content -->
			<div class='flex-auto p-4'>
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
	name: 'NoSidebarLayout'
}
</script>

<style>
</style>

