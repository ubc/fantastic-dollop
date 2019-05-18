import Vue from 'vue'
import App from '@/App.vue'

// configuration for vue plugins
import router from '@/plugins/router'
import store from '@/plugins/store'

// for making http requests
import axios from 'axios'

// css framework
import '@/plugins/tailwind.scss'

// svg icon set
import '@/plugins/zondicons'

// layouts
import DefaultLayout from "@/layouts/Default"
import NoSidebarLayout from "@/layouts/NoSidebar"

// make axios available globally from Vue
Vue.prototype.axios = axios

// make the layouts available
Vue.component('DefaultLayout', DefaultLayout)
Vue.component('NoSidebarLayout', NoSidebarLayout)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
