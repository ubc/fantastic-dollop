<template>
	<div id="app">

		<Header />

		<!-- Trying to make the sign in more seamless. Sign in is available in the
		entire app, we just need to show it if the user is accessing a page that
		needs sign in. Once they are signed in, the form should automatically
		disappear and the page they were on gets unhidden. -->
		<div class='pagePadding flex justify-center' v-if='needSignIn'>
			<SignIn />
		</div>

		<!-- Main content. Note that v-show only hides/unhides while v-if destroys
		the elements in DOM. We don't want the destructive 'v-if' cause it'll
		destroy any unsaved data the user was working on at the time. If user's
		token expired in the middle of something, they just need to log back in and
		won't have to redo stuff. -->
		<component :is="layout" v-show='!needSignIn'>
			<router-view />
		</component>

		<Footer />

	</div>
</template>

<script>
import Header from '@/layouts/Header'
import Footer from '@/layouts/Footer'
import SignIn from '@/components/SignIn'

const DEFAULT_LAYOUT = "Default"

export default {
	name: 'App',
	components: {
		Header,
		Footer,
		SignIn
	},
	computed: {
		layout() {
			return (this.$route.meta.layout || DEFAULT_LAYOUT) + 'Layout'
		},
		isSignedIn() {
			return this.$store.getters['auth/isSignedIn']
		},
		needSignIn() {
			if (this.$route.meta.isPublic) return false
			if (this.isSignedIn) return false
			return true
		}
	},
	watch: {
		'$route' () {
			// reset errors on page navigate
			this.$store.commit('error/reset')
		}
	}
}
</script>

<style>
@import 'assets/styles/tailwind.css';
</style>
