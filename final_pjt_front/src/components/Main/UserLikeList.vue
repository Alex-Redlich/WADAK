<template>
  <div class="UserLikeList">
    <!-- 유저 이름 태그 블럭 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="UserLikeList_username">스펙타클한남자</p>
      <p id="UserLikeList_text">님이 좋아하는 영화들</p>
    </div>
    <!-- 카드 리스트 -->
    <div>
      <div class="row justify-content-center">
        <div id="MovieCardUserList" class="col" v-for="card in 3" :key="card">
          <MovieCardLarge />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardLarge from "@/components/Main/MovieCardLarge";
export default {
  name: "UserLikeList",
  components: {
    MovieCardLarge,
  },
};
</script>

<style>
#MovieCardUserList {
  display: flex;
  justify-content: center;
}
#UserLikeList_username {
  font-size: 50px;
  font-weight: 800;
  margin-right: 10px;
}
#UserLikeList_text {
  font-size: 25px;
  font-weight: 300;
}
</style>
