<template>
  <div class="ReviewView">
    <ReviewList />
  </div>
</template>

<script>
import ReviewList from "@/components/Review/ReviewList";
import Swal from "sweetalert2";

export default {
  name: "ReviewView",
  components: {
    ReviewList,
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
.ReviewView {
  margin-top: 70px;
  margin-left: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
