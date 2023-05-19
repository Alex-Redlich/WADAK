<template>
  <div class="LikeMovies">
    <div style="border: solid black">
      <h1>user가 좋아하는 영화들</h1>
      <div v-for="card in 5" :key="card">
        <MovieCardSmall />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Profile/MovieCardSmall"
export default {
  name: "LikeMovies",
  components: {
    MovieCardSmall,
  },
}
</script>

<style></style>
