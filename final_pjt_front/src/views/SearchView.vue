<template>
  <div class="SearchView">
    <SearchList />
  </div>
</template>

<script>
import SearchList from "@/components/Search/SearchList";
export default {
  name: "SearchView",
  components: {
    SearchList,
  },
};
</script>
<style scoped>
.SearchView {
  margin-top: 70px;
  margin-left: 200px;
  padding: 50px;
  background-color: black;
  height: 1100px;
}
</style>
