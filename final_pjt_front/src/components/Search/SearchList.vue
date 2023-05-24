<template>
  <div class="SearchList">
    <div>
      <h1>찾고 있는 영화가 있나요?</h1>
      <form @submit.prevent="getSearch" class="Searchbar">
        <div id="Searchbar_Keyword" class="mb-3">
          <input class="form-control" id="keyword" placeholder="무엇이든 검색하세요!" v-model="keyword" />
          <button id="Searchbar" type="submit" class="btn btn-warning">Search</button>
        </div>
      </form>
    </div>

    <div id="Searchlistcard">
      <div v-if="search_movies.length" style="width: 1700px" id="searchresult">
        <MovieCardMiddle id="MovieCardSearch" v-for="movie in search_movies" :key="movie.id" :movie="movie" />
      </div>
      <div v-else style="margin: 30px">
        <h1>검색 결과가 없습니다😥</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import MovieCardMiddle from "@/components/Search/MovieCardMiddle";
export default {
  name: "SearchList",
  components: {
    MovieCardMiddle,
  },
  data() {
    return {
      search_movies: {},
      keyword: "",
    };
  },
  methods: {
    getSearch() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/movies/search/${this.keyword}/`,
      })
        .then((res) => {
          this.search_movies = res.data.results;
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
#Searchlistcard {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
#searchresult {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
#MovieCardSearch {
  display: flex;
  justify-content: center;
  width: 300px;
}
#keyword {
  width: 700px;
  height: 60px;
  font-size: 20px;
}
#Searchbar {
  height: 60px;
  width: auto;
}

#Searchbar_Keyword {
  margin: 50px;
  display: flex;
  justify-content: center;
}
</style>
