import "@babel/polyfill"
import "mutationobserver-shim"
import Vue from "vue"
import App from "./App.vue"
import router from "./router"
import AOS from "aos"
import "aos/dist/aos.css"
import store from "./store"

import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue"
import "bootstrap-vue/dist/bootstrap-vue-icons.min.css"

import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.config.productionTip = false

new Vue({
  router,

  render: (h) => h(App),

  store,

  mounted() {
    AOS.init()
  },
}).$mount("#app")
