<template>
	<div class='flex border-gray-300 border-b'>
		<div class='flex-auto'>
			<h1 class="font-semibold pagePadding text-lg md:text-xl">
				App Name
			</h1>
		</div>
		<div class='flex-1 pagePadding flex justify-end'>
			<!-- sign in/out -->
			<router-link to='/home' v-if='!isSignedIn'>
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
			this.$router.push({ name: 'signedOut' })
		}
	}
}
</script>

<style>
</style>
