import Vue from "vue"
import VueRouter from "vue-router"
import MainView from "@/views/MainView"
import MovieDetailView from "@/views/MovieDetailView"
import ReviewView from "@/views/ReviewView"
import ProfileView from "@/views/ProfileView"
import SearchView from "@/views/SearchView"
import InventoryView from "@/views/InventoryView"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "home",
    component: MainView,
  },
  {
    path: "/movies/:moviePk",
    name: "moviedetail",
    component: MovieDetailView,
  },
  {
    path: "/popcorn-machine",
    name: "community",
    component: ReviewView,
  },
  {
    path: "/profile/:userId",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/search",
    name: "search",
    component: SearchView,
  },
  {
    path: "/:userId/inventory",
    name: "inventory",
    component: InventoryView,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
