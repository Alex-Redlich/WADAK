import Vue from "vue"
import VueRouter from "vue-router"
import MainView from "@/views/MainView"
import MovieDetailView from "@/views/MovieDetailView"
import ReviewView from "@/views/ReviewView"
import ProfileView from "@/views/ProfileView"
import SearchView from "@/views/SearchView"
import InventoryView from "@/views/InventoryView"
import ReviewCreateForm from "@/components/MovieDetail/ReviewCreateForm"
import ReviewDetail from "@/components/MovieDetail/ReviewDetail"
import LoginForm from "@/components/Profile/LoginForm"
import SignupForm from "@/components/Profile/SignupForm"

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
    path: "/login",
    name: "login",
    component: LoginForm,
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
  {
    path: "/:movieId/reviewcreate",
    name: "reviewcreate",
    component: ReviewCreateForm,
  },
  {
    path: "/:reviewId/reviewdetail",
    name: "reviewdetail",
    component: ReviewDetail,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupForm,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
