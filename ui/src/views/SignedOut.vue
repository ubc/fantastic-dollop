<template>
	<div class='py-4'>
		<div v-show='!isSignedIn'>
			<h3 class='font-bold text-2xl text-center'>
				You are now signed out.
			</h3>
			<h6 class='mb-4 text-lg text-center'>
				Thank you and have a great day!
			</h6>
			<p class='text-center text-lg'>
			You can return to the <router-link to='/'>home page</router-link> or <router-link :to='{name: "signedInHome"}'>sign in</router-link> again.
			</p>
		</div>
		<div v-show='isSignedIn'>
			<h4 class='font-bold mb-4 text-center text-2xl'>
				You've reached the sign out page, maybe by accident?
			</h4>
			<p class='text-center text-lg'>
			Do you wish to return to the <router-link :to='{name: "signedInHome"}'>home page</router-link> or <a href v-on:click.prevent='signOut'>sign out</a>?
			</p>
		</div>
	</div>
</template>

<script>
export default {
	name: "SignedOut",
	computed: {
		isSignedIn() {
			return this.$store.getters['auth/isSignedIn']
		}
	},
	methods: {
		signOut() {
			this.$store.dispatch('auth/signOut')
		}
	}
}
</script>

<style scoped>
</style>
