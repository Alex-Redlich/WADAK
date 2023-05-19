<template>
  <div class="UserLikeList">
    <div style="border: solid black">
      <h1>유저가 좋아요한 리스트</h1>
      <div v-for="card in 3" :key="card">
        <MovieCardLarge />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardLarge from "@/components/Main/MovieCardLarge"
export default {
  name: "UserLikeList",
  components: {
    MovieCardLarge,
  },
}
</script>

<style></style>
