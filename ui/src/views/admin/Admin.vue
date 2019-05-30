<template>
  <div>
		<h1 class='font-bold text-xl mb-2'>Admin Area</h1>
		<div class='flex pills'>
			<router-link :to='{ name: "adminCourseTable" }' class='flex-initial mr-2'>
				Courses
			</router-link>
			<router-link :to='{ name: "adminUserTable" }' class='flex-initial'>
				Users
			</router-link>
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
		@apply border border-gray-400 rounded px-2 py-1; 
		&.router-link-active {
			@apply border-orange-400;
		}
	}
}
</style>
