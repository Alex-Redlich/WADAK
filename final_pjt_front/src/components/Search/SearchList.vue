<template>
  <div class="SearchList">
    <div style="border: solid black">
      <h1>검색 기능</h1>
      <div v-for="card in 3" :key="card">
        <MovieCardMiddle />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardMiddle from "@/components/Search/MovieCardMiddle"
export default {
  name: "SearchList",
  components: {
    MovieCardMiddle,
  },
}
</script>

<style></style>
