import { createStore } from 'vuex'
import persistedstate from 'vuex-persistedstate';


const store = createStore({
  plugins: [persistedstate()],
  state: {
    page: 0,
    access_token: "",
    username: "",
    is_login: false 
  },
  mutations: {
    setPage(state, payload) {
      state.page = payload
    },
    setAccessToken(state, token) {
      state.access_token = token
    },
    setUsername(state, username) {
      state.username = username
    },
    setIsLogin(state, is_login) {
      state.is_login = is_login
    }
  },
  actions: {
    setPage(context, payload) {
      context.commit('setPage', payload)
    },
    setAccessToken(context, payload) {
      context.commit('setAccessToken', payload)
    },
    setUsername(context, payload) {
      context.commit('setUsername', payload)
    },
    setIsLogin(context, payload) {
      context.commit('setIsLogin', payload)
    }
  },
  getters: {
    getPage: (state) => state.page,
  }
})

export default store