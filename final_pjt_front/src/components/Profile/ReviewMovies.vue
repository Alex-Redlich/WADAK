<template>
  <div class="ReviewMovies">
    <div style="border: solid black">
      <h1>user가 리뷰를 남긴 영화들</h1>
      <div v-for="card in 5" :key="card">
        <MovieCardSmall />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Profile/MovieCardSmall"
export default {
  name: "ReviewMovies",
  components: {
    MovieCardSmall,
  },
}
</script>

<style></style>
