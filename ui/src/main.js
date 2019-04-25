import Vue from 'vue'
import App from './App.vue'

// configuration for vue plugins
import router from './plugins/router'
import store from './plugins/store'

// for making http requests
import axios from 'axios'

// make axios available globally from Vue
Vue.prototype.axios = axios

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
