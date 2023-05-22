<template>
  <div class="ReviewView">
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
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
