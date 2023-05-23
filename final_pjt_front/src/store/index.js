import Vue from "vue"
import Vuex from "vuex"
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    isLogin: false,
    user_pk: null,
  },
  getters: {},
  mutations: {
    LOGIN(state, payload) {
      state.user_pk = payload
      this.isLogin = true
    },
    LOGOUT(state) {
      state.user_pk = null
      this.isLogin = false
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
