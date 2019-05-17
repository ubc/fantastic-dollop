<template>
	<div>
		<h3>Sign In</h3>
		<form class='form-vertical'>
			<label for='username'>Username</label>
			<input id='username' name='username' v-model='username' autocomplete='username' spellcheck='false' class='border' />
			<PasswordField v-model='password' />
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
