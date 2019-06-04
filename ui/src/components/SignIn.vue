<template>
	<div class='block w-5/6 md:w-1/3 lg:w-1/5 xl:w-1/6'>
		<h3 class='text-2xl text-center'>Sign in</h3>
		<Error v-if='errMsg' :msg='errMsg' class='mt-2' />
		<form class='formVertical' v-on:submit.prevent='signIn'>
			<label for='username'>Username</label>
			<input id='username' name='username' v-model='username' 
				autocomplete='username' spellcheck='false' type='text' class='w-full'
				required />
			<PasswordField v-model='password' :is-required='true' :is-full-width='true' />

			<button class='w-full mt-4 btnPrimary' :disabled='isLoading'>
					Sign in
			</button>
			<div class='block mt-2 flex justify-center' :class='{visible: isLoading, invisible: !isLoading}'>
				<Loading />
			</div>
		</form>
	</div>
</template>

<script>
import Error from '@/components/util/status/Error'
import Loading from '@/components/util/status/Loading'

import PasswordField from '@/components/users/PasswordField'

export default {
	name: 'SignIn',

	components: {
		Error,
		Loading,
		PasswordField
	},

	computed: {
		isSignedIn() {
			return this.$store.getters['auth/isSignedIn']
		}
	},

	data() { return {
		username: null,
		password: null,
		errMsg: '',
		isLoading: false
	}},

	methods: {
		signIn() {
			var formData = new FormData()
			formData.set('username', this.username)
			formData.set('password', this.password)
			this.isLoading = true;
			this.axios({
				method: 'post',
				url: '/signin',
				data: formData,
				config: { headers: {'Content-Type': 'multipart/form-data' }}
			}).then((response) => {
				//handle success
				this.isLoading = false;
				this.$store.dispatch('auth/signIn', response.data.access_token)
			}).catch((error) => {
				this.isLoading = false;
				if (error.response) {
					if (error.response.status == 404) {
						this.errMsg = "Failed to reach server. This might be a temporary issue, please wait a bit and try again."
					}
					else {
						this.errMsg = error.response.data.detail
					}
				} else if (error.request) {
					// The request was made but no response was received
					// `error.request` is an instance of XMLHttpRequest in the browser and an instance of
					// http.ClientRequest in node.js
					this.errMsg = "Server failed to respond."
				} else {
					// Something happened in setting up the request that triggered an Error
					this.errMSg = "Failed to send request, check your internet connection."
				}
			})
		}
	}

}
</script>

<style scoped>
</style>
