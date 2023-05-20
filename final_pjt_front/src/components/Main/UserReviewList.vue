<template>
  <div class="UserReviewList">
    <div style="border: solid black">
      <h1>유저가 리뷰남긴 리스트</h1>
      <div v-for="card in 3" :key="card">
        <MovieCardLarge />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardLarge from "@/components/Main/MovieCardLarge";
export default {
  name: "UserReviewList",
  components: {
    MovieCardLarge,
  },
};
</script>

<style></style>
