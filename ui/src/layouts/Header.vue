<template>
	<div class='flex border-gray-300 border-b'>
		<div class='flex-auto bg-gray-100'>
			<h1 class="text-xl font-semibold p-4">
				App Name
			</h1>
		</div>
		<div class='flex-1 p-4 flex justify-end'>
			<router-link to='signin' v-if='!isSignedIn'>
				<LabelledIcon label='Sign in'>
					<SignInIcon title="Sign in" />
				</LabelledIcon>
			</router-link>
			<a href='' v-on:click.prevent='signOut' v-if='isSignedIn'>
				<LabelledIcon label='Sign out'>
					<SignOutIcon title="Sign out" />
				</LabelledIcon>
			</a>
		</div>
	</div>
</template>

<script>
import LabelledIcon from '@/components/util/LabelledIcon'

import SignInIcon from 'icons/Account'
import SignOutIcon from 'icons/Logout'

export default {
	name: 'Header',
	components: {
		LabelledIcon,
		SignInIcon,
		SignOutIcon
	},
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

<style>
</style>
