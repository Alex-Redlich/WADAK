<template>
  <div class="UserToday">
    <div style="border: solid black">
      <h1>유저의 오늘의 영화</h1>
      <MovieCardOneDetail />
    </div>
  </div>
</template>

<script>
import MovieCardOneDetail from "@/components/Main/MovieCardOneDetail"

export default {
  name: "UserToday",
  components: {
    MovieCardOneDetail,
  },
}
</script>

<style></style>
