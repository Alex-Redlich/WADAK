<template>
  <div class="SearchView">
    <h1>Search Page</h1>
    <SearchList />
  </div>
</template>

<script>
import SearchList from "@/components/Search/SearchList"
export default {
  name: "SearchView",
  components: {
    SearchList,
  },
}
</script>
<style scoped>
.SearchView {
  margin-top: 70px;
  margin-left: 200px;
}
</style>
