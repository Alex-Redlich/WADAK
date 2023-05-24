import Vue from "vue"
import Vuex from "vuex"
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    isLogin: false,
    userID: 1,
  },
  getters: {},
  mutations: {
    LOGIN(state, payload) {
      state.userID = payload
      state.isLogin = true
    },
    LOGOUT(state) {
      state.userID = null
      state.isLogin = false
    },
  },
  actions: {
    Login(context, payload) {
      context.commit("LOGIN", payload)
    },
    Logout(context) {
      context.commit("LOGOUT")
    },
  },
  modules: {},
})
