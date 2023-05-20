<template>
  <div id="app">
    <!-- 상단 네비게이션 바 -->
    <nav class="navbar fixed-top" id="topbar">
      <div class="container-fluid">
        <a class="navbar-brand" href="#"><img class="nav-image" src="@/assets/logo.png" alt="WADAK" /></a>
        <div class="toplist">
          <router-link to="/:userId/inventory">로그아웃</router-link> |
          <router-link to="/:userId/inventory">인벤토리</router-link> |
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
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: "KBO-Dia-Gothic-l";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
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
</style>
