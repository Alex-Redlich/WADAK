<template>
  <div class="ProfileView">
    <UserInfo />
    <div class="row">
      <div class="col-5">
        <TodayMovie />
      </div>
      <div class="col-7">
        <div class="row flex-column">
          <LikeMovies />
          <ReviewMovies />
        </div>
      </div>
    </div>
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
  data() {},
  methods: {},
}
</script>
<style scoped>
.ProfileView {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
}
</style>
