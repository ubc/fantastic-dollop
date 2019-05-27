<template>
  <div>
		<h1 class='font-bold text-xl mb-2'>Admin Area</h1>
		<div class='flex pills'>
			<router-link :to='{ name: "adminUserTable" }' class='flex-initial mr-2'>
				Users
			</router-link>
			<a>
				Item 2
			</a>
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
.pills { 
	@apply mb-4;
	& a {
		@apply px-2 py-1; 
	}
}
.router-link-active {
	@apply border border-orange-400 rounded;
}
</style>
