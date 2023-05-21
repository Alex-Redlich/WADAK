<template>
  <div class="UserReviewList mb-4">
    <!-- 유저 이름 태그 블럭 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="UserReviewlist_username">재밌으면 짖는 개</p>
      <p id="UserReviewlist_text">님의 최근 리뷰 모음.zip</p>
    </div>
    <!-- 카드 리스트 -->
    <div>
      <div class="row justify-content-center">
        <div id="MovieCardUserReview" class="col" v-for="card in 3" :key="card">
          <MovieCardLarge />
        </div>
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

<style>
#MovieCardUserReview {
  display: flex;
  justify-content: center;
}
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
