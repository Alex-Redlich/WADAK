<template>
  <div class="MovieInfo2">
    <div style="border: solid black">
      <h1>영화 정보2</h1>
      iframe 2개
      <MovieCardLarge />
    </div>
  </div>
</template>

<script>
import MovieCardLarge from "@/components/MovieDetail/MovieCardLarge"
export default {
  name: "MovieInfo2",
  components: {
    MovieCardLarge,
  },
}
</script>

<style></style>
