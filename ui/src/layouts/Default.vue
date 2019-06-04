<template>
	<div>
		<Breadcrumb />

		<!-- content body -->
		<div class="pagePadding flex justify-center">
			<!-- router-view stuff will go into slot -->
			<div class='w-full lg:w-5/6 xl:w-3/4'>
				<slot />
			</div>
		</div>

	</div>
</template>

<script>
import Breadcrumb from '@/layouts/Breadcrumb'

export default {
	name: 'DefaultLayout',
	components: {
		Breadcrumb
	}
}
</script>

<style>
</style>
