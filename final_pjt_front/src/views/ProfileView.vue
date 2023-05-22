<template>
  <div class="ProfileView">
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
<style scoped>
.ProfileView {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
}
</style>
