<template>
  <div class="ReviewView">
    <h1>Review Page</h1>
    <ReviewList />
  </div>
</template>

<script>
import ReviewList from "@/components/Review/ReviewList"
export default {
  name: "ReviewView",
  components: {
    ReviewList,
  },
}
</script>

<style scoped>
.ReviewView {
  margin-top: 70px;
  margin-left: 200px;
}
</style>
