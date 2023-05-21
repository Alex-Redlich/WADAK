<template>
  <div class="MovieCardOneDetail">
    <div class="card" style="max-width: 1200px">
      <div class="row">
        <div class="col-4">
          <img src="https://image.tmdb.org/t/p/w500/3JT1oE0JIA6CQJaZDG00y3S0kP3.jpg" class="img-fluid rounded-start" />
        </div>
        <div class="col-8 p-5">
          <div class="card-body">
            <h5 class="card-title">분노의 질주: 라이드 오어 다이</h5>
            <p class="card-text">2023-05-17</p>
            <p class="card-text">⭐ 7.1</p>
            <p class="card-text-detail">
              돔과 그의 패밀리 앞에 나타난 운명의 적 단테. 과거의 그림자는 돔의 모든 것을 파괴하기 위해 달려온다. 단테에
              의해 산산히 흩어진 패밀리들은 모두 목숨을 걸고 맞서야 하는 함정에 빠지고 마는데...
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCardOneDetail",
};
</script>

<style>
.card-body {
  text-align: start;
}
.card-title {
  color: black;
  font-size: 50px;
  margin-bottom: 20px;
}
.card-text {
  color: grey;
  font-size: 30px;
}
.card-text-detail {
  color: grey;
  font-size: 20px;
}
</style>
