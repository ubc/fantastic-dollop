import axios from 'axios'
import store from '@/plugins/store'

// If request rejected because of expired tokens, sign the user out.
// For some reason, adding this interceptor onto the instance variable doesn't
// work, but adding it globally work, so that's why this is done before we 
// created the axios instance.
axios.interceptors.response.use(
  response => response,
  (error) => {
    if (error.response.status == 401 ) {
      if (store.getters['auth/isSignedIn']) store.commit('auth/rejectToken')
      store.dispatch('auth/signOut')
    }
    // pass on the error
    return Promise.reject(error)
  })

const http = axios.create()
http.defaults.baseURL = process.env.VUE_APP_API

export default http
