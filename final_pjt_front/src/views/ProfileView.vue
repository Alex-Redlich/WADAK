<template>
  <div class="ProfileView">
    <h1>Profile Page</h1>
    <UserInfo />
    <TodayMovie />
    <LikeMovies />
    <ReviewMovies />
  </div>
</template>

<script>
import UserInfo from "@/components/Profile/UserInfo"
import TodayMovie from "@/components/Profile/TodayMovie"
import LikeMovies from "@/components/Profile/LikeMovies"
import ReviewMovies from "@/components/Profile/ReviewMovies"
export default {
  name: "ProfileView",
  components: {
    UserInfo,
    TodayMovie,
    LikeMovies,
    ReviewMovies,
  },
}
</script>
