import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState({
    key:'vuex',
    storage:window.sessionStorage,
    whiteList:[],
    blackList: [],
  })],
  state: {
    isLogin: false,
    userID: null,
    userInteractions : null,
  },
  getters: {},
  mutations: {
    LOGIN(state, payload) {
      state.userID = payload;
      state.isLogin = true;
    },
    LOGOUT(state) {
      state.userID = null;
      state.isLogin = false;
    },
    USERINTERACTION_UPDATE(state, payload){
      state.userInteractions = payload
    },
  },
  actions: {
    Login(context, payload) {
      // console.log(payload);
      context.commit("LOGIN", payload);
    },
    Logout(context) {
      context.commit("LOGOUT");
    },
    UserInteractionUpdate(context, payload){
      context.commit("USERINTERACTION_UPDATE", payload.userInteractions)
    }
  },
  modules: {},
});
