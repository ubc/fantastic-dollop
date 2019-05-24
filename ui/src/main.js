import Vue from 'vue'
import App from '@/App.vue'

// configuration for vue plugins
import router from '@/plugins/router'
import store from '@/plugins/store'

// for making http requests, make axios globally available on Vue
import axios from '@/plugins/axios'

// layouts
import DefaultLayout from "@/layouts/Default"

// make the layouts available
Vue.component('DefaultLayout', DefaultLayout)

// make axios available from Vue
Vue.prototype.axios = axios

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
