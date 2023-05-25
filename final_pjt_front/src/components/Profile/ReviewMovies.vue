<template>
  <div class="ReviewMovies">
    <div id="ReviewMovies">
      <MovieCardSmall v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Profile/MovieCardSmall";
import axios from "axios";

export default {
  name: "LikeMovies",
  data() {
    return {
      movies: {},
    };
  },
  props: {
    userID: Number,
  },
  components: {
    MovieCardSmall,
  },
  methods: {
    GetUserReview() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/accounts/profile/${this.userID}/review/`,
      })
        .then((res) => {
          this.movies = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.GetUserReview();
  },
};
</script>

<style lscoped>
.ReviewMovies {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#ReviewMovies {
  display: flex;
  justify-content: center;
}
</style>
