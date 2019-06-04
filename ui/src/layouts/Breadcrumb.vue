<template>
	<div class='bg-gray-100 border-b border-gray-300 text-center text-sm md:text-base'>
		<span v-for="(breadcrumb,index) in breadcrumbs" v-bind:key='breadcrumb.path'
			class='list-none'>
			<SeparatorIcon v-if='index>0' class='mx-1' />
			<router-link :to='breadcrumb.path'>{{ breadcrumb.label }}</router-link>
		</span>
	</div>
</template>

<script>
import SeparatorIcon from 'icons/ChevronRight'

export default {
	name: "Breadcrumb",
	components: {
		SeparatorIcon
	},
	data() { return {
		breadcrumbs: []
	}},
	methods: {
		update() {
			let newBreadcrumbs = []
			newBreadcrumbs.push({path: '/', label: 'Home'})
			this.$route.matched.forEach((route) => {
				if (route.meta.breadcrumb) {
					let breadcrumb = { path: route.path, label: route.meta.breadcrumb } 
					newBreadcrumbs.push(breadcrumb)
				}
			})
			this.breadcrumbs = newBreadcrumbs
		}
	},
	mounted() {
		this.update()
	},
	watch: {
		'$route' () {
			this.update()
		}
	}
}
</script>

<style scoped>
.separator {
	@apply relative ;
}
</style>
