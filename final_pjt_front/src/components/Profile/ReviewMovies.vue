<template>
  <div class="ReviewMovies">
    <h1>user 최근 남긴 영화들</h1>
    <div id="ReviewMovies">
      <div v-for="card in 3" :key="card">
        <MovieCardSmall />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Profile/MovieCardSmall";
export default {
  name: "LikeMovies",
  components: {
    MovieCardSmall,
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
