import { createStore } from 'vuex'
import persistedstate from 'vuex-persistedstate';


const store = createStore({
  plugins: [persistedstate()],
  state: {
    page: 0,
    access_token: "",
    username: "",
    is_login: false,
    keyword: "",
    answer_page: 0,
    sort_by: 'create_date',
    desc: true,
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
    },
    setKeyword(state, keyword) {
      state.keyword = keyword
    },
    setAnswerPage(state, answer_page) {
      state.answer_page = answer_page
    },
    setSortBy(state, sort_by) {
      state.sort_by = sort_by
    },
    setDesc(state, desc) {
      state.desc = desc
    },
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
    },
    setKeyword(context, payload) {
      context.commit('setKeyword', payload)
    },
    setAnswerPage(context, payload) {
      context.commit('setAnswerPage', payload)
    },
    setSortBy(context, payload) {
      context.commit('setSortBy', payload)
    },
    setDesc(context, payload) {
      context.commit('setDesc', payload)
    },
  },
  getters: {
    getPage: (state) => state.page,
  }
})

export default store
