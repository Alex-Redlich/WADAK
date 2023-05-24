<template>
  <div class="UserToday mb-4">
    <!-- 유저 이름 태그 블럭 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="UserReviewlist_username">{{ following_nickname }}</p>
      <p id="UserReviewlist_text">님의 Today Movie</p>
    </div>
    <!-- 단독 카드 -->
    <div class="d-flex justify-content-center">
      <MovieCardOneDetail :movie="usertoday_movie" />
    </div>
  </div>
</template>

<script>
import MovieCardOneDetail from "@/components/Main/MovieCardOneDetail";
import axios from "axios";

export default {
  name: "UserToday",
  components: {
    MovieCardOneDetail,
  },
  data() {
    return {
      usertoday_movie: {},
      following_nickname: "",
    };
  },
  methods: {
    getUserToday() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/movies/8/follow/today/`,
      })
        .then((res) => {
          console.log(res.data);
          this.usertoday_movie = res.data;
          this.following_nickname = res.data.following_nickname;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getUserToday();
  },
};
</script>

<style>
#UserReviewlist_username {
  font-size: 50px;
  font-weight: 800;
  margin-right: 10px;
}
#UserReviewlist_text {
  font-size: 25px;
  font-weight: 300;
}
</style>
