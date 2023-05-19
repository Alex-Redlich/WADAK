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
