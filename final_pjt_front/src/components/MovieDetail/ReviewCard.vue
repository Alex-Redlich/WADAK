<template>
  <div class="ReviewCard">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title text-center">리뷰 타이틀</h5>
        <h5 class="card-subtitle mb-2 text-muted">작성자</h5>
        <h6 class="card-subtitle mb-2 text-muted">평점</h6>
        <p class="card-text">
          아 이영화 개 맛집 존맛탱 개맛있구요아 이영화 개 맛집 존맛탱 개맛있구요아 이영화 개 맛집 존맛탱 개맛있구요아 이영화 개 맛집 존맛탱 개맛있구요아 이영화 개 맛집 존맛탱 개맛있구요아 이영화 개
          맛집 존맛탱 개맛있구요
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewCard",
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
</style>
