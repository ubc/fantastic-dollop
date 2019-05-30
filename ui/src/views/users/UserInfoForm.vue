<!-- Form for entering user information -->
<template>
	<div>
		<Loading v-if='user.loading' />
		<form @submit.prevent='saveUser'>
			<!-- Required Fields -->
			<fieldset>
				<legend>Required</legend>

				<label for='username'>Username</label>
				<input id='username' name='username' v-model='user.username' autocomplete='username' spellcheck='false' class='border' />
				<span v-for="error in user.errors.username" v-bind:key="error">{{ error }}</span>

				<label for='password'>Password</label>
				<input id='password' name='password' v-model='user.password' type='password' v-bind:autocomplete='passwordAutocomplete' spellcheck='false' class='border' />
			</fieldset>

			<!-- Optional Fields -->
			<fieldset>
				<legend>Optional</legend>
				<!-- Using UK gov guidelines for various fields:
					https://design-system.service.gov.uk/patterns/ -->
				<label for='name'>Name</label>
				<input id='name' name='name' v-model='user.name' autocomplete='name' spellcheck='false' placeholder='John Smith' class='border' />

				<!-- autocomplete using 'given-name' instead of 'nickname', since
				nickname might be a bit too casual for our university context. -->
				<label for='preferredName'>Preferred Name</label>
				<input id='preferredName' name='preferredName' v-model='user.preferredName' spellcheck='false' autocomplete='given-name' placeholder='John' class='border' />

				<label for='email'>Email</label>
				<input id='email' name='email' v-model='user.email' type='email' spellcheck='false' autocomplete='email' class='border' />

				<label for='studentNumber'>Student Number</label>
				<input id='studentNumber' name='studentNumber' v-model='user.studentNumber' spellcheck='false' class='border' />
			</fieldset>

			<button type='submit' class='btnPrimary'>Save</button>
		</form>
	</div>
</template>

<script>
import Loading from '@/components/util/status/Loading'
import {User} from '@/models/User'

export default {
	name: 'UserInfoForm',
	components: {
		Loading
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
				console.log("we has error")
				console.log(error)
				console.log(this.user.errors)
			})
		}
	}
}
</script>

<style>
</style>
