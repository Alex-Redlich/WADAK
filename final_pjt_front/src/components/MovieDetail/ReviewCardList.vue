<template>
  <div class="ReviewCardList">
    <div style="border: solid black">
      <h1>리뷰 카드 리스트</h1>
      <div v-for="card in 3" :key="card">
        <ReviewCard />
      </div>
    </div>
  </div>
</template>

<script>
import ReviewCard from "@/components/MovieDetail/ReviewCard"
export default {
  name: "ReviewCardList",
  components: {
    ReviewCard,
  },
}
</script>

<style></style>
