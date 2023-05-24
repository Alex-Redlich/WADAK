<template>
  <div class="UserReviewList mb-4">
    <!-- 유저 이름 태그 블럭 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="UserReviewlist_username">{{ following_nickname }}</p>
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
    };
  },
  methods: {
    getUserLikeList() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/movies/1/follow/review/`,
      })
        .then((res) => {
          console.log(res.data);
          this.userreview_movies = res.data.movies;
          this.following_nickname = res.data.following_nickname;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getUserLikeList();
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
