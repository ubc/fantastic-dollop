<template>
	<div class='block'>
		<h3 class='text-2xl text-center'>Sign In</h3>
		<form class='formVertical'>
			<label for='username'>Username</label>
			<input id='username' name='username' v-model='username' autocomplete='username' spellcheck='false' class='border' />
			<PasswordField v-model='password' />

			<button type='button' class='w-full mt-4 btnPrimary'>
				Sign In
			</button>
		</form>
	</div>
</template>

<script>
import PasswordField from '@/components/users/PasswordField'

export default {
	name: 'Login',
	components: {
		PasswordField
	},
	data() { return {
		username: null,
		password: null 
	}}
}
</script>

<style>
</style>
