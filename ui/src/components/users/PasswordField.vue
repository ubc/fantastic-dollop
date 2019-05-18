<template>
	<div>
		<label for='password'>Password</label>
		<input id='password' name='password' 
			spellcheck='false' class='border' 
			v-bind:type='passwordType' 
			v-bind:autocomplete='passwordAutocomplete' 
			v-bind:value='password'
			v-on:input='onPasswordInput'
			/>
		<a @click='togglePasswordVisible' class='block mt-1'>
			<Zondicon :icon="showPasswordIcon" class='zicon' />
			{{ showOrHide }} password
		</a>
	</div>
</template>

<script>
export default {
	name: "PasswordField",
	computed: {
		passwordAutocomplete() {
			if (this.isNewPassword) return 'new-password'
			return 'current-password'
		}
	},
	data() { return {
		passwordType: 'password',
		password: '',
		showPasswordIcon: 'view-show',
		showOrHide: 'show'
	}},
	props: {
		isNewPassword: Boolean
	},
	methods: {
		onPasswordInput(event) {
			this.$emit("input", event.target.value)
			this.password = event.target.value
		},
		togglePasswordVisible() {
			this.passwordType = this.passwordType == 'password' ?
				'text':'password'
			this.showPasswordIcon = this.showPasswordIcon == 'view-show' ?
				'view-hide' : 'view-show'
			this.showOrHide = this.showOrHide == 'show' ?
				'hide' : 'show'
		}
	}
}
</script>

<style type='scss'>
</style>
