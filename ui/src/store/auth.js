// Stores the auth token in vuex, with a backup in a cookie

import axios from 'axios'

export const TOKEN_KEY = 'token'

export const auth = {
  namespaced: true,
  state: {
    token: localStorage.getItem(TOKEN_KEY) || ''
  },
  mutations: {
    token(state, token) {
      state.token = token
    }
  },
  getters: {
    isSignedIn: (state) => {
      if (state.token) return true
      return false
    }
  },
  actions: {
    signIn(context, token) {
      localStorage.setItem(TOKEN_KEY, token)
      context.commit('token', token)
      axios.defaults.headers.common['Authorization'] = "Bearer " + token
    },
    signOut(context) {
      localStorage.removeItem(TOKEN_KEY)
      context.commit('token', '')
      delete axios.defaults.headers.common["Authorization"]
    }
  }
}

// make sure we're authed on page load if there's a stored token
if (localStorage.getItem(TOKEN_KEY))
  axios.defaults.headers.common['Authorization'] = "Bearer " + localStorage.getItem(TOKEN_KEY)
