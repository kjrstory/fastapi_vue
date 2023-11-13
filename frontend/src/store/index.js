import { createStore } from 'vuex'
import persistedstate from 'vuex-persistedstate';


const store = createStore({
    plugins: [persistedstate()],
    state: {
        page: 0
    },
    mutations: {
        setPage: (state, payload) => state.page = payload 
    },
    actions: {
        setPage: ({commit}, payload) => commit('setPage', payload)
    },
})

export default store
