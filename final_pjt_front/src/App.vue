<template>
  <div id="app">
    <!-- 상단 네비게이션 바 -->
    <nav class="navbar fixed-top" id="topbar">
      <div class="container-fluid">
        <a class="navbar-brand" href="/"><img class="nav-image" src="@/assets/logo.png" alt="WADAK" /></a>
        <div class="toplist mb-4">
          <router-link to="/login">로그인</router-link> | <router-link to="/signup">회원가입</router-link> |
          <router-link to="/profile/:userId">프로필</router-link>
        </div>
      </div>
    </nav>
    <!-- 좌측 사이드 바 -->
    <nav class="sidenav">
      <div class="d-flex justify-content-center flex-column">
        <router-link to="/">영화보기</router-link>
        <router-link to="/popcorn-machine">팝콘머신</router-link>
        <router-link to="/search">찾기</router-link>
      </div>
    </nav>
    <router-view :key="$route.path" />
    <!-- 풋터 -->
    <div class="footering"></div>
    <footer class="row py-5 border-top">
      <div class="col">
        <img class="nav-image" src="@/assets/logo.png" alt="WADAK" />
        <p class="text-muted">© 2023 WADAK</p>
        <p class="text-muted">김효인 김영민</p>
      </div>

      <div class="col mb-3 d-flex justify-content-center">
        <ul class="nav" style="width: 650px">
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">자막 및 음성</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">화면 해설</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">고객 센터</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">기프트 카드</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">미디어 센터</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">투자 정보(IR)</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">입사 정보</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">이용 약관</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">개인 정보</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">법적 고지</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">쿠키 설정</a></li>
          <li class="nav-item m-3"><a href="#" class="nav-link p-0 text-muted">회사 정보</a></li>
        </ul>
      </div>
    </footer>
  </div>
</template>

<style>
#app {
  font-family: "KBO-Dia-Gothic-l";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: black;
}
@font-face {
  font-family: "KBO-Dia-Gothic-md";
  src: url("@/assets/fonts/KBO_Dia_Gothic_medium.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "KBO-Dia-Gothic-l";
  src: url("@/assets/fonts/KBO_Dia_Gothic_light.ttf") format("truetype");
  font-weight: 300;
}
@font-face {
  font-family: "KBO-Dia-Gothic-b";
  src: url("@/assets/fonts/KBO_Dia_Gothic_bold.ttf") format("truetype");
  font-weight: 700;
}
.nav-image {
  max-height: 70px;
}
#topbar {
  max-height: 70px;
  width: 1920px;
  background-color: #090e13;
}
nav a:hover {
  color: white;
}
nav a {
  font-weight: bold;
  font-size: 25px;
  color: #939597;
  font-family: "KBO-Dia-Gothic-md";
  margin-bottom: 10px;
}

nav a.router-link-exact-active {
  color: #f5df4d;
}

.sidenav {
  background-color: #090e13;
  position: fixed;
  width: 200px;
  height: 100%;
  padding-top: 50px;
}
.footering {
  background-color: black;
  height: 500px;
}
</style>
