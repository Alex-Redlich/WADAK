<template>
  <div class="PopularList">
    <div style="border: solid black">
      <h1>인기 순위 리스트</h1>
      <div v-for="card in 5" :key="card">
        <MovieCardSmall />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Main/MovieCardSmall"
export default {
  name: "PopularList",
  components: {
    MovieCardSmall,
  },
}
</script>

<style></style>
