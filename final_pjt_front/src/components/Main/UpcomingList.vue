<template>
  <div class="UpcomingList mb-4">
    <!-- 제목 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="MovieCardUpcomingTitle">최근 영화 모음.zip</p>
    </div>
    <!-- 카드 리스트 -->
    <div>
      <div id="UpcomingList" class="row justify-content-center">
        <MovieCardSmall id="MovieCardUpcoming" class="col" v-for="movie in movies" :key="movie.id" :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Main/MovieCardSmall";
import axios from "axios";
export default {
  name: "UpcomingList",
  components: {
    MovieCardSmall,
  },
  data() {
    return {
      movies: [],
    };
  },
  methods: {
    getRecentList() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/movies/recent/",
      })
        .then((res) => {
          this.movies = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getRecentList();
  },
};
</script>

<style>
#UpcomingList {
  padding-left: 30px;
  padding-right: 30px;
}
#MovieCardUpcoming {
  display: flex;
  justify-content: center;
}
#MovieCardUpcomingTitle {
  font-size: 30px;
  font-weight: 700;
  margin-left: 20px;
  margin-top: 10px;
}
</style>
