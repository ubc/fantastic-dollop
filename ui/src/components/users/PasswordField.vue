<template>
	<div>
		<label for='password'>Password</label>
		<input id='password' name='password' 
			spellcheck='false' class='w-full' 
			v-bind:type='passwordType' 
			v-bind:autocomplete='passwordAutocomplete' 
			v-bind:value='password'
			v-bind:required='isRequired'
			v-bind:disabled='isDisabled'
			v-on:input='onPasswordInput'
			/>
		<a @click='togglePasswordVisible' class='block mt-1'>
			<EyeOffIcon v-if='showPassword' />
			<EyeIcon v-else />
			{{ showPassword ? 'hide' : 'show' }} password
		</a>
	</div>
</template>

<script>
import EyeIcon from 'icons/Eye'
import EyeOffIcon from 'icons/EyeOff'

export default {
	name: "PasswordField",
	components: {
		EyeIcon,
		EyeOffIcon
	},
	computed: {
		passwordAutocomplete() {
			if (this.isNewPassword) return 'new-password'
			return 'current-password'
		}
	},
	data() { return {
		passwordType: 'password',
		password: '',
		showPassword: false
	}},
	props: {
		isNewPassword: Boolean,
		isRequired: {
			type: Boolean,
			default: false
		},
		isDisabled: {
			type: Boolean,
			default: false
		}
	},
	methods: {
		onPasswordInput(event) {
			this.$emit("input", event.target.value)
			this.password = event.target.value
		},
		togglePasswordVisible() {
			this.passwordType = this.passwordType == 'password' ? 'text' : 'password'
			this.showPassword = !this.showPassword
		}
	}
}
</script>

<style type='scss'>
</style>
