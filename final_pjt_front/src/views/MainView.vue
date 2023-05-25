<template>
  <div class="MainView">
    <!-- <h1>Main Page</h1> -->
    <RankerList />
    <UserLikeList />
    <PopularList />
    <UserToday />
    <UpcomingList />
    <UserReviewList />
  </div>
</template>

<script>
import RankerList from "@/components/Main/RankerList";
import UserLikeList from "@/components/Main/UserLikeList";
import PopularList from "@/components/Main/PopularList";
import UserToday from "@/components/Main/UserToday";
import UpcomingList from "@/components/Main/UpcomingList";
import UserReviewList from "@/components/Main/UserReviewList";
import Swal from "sweetalert2";

export default {
  name: "MainView",
  components: {
    RankerList,
    UserLikeList,
    PopularList,
    UserToday,
    UpcomingList,
    UserReviewList,
  },
  computed: {
    isLogin() {
      return this.$store.state.isLogin;
    },
  },
  methods: {
    loginAlert() {
      if (!this.isLogin) {
        Swal.fire("로그인이 필요한 서비스 입니다", "", "error");
        this.$router.push({ name: "login" });
      }
    },
  },
  created() {
    this.loginAlert();
  },
};
</script>
<style scoped>
.MainView {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
  /* border: outset #f5df4d; */
}
</style>
