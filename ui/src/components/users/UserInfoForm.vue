<!-- Form for entering user information -->
<template>
	<div>
		<form @submit.prevent='saveUser'>
			<!-- Required Fields -->
			<fieldset>
				<legend>Required</legend>

				<label for='username'>Username</label>
				<input id='username' name='username' v-model='username' autocomplete='username' spellcheck='false' />

				<label for='password'>Password</label>
				<input id='password' name='password' v-model='password' type='password' v-bind:autocomplete='passwordAutocomplete' spellcheck='false' />
			</fieldset>

			<!-- Optional Fields -->
			<fieldset>
				<legend>Optional</legend>
				<!-- Using UK gov guidelines for various fields:
					https://design-system.service.gov.uk/patterns/ -->
				<label for='name'>Name</label>
				<input id='name' name='name' v-model='name' autocomplete='name' spellcheck='false' placeholder='Alfie Owens' />

				<!-- autocomplete using 'given-name' instead of 'nickname', since 
				nickname might be a bit too casual for our university context. -->
				<label for='preferredName'>Preferred Name</label>
				<input id='preferredName' name='preferredName' v-model='preferredName' spellcheck='false' autocomplete='given-name' placeholder='Stormageddon' />

				<label for='email'>Email</label>
				<input id='email' name='email' v-model='email' type='email' spellcheck='false' autocomplete='email' />

				<label for='studentNumber'>Student Number</label>
				<input id='studentNumber' name='studentNumber' v-model='studentNumber' type='number' spellcheck='false' min='1000000' />
			</fieldset>

			<button type='submit'>Save</button>
		</form>
	</div>
</template>

<script>
export default {
	name: 'UserInfoForm',
	computed: {
		passwordAutocomplete: function() {
			if (this.isNewUser) return 'new-password';
			return 'current-password';
		}
	},
	props: {
		isNewUser: {
			type: Boolean,
			default: false
		}
	},
	data: function () { return {
		username: '',
		password: '',
		name: '',
		preferredName: '',
		email: '',
		studentNumber: ''
	}},
	methods: {
		saveUser: function() {
			console.log("Blah")
			this.axios.get(process.env.VUE_APP_API)
				.then(function(response) {
					console.log(response)
				})
		}
	}
}
</script>

<style>
</style>
