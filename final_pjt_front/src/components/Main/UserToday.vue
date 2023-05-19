<template>
  <div class="UserToday">
    <div style="border: solid black">
      <h1>유저의 오늘의 영화</h1>
      <MovieCardOne />
    </div>
  </div>
</template>

<script>
import MovieCardOne from "@/components/Main/MovieCardOne"

export default {
  name: "UserToday",
  components: {
    MovieCardOne,
  },
}
</script>

<style></style>
