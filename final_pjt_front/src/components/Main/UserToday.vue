<template>
  <div class="UserToday">
    <!-- 유저 이름 태그 블럭 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="UserReviewlist_username">세종시 속도제한 20km</p>
      <p id="UserReviewlist_text">님의 Today Movie</p>
    </div>
    <!-- 단독 카드 -->
    <div class="d-flex justify-content-center">
      <MovieCardOneDetail />
    </div>
  </div>
</template>

<script>
import MovieCardOneDetail from "@/components/Main/MovieCardOneDetail";

export default {
  name: "UserToday",
  components: {
    MovieCardOneDetail,
  },
};
</script>

<style>
#UserReviewlist_username {
  font-size: 50px;
  font-weight: 800;
  margin-right: 10px;
}
#UserReviewlist_text {
  font-size: 25px;
  font-weight: 300;
}
</style>
