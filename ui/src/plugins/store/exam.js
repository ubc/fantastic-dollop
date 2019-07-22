// stupid hack to workaround the fact that vuemc doesn't play well with vuex

export const exam = {
  namespaced: true,
  state: {
    sources: []
  },
  mutations: {
    setSources(state, sources) {
      state.sources = sources
    },
  },
  getters: {
    getSourceMaxPageCount(state) {
      if (state.sources && state.sources.length) {
        return state.sources[0].page_count
      }
      return 0
    }
  },
  actions: {
  }
}
