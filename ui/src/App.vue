<template>
	<div id="app">

		<Header />

		<!-- content body -->
		<component :is="layout">
			<router-view />
		</component>

		<Footer />

	</div>
</template>

<script>
import Header from '@/layouts/Header'
import Footer from '@/layouts/Footer'

const DEFAULT_LAYOUT = "Default"

export default {
	name: 'App',
	components: {
		Header,
		Footer
	},
	computed: {
		layout() {
			return (this.$route.meta.layout || DEFAULT_LAYOUT) + 'Layout'
		}
	}
}
</script>

<style>
</style>
