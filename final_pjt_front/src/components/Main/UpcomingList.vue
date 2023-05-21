<template>
  <div class="UpcomingList mb-4">
    <!-- 제목 -->
    <div class="d-flex justify-content-start align-items-baseline ps-3 pl-3">
      <p id="MovieCardUpcomingTitle">UPCOMING! 지금 상영중</p>
    </div>
    <!-- 카드 리스트 -->
    <div>
      <div id="UpcomingList" class="row justify-content-center">
        <div id="MovieCardUpcoming" class="col" v-for="card in 5" :key="card">
          <MovieCardSmall />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardSmall from "@/components/Main/MovieCardSmall";
export default {
  name: "UpcomingList",
  components: {
    MovieCardSmall,
  },
};
</script>

<style>
#UpcomingList {
  padding-left: 30px;
  padding-right: 30px;
}
#MovieCardUpcoming {
  display: flex;
  justify-content: center;
}
#MovieCardUpcomingTitle {
  font-size: 30px;
  font-weight: 700;
  margin-right: 10px;
  margin-top: 10px;
}
</style>
