<template>
	<div>

		<!-- content body -->
		<div class="flex">
			<!-- side nav -->
			<div class='flex-initial p-4 border-gray-300 border-r min-h-64'>
				<router-link to="/">Root</router-link> |
				<router-link to="/home">Home</router-link> |
				<router-link to="/users">User</router-link>
			</div>
			<!-- content -->
			<div class='flex-1 p-4'>
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
