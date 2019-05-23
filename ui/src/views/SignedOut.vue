<template>
	<div class='py-4'>
		<h3 class='font-bold text-2xl text-center'>
			You are now signed out.
		</h3>
		<h6 class='mb-4 text-lg text-center'>
			Thank you and have a great day!
		</h6>
		<p class='text-center'>
		You can return to the <router-link to='/'>home page</router-link> or <router-link :to='{name: "signedInHome"}'>sign in</router-link> again.
		</p>
	</div>
</template>

<script>
export default {
	name: "SignedOut"
}
</script>

<style scoped>
</style>
