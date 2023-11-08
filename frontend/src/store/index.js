import { createStore } from 'vuex'
import persistedstate from 'vuex-persistedstate';


const store = createStore({
  plugins: [persistedstate()],
  state: {
    page: 0
  },
  mutations: {
    setPage(state, payload) {
      state.page = payload
    }
  },
  actions: {
    setPage(context, payload) {
      context.commit('setPage', payload)
    }
  },
  getters: {
    getPage: (state) => state.page
  }
})

export default store
