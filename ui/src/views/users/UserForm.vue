<!-- Form for entering user information -->
<template>
	<div>
		<h3 class='text-2xl'>
			<span v-show='isNewUser'>Add</span><span v-show='!isNewUser'>Edit</span>
			User
		</h3>

		<Loading v-if='user.loading' />

		<Error :msg='errMsg' v-if='errMsg'></Error>

		<form @submit.prevent='saveUser' class='formVertical'>
			<!-- Required Fields -->
			<fieldset>
				<legend>Required</legend>

				<label for='username'>Username</label>
				<input id='username' name='username' v-model='user.username' type='text'
					autocomplete='username' spellcheck='false' class='border' required />
				<span v-for="error in user.errors.username" v-bind:key="error">{{ error }}</span>

				<PasswordField v-model='user.password' :is-required='true'
					:is-new-password='isNewUser' />
			</fieldset>

			<!-- Optional Fields -->
			<fieldset>
				<legend>Optional</legend>
				<!-- Using UK gov guidelines for various fields:
					https://design-system.service.gov.uk/patterns/ -->
				<label for='name'>Name</label>
				<input id='name' name='name' v-model='user.name' autocomplete='name'
					spellcheck='false' placeholder='John Smith' class='border' type='text'/>

				<!-- autocomplete using 'given-name' instead of 'nickname', since
				nickname might be a bit too casual for our university context. -->
				<label for='preferredName'>Preferred Name</label>
				<input id='preferredName' name='preferredName' type='text'
					v-model='user.preferredName' spellcheck='false' autocomplete='given-name' placeholder='John' class='border' />

				<label for='email'>Email</label>
				<input id='email' name='email' v-model='user.email' type='email' spellcheck='false' autocomplete='email' class='border' />

				<label for='studentNumber'>Student Number</label>
				<input id='studentNumber' name='studentNumber' v-model='user.studentNumber' spellcheck='false' type='text' class='border' />
			</fieldset>

			<button type='submit' class='btnPrimary my-4'>Save</button>
		</form>
	</div>
</template>

<script>
import Error from '@/components/util/status/Error'
import Loading from '@/components/util/status/Loading'
import PasswordField from '@/components/users/PasswordField'

import {User} from '@/models/User'

export default {
	name: 'UserForm',
	components: {
		Error,
		Loading,
		PasswordField
	},
	computed: {
		passwordAutocomplete() {
			if (this.isNewUser) return 'new-password';
			return 'current-password';
		},
		isNewUser() {
			if (this.userId) return false
			return true
		}
	},
	props: {
		userId: {
			type: Number,
			default: null
		}
	},
	data() { return {
		errMsg: '',
		user: new User()
	}},
	mounted() {
		if (this.userId) {
			this.user.id = this.userId
			this.user.fetch()
		}
	},
	methods: {
		saveUser: function() {
			this.user.save().then( () => {
				this.$router.push({'name': 'adminUserTable'})
			}).catch( (error) => {
				this.errMsg = "Failed to save user: " + error.message
				if (error.response.response.status == 409)
					this.errMsg = "Failed to save user: " +
						error.response.response.data.detail
			})
		}
	}
}
</script>

<style>
</style>
