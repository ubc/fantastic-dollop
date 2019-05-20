<template>
	<div class='flex border-gray-300 border-b'>
		<div class='flex-auto bg-gray-100'>
			<h1 class="text-xl font-semibold p-4">
				App Name
			</h1>
		</div>
		<div class='flex-1 p-4 flex justify-end'>
			<router-link to='signin'>
				<LabelledIcon label='Sign in'>
					<SignInIcon title="Sign in" />
				</LabelledIcon>
			</router-link>
		</div>
	</div>
</template>

<script>
import LabelledIcon from '@/components/util/LabelledIcon'

import SignInIcon from 'icons/Account'

export default {
	name: 'Header',
	components: {
		LabelledIcon,
		SignInIcon
	}
}
</script>

<style>
</style>
