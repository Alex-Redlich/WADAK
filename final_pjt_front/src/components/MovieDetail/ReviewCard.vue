<template>
  <div class="ReviewCard hovering3">
    <div class="card" @click="ReviewDetail">
      <div class="card-body">
        <h5 class="card-title text-center">{{ review.title }}</h5>
        <h5 class="card-subtitle mb-2 text-muted">{{ review }}</h5>
        <h6 class="card-subtitle mb-2 text-muted">⭐{{ review.rating }}</h6>
        <p class="card-text">
          {{ review.content }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewCard",
  data() {
    return {
      reviewID: this.review.id,
      reviews: this.review,
    }
  },
  methods: {
    ReviewDetail() {
      this.$router.push({ name: "reviewdetail", params: { reviewID: this.reviewID, reviews: this.review } })
    },
  },
  props: {
    review: Object,
  },
}
</script>

<style scoped>
.ReviewCard {
  width: 300px;
}
.card-body {
  text-align: center;
}
.card-text {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.hovering3:hover {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
