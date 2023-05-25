<template>
  <div class="ReviewCard hovering3">
    <div class="card" @click="ReviewDetail">
      <div class="card-body">
        <h5 class="card-title text-center">{{ review.title }}</h5>
        <h5 class="card-subtitle mb-2 text-muted">{{ review.user.nickname }}</h5>
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
      review_detail: this.review,
      moviePK: this.$route.params.moviePK,
    };
  },
  methods: {
    ReviewDetail() {
      this.$router.push({
        name: "reviewdetail",
        params: { reviewID: this.reviewID, review_detail: this.review, moviePK: this.moviePK },
      });
    },
  },
  props: {
    review: Object,
  },
};
</script>

<style scoped>
.ReviewCard {
  width: 300px;
}
.card-body {
  text-align: center;
  height: 400px;
}
.card-text {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.hovering3:hover {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
