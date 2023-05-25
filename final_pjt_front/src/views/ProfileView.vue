<template>
  <div class="ProfileView">
    <div id="Profile">
      <div class="row">
      <div class="col-6 ">
        <TodayMovie class="d-flex align-items-center justify-content-center" />
      </div>
      <div class="col-6">
        <div class="row flex-column">
          <UserInfo />
          <LikeMovies />
          <ReviewMovies />
        </div>
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
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
  padding-top: 30px;
}
#Profile {
  background-color: white;
  width: 1500px;
  color: #6c6e70;
  border-radius: 30px;
}
</style>
