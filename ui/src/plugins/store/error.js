// More important errors that needs to persist are stored here, so we can show
// them to the user in a non-temporary way (e.g. not toasts).
import Vue from 'vue'

export const error = {
  namespaced: true,
  state: {
    errors: [],
  },
  mutations: {
    add(state, options) {
      let errMsg = options.message + ' '
      let response = options.error.response
      if (options.error.response.response) {
        // vue-mc calls wraps axios response in another response
        response = options.error.response.response
      }
      if (response) {
        // we got a response from the server
        if (response.status == 401) {
          errMsg += 'Session expired, please try again after signing in. '
        }
        else if (response.data.detail) {
          // server gave us error detail, include it in the error message
          errMsg += response.data.detail
        }
        else if (options.error.message) {
          // no server detail, so use the generic error message
          errMsg += options.error.message
        }
      }
      else if (options.error.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the browser
        errMsg += 'Server not responding. '
      } else {
        // Something happened in setting up the request that triggered an Error
        errMsg += 'Failed to send request, check your internet connection. '
      }
      // only push unique errors
      if (!state.errors.includes(errMsg)) {
        //Vue.notify({group: 'globalError', text: options.message})
        Vue.notify({title: options.message, type: 'error'})
        state.errors.push(errMsg)
      }
    },
    remove(state, message) {
      let index = state.errors.indexOf(message)
      if (index >= 0) state.errors.splice(index, 1)
    },
    reset(state) {
      state.errors = []
    }
  },
  getters: {
    hasError(state) {
      if (state.errors.length > 0) return true
      return false
    }
  },
  actions: {
  }
}
