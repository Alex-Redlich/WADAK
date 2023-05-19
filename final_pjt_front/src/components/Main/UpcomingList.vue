<template>
  <div class="UpcomingList">
    <div style="border: solid black">
      <h1>지금 상영중</h1>
      <div v-for="card in 5" :key="card">
        <MovieCardSmall />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Main/MovieCardSmall"
export default {
  name: "UpcomingList",
  components: {
    MovieCardSmall,
  },
}
</script>

<style></style>
