<template>
  <div id="app">
    <nav>
      <router-link to="/">영화보기</router-link> | <router-link to="/movies/:moviePk">moviedetail</router-link> | <router-link to="/popcorn-machine">팝콘머신</router-link> |
      <router-link to="/profile/:userId">프로필</router-link> | <router-link to="/search">찾기</router-link> | <router-link to="/:userId/inventory">인벤토리</router-link> |
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
  color: #2c3e50;
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

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  font-family: "KBO-Dia-Gothic-md";
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
