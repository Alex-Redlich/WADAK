<template>
  <div class="TodayMovie">
    <h1>오늘의 영화</h1>
    <MovieCardOne />
  </div>
</template>

<script>
import MovieCardOne from "@/components/Profile/MovieCardOne";
export default {
  name: "TodayMovie",
  components: {
    MovieCardOne,
  },
};
</script>

<style>
.TodayMovie {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
