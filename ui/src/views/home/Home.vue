<template>
  <div class="flex flex-col md:flex-row">
		<div class='flex-1 p-2'>
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum dui faucibus in ornare quam viverra orci sagittis. Porttitor rhoncus dolor purus non enim. Dolor sit amet consectetur adipiscing elit duis. Scelerisque in dictum non consectetur a erat. Sem nulla pharetra diam sit amet. Ut pharetra sit amet aliquam id diam maecenas ultricies mi. Mauris augue neque gravida in fermentum et sollicitudin ac orci. Purus gravida quis blandit turpis cursus. Ipsum consequat nisl vel pretium lectus quam id. Tincidunt augue interdum velit euismod in pellentesque. Facilisi cras fermentum odio eu feugiat. Sit amet risus nullam eget felis. Id diam maecenas ultricies mi eget. Elementum tempus egestas sed sed risus pretium quam vulputate dignissim. Morbi tristique senectus et netus et.</p>
			<p>Euismod elementum nisi quis eleifend quam adipiscing vitae proin. Facilisis sed odio morbi quis commodo odio aenean sed adipiscing. Amet est placerat in egestas erat imperdiet sed euismod nisi. Suspendisse ultrices gravida dictum fusce ut. Consectetur a erat nam at lectus urna. Ac turpis egestas maecenas pharetra convallis posuere morbi leo. Et pharetra pharetra massa massa ultricies mi quis hendrerit dolor. Mauris vitae ultricies leo integer malesuada nunc vel risus. Amet cursus sit amet dictum sit. Turpis egestas pretium aenean pharetra magna. Sit amet mattis vulputate enim nulla. Facilisis volutpat est velit egestas dui. Tristique senectus et netus et malesuada fames ac turpis egestas. Feugiat scelerisque varius morbi enim nunc faucibus a. Volutpat sed cras ornare arcu dui. Dui vivamus arcu felis bibendum. Non nisi est sit amet facilisis magna etiam tempor. In nulla posuere sollicitudin aliquam ultrices. Lacus laoreet non curabitur gravida. Morbi tincidunt ornare massa eget egestas purus viverra.</p>
		</div>
		<div class='flex-1 p-2'>
			<div class='mb-4 text-center'>
				<router-link :to='{name:"signedInHome"}' tag='button' class='btnPrimary'>
					Sign in</router-link>
			</div>
			<p>Et sollicitudin ac orci phasellus. At auctor urna nunc id cursus metus aliquam. Tellus elementum sagittis vitae et leo. Varius morbi enim nunc faucibus a pellentesque sit. Non nisi est sit amet. Pellentesque massa placerat duis ultricies lacus sed turpis. Lectus urna duis convallis convallis tellus id. Feugiat nisl pretium fusce id velit ut tortor pretium viverra. A lacus vestibulum sed arcu non odio euismod lacinia. At urna condimentum mattis pellentesque id nibh. Leo urna molestie at elementum eu facilisis sed. Fermentum iaculis eu non diam phasellus. Sed odio morbi quis commodo odio aenean. Leo urna molestie at elementum.</p>
			<p>At in tellus integer feugiat scelerisque varius morbi enim. Posuere lorem ipsum dolor sit. Faucibus scelerisque eleifend donec pretium vulputate sapien. Lorem dolor sed viverra ipsum nunc aliquet bibendum enim facilisis. Vivamus at augue eget arcu dictum. Eget nullam non nisi est sit amet facilisis magna. Malesuada proin libero nunc consequat interdum. Volutpat ac tincidunt vitae semper quis lectus nulla. Morbi blandit cursus risus at ultrices mi tempus imperdiet nulla. Metus aliquam eleifend mi in. Pulvinar etiam non quam lacus suspendisse faucibus interdum posuere lorem.</p>
		</div>
  </div>
</template>

<script>
export default {
  name: 'home',
  components: {
  },
	computed: {
		isSignedIn() {
			return this.$store.getters['auth/isSignedIn']
		}
	},
	mounted() {
		if (this.isSignedIn)
			this.$router.replace({ name: 'signedInHome' })
	}
}
</script>

<style scoped>
p {
	@apply mb-4;
}
</style>
