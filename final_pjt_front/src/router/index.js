import Vue from "vue";
import VueRouter from "vue-router";
import MainView from "@/views/MainView";
import MovieDetailView from "@/views/MovieDetailView";
import ReviewView from "@/views/ReviewView";
import ProfileView from "@/views/ProfileView";
import SearchView from "@/views/SearchView";
import ReviewCreateForm from "@/components/MovieDetail/ReviewCreateForm";
import ReviewDetail from "@/components/MovieDetail/ReviewDetail";
import LoginForm from "@/components/Profile/LoginForm";
import SignupForm from "@/components/Profile/SignupForm";
import UpdateForm from "@/components/Profile/UpdateForm";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: MainView,
  },
  {
    path: "/movies/:moviePK",
    name: "moviedetail",
    component: MovieDetailView,
  },
  {
    path: "/popcorn-machine",
    name: "community",
    component: ReviewView,
  },

  {
    path: "/profile/:userID",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginForm,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupForm,
  },
  {
    path: "/updateprofile/:userID",
    name: "update",
    component: UpdateForm,
  },
  {
    path: "/search",
    name: "search",
    component: SearchView,
  },

  {
    path: "/reviewcreate/:moviePK",
    name: "reviewcreate",
    component: ReviewCreateForm,
  },
  {
    path: "/reviewdetail/:reviewID",
    name: "reviewdetail",
    component: ReviewDetail,
  },
];

const router = new VueRouter({
  mode: "history",
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
  base: process.env.BASE_URL,
  routes,
});

export default router;
