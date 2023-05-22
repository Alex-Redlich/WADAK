<template>
  <div class="LikeMovies">
    <h1>user가 좋아하는 영화들</h1>
    <div id="LikeMovies">
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
.LikeMovies {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#LikeMovies {
  display: flex;
  justify-content: center;
}
</style>
