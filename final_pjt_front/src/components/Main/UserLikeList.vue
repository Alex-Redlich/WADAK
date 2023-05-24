<template>
  <div class="UserLikeList mb-4">
    <!-- 유저 이름 태그 블럭 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="UserLikeList_username">{{ following_nickname }}</p>
      <p id="UserLikeList_text">님이 좋아하는 영화들</p>
    </div>
    <!-- 카드 리스트 -->
    <div>
      <div class="row justify-content-center">
        <MovieCardLarge
          id="MovieCardPopular"
          class="col"
          v-for="movie in userlike_movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieCardLarge from "@/components/Main/MovieCardLarge";
export default {
  name: "UserLikeList",
  components: {
    MovieCardLarge,
  },
  data() {
    return {
      userlike_movies: {},
      following_nickname: "",
    };
  },
  methods: {
    getUserLikeList() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/movies/1/follow/like/`,
      })
        .then((res) => {
          console.log(res.data);
          this.userlike_movies = res.data.movies;
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
#MovieCardUserList {
  display: flex;
  justify-content: center;
}
#UserLikeList_username {
  font-size: 50px;
  font-weight: 800;
  margin-right: 10px;
}
#UserLikeList_text {
  font-size: 25px;
  font-weight: 300;
}
</style>
