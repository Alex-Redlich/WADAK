<template>
  <div class="SearchView">
    <SearchList />
  </div>
</template>

<script>
import SearchList from "@/components/Search/SearchList";
import Swal from "sweetalert2";

export default {
  name: "SearchView",
  components: {
    SearchList,
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
.SearchView {
  margin-top: 70px;
  margin-left: 200px;
  padding: 50px;
  background-color: black;
  height: 1100px;
}
</style>
