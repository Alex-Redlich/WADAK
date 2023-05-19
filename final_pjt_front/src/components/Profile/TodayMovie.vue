<template>
  <div class="TodayMovie">
    <div style="border: solid black">
      <h1>오늘의 영화</h1>
      <MovieCardOne />
    </div>
  </div>
</template>

<script>
import MovieCardOne from "@/components/Profile/MovieCardOne"
export default {
  name: "TodayMovie",
  components: {
    MovieCardOne,
  },
}
</script>

<style></style>
