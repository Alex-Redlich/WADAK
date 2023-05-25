<template>
  <div class="UserReviewList mb-4">
    <!-- 유저 이름 태그 블럭 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="UserReviewlist_username" @click="GoProfile">{{ following_nickname }}</p>
      <p id="UserReviewlist_text">님이 최근 리뷰를 남긴 작품들</p>
    </div>
    <!-- 카드 리스트 -->
    <div>
      <div class="row justify-content-center">
        <MovieCardLarge
          id="MovieCardUserReview"
          class="col"
          v-for="movie in userreview_movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardLarge from "@/components/Main/MovieCardLarge";
import axios from "axios";

export default {
  name: "UserReviewList",
  components: {
    MovieCardLarge,
  },
  data() {
    return {
      userreview_movies: {},
      following_nickname: "",
      userID_userreview: "",
    };
  },
  methods: {
    GoProfile() {
      console.log(this.userID_userreview);
      this.$router.push({ name: "profile", params: { userID: this.userID_userreview } });
    },
    getUserReviewList() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/movies/${this.$store.state.userID}/follow/review/`,
      })
        .then((res) => {
          this.userreview_movies = res.data.movies;
          this.following_nickname = res.data.following_nickname;
          this.userID_userreview = res.data.id;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getUserReviewList();
  },
};
</script>

<style>
#MovieCardUserReview {
  display: flex;
  justify-content: center;
}
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
