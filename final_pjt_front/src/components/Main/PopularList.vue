<template>
  <div class="PopularList mb-4">
    <!-- 제목 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="PopularListTitle">지금 인기있는 영화들!</p>
    </div>
    <!-- 카드 리스트 -->
    <div>
      <div id="PopularList" class="row justify-content-center">
        <MovieCardSmall id="MovieCardPopular" class="col" v-for="movie in movies" :key="movie.id" :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Main/MovieCardSmall";
import axios from "axios";
export default {
  name: "PopularList",
  components: {
    MovieCardSmall,
  },
  data() {
    return {
      movies: {},
    };
  },
  methods: {
    getPopularList() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/movies/popular/",
      })
        .then((res) => {
          this.movies = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getPopularList();
  },
};
</script>

<style>
#PopularList {
  padding-left: 30px;
  padding-right: 30px;
}
#MovieCardPopular {
  display: flex;
  justify-content: center;
}
#PopularListTitle {
  font-size: 30px;
  font-weight: 700;
  margin-left: 20px;
  margin-top: 10px;
}
</style>
