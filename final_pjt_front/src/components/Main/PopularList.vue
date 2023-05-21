<template>
  <div class="PopularList">
    <!-- 제목 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="PopularListTitle">지금 인기있는 영화들!</p>
    </div>
    <!-- 카드 리스트 -->
    <div>
      <div id="PopularList" class="row justify-content-center">
        <div id="MovieCardPopular" class="col" v-for="card in 5" :key="card">
          <MovieCardSmall />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Main/MovieCardSmall";
export default {
  name: "PopularList",
  components: {
    MovieCardSmall,
  },
};
</script>

<style>
#PopularList {
  padding-left: 30px;
  padding-right: 30px;
}
#MovieCardPopular {
  display: flex;
  justify-content: center;
}
#PopularListTitle {
  font-size: 30px;
  font-weight: 700;
  margin-right: 10px;
  margin-top: 10px;
}
</style>
