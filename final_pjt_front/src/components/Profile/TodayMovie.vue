<template>
  <div class="TodayMovie">
    <MovieCardOne :userinfo="userinfo" />
    <h1 id="TodayMovieTitle">Today Movie's📢</h1>
  </div>
</template>

<script>
import MovieCardOne from "@/components/Profile/MovieCardOne";
export default {
  name: "TodayMovie",
  data() {
    return {};
  },
  components: {
    MovieCardOne,
  },
  props: {
    userinfo: Object,
  },
};
</script>

<style>
.TodayMovie {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 50px;
}
#TodayMovieTitle {
  margin-top: 20px;
  font-weight: 1000;
}
</style>
