<template>
	<div id="app">

		<!-- header -->
		<div class='flex'>
			<div class='flex-1 border-gray-300 border-b'>
				<h1 class="text-xl font-semibold p-4">
					App Name
				</h1>
			</div>
		</div>

		<!-- content body -->
		<div class="flex">
			<!-- side nav -->
			<div class='flex-initial p-4 border-gray-300 border-r min-h-64'>
				<router-link to="/">Home</router-link> |
				<router-link to="/about">About</router-link> |
				<router-link to="/users">User</router-link>
			</div>
			<!-- content -->
			<div class='flex-1 p-4'>
				<div class='flex justify-center'>
					<router-view/>
				</div>
			</div>
		</div>

		<!-- footer -->
		<div class='flex'>
			<div class='flex-1 border-gray-300 border-t p-4'>
				footer
			</div>
		</div>

	</div>
</template>

<style>
</style>
