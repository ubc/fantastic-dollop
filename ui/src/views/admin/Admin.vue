<template>
  <div>
		<h1 class='font-bold text-xl mb-2'>Admin Area</h1>
		<div class='flex'>
			<router-link :to='{ name: "adminUserTable" }' class='flex-initial mr-2'>
				Users
			</router-link>
			<div class='flex-initial'>
				Item 2
			</div>
		</div>
		<router-view />
  </div>
</template>

<script>
export default {
  name: 'AdminHome'
}
</script>

<style scoped>
</style>
