<template>
  <div class="MovieInfo">
    <!-- <h1>영화 정보</h1> -->
    <div id="MovieInfo" class="row">
      <div class="col-4"><img id="MovieDetailimg" src="https://image.tmdb.org/t/p/w500/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg" /></div>
      <div id="MovieInfo2" class="col-8">
        <p id="MovieTitle">슈퍼 마리오 브라더스</p>
        <p id="MovieTagline">동생을 구하기 위해! 세상을 지키기 위해! '슈퍼 마리오'로 레벨업하기 위한 '마리오'의 스펙터클한 스테이지가 시작된다</p>
        <p id="MovieGenre">애니메이션·가족·모험·판타지·코미디</p>
        <div id="MovieDetail" class="d-flex">
          <p id="MovieVote">⭐ 7.7</p>
          <p id="Movieruntime">92 분</p>
        </div>
        <p id="MovieOverview">
          따단-딴-따단-딴 ♫ 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로
          빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는
          다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은
          예기치 못한 위험에 빠지게 되는데...!
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieInfo",
}
</script>

<style>
#MovieInfo {
  padding: 50px;
  border-bottom: solid #939597;
}
#MovieInfo2 {
  padding-right: 250px;
}
#MovieDetailimg {
  width: 400px;
}
#MovieTitle {
  text-align: start;
  font-size: 80px;
  font-weight: 1000;
}
#MovieTagline {
  text-align: start;
  font-size: 20px;
  color: #b4b6b8;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
#MovieGenre {
  text-align: start;
  font-size: 30px;
}
#MovieDetail {
  font-size: 30px;
}
#MovieOverview {
  text-align: start;
  font-size: 25px;
  display: -webkit-box;
  -webkit-line-clamp: 8;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
