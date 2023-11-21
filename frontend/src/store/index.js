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
        setPage: (state, payload) => state.page = payload ,
        setAccessToken: (state, payload) => state.access_token = payload, 
        setUsername: (state, payload) => state.username = payload,
        setIsLogin: (state, payload) => state.is_login = payload,
        setKeyword: (state, payload) => state.keyword = payload,
        setAnswerPage: (state, payload) => state.answer_page = payload,
        setSortBy: (state, payload) => state.sort_by = payload,
        setDesc: (state, payload) => state.desc = payload,
    },
    actions: {
        setPage: ({commit}, payload) => commit('setPage', payload),
        setAccessToken: ({commit}, payload) => commit('setAccessToekn', payload),
        setUsername: ({commit}, payload) => commit('setUsername', payload),
        setIsLogin: ({commit}, payload) => commit('setIsLogin', payload),
        setKeyword: ({commit}, payload) => commit('setKeyword', payload),
        setAnswerPage: ({commit}, payload) => commit('setAnswerPage', payload),
        setSortBy: ({commit}, payload) => commit('setSortBy', payload),
        setDesc: ({commit}, payload) => commit('setDesc', payload),
    },
})

export default store
