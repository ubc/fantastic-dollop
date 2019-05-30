<!-- Form for entering user information -->
<template>
	<div>
		<Loading v-if='course.loading' />
		<form @submit.prevent='saveCourse'>
			<!-- Required Fields -->
			<fieldset>
				<legend>Required</legend>

				<label for='name'>Name</label>
				<input id='name' name='name' v-model='user.name' spellcheck='false' class='border' />
				<span v-for="error in user.errors.username" v-bind:key="error">{{ error }}</span>
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
			console.log("fetching user")
			this.user.id = this.userId
			this.user.fetch()
			console.log(this.user)
		}
	},
	methods: {
		saveUser: function() {
			this.user.save().then( (response) => {
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
