<template>
	<div class='flex flex-col items-center w-full'>
		<notifications :duration='7000' position='top center' />
		<Error v-for='error in errors' :key='error'
			class='mb-2 w-full md:w-7/12 lg:w-1/2 xl:w-5/12'>
			<div class='flex items-stretch justify-between'>
				<!-- message area -->
				<div class='flex-auto'>
					{{ error }}
				</div>
				<!-- close button -->
				<button href='' v-on:click='remove(error)'
					class='flex-initial px-2 text-gray-500 hover:text-black'>
						<CloseIcon class='text-xl md:text-lg' />
				</button>
			</div>
		</Error>
	</div>
</template>

<script>
import CloseIcon from 'icons/Close'
import Error from '@/components/util/status/Error'

export default {
	name: "GlobalError",
	components: {
		CloseIcon,
		Error
	},
	computed: {
		errors() {
			return this.$store.state.error.errors
		}
	},
	methods: {
		remove(message) {
			this.$store.commit('error/remove', message)
		}
	}
}
</script>

<style scoped>
.vue-notification {
	font-size: 16px;
}
</style>
