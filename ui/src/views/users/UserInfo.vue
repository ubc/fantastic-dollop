<template>
	<div>
		<Loading v-if='user.loading' />

		<p>{{ user.$.username }}</p>
		<p>{{ user.$.name }}</p>
		<p>{{ user.$.preferredName }}</p>
		<p>{{ user.$.studentNumber }}</p>
		<p>{{ user.$.created }}</p>
		<p>{{ user.$.modified }}</p>


	</div>
</template>

<script>
import Loading from '@/components/util/status/Loading'
import {User} from '@/models/User'

export default {
	name: "UserInfo",
	components: {
		Loading
	},
	props: {
		userId: {
			type: Number,
			required: true
		}
	},
	data() { return {
		user: new User()
	}},
	mounted() {
		this.user.id = this.userId
		this.user.fetch()
	}
}
</script>

<style scoped>
</style>
