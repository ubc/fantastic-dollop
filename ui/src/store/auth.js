// Stores the auth token in vuex, with a backup in a cookie

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
    },
    signOut(context) {
      localStorage.removeItem(TOKEN_KEY)
      context.commit('token', '')
    }
  }
}
