<template>
  <div class="MovieInfo">
    <!-- <h1>영화 정보</h1> -->
    <div id="MovieInfo" class="row">
      <div class="col-4"><img id="MovieDetailimg" :src="url" /></div>
      <div id="MovieInfo2" class="col-8">
        <div class="d-flex align-items-baseline">
          <p id="MovieTitle">{{ movie.title }}</p>
          <div>
            <img v-if="isLikedBtn" id="Btn1" @click="ClickLike" src="@/assets/Like_ON.png" alt="" />
            <img v-else id="Btn1" @click="ClickLike" src="@/assets/Like_OFF.png" alt="" />
          </div>
          <div>
            <img v-if="isTodayMovieBtn" id="Btn2" @click="ClickTodayMovie" src="@/assets/TodayMovie_ON.png" alt="" />
            <img v-else id="Btn2" @click="ClickTodayMovie" src="@/assets/TodayMovie_OFF.png" alt="" />
          </div>
        </div>

        <p id="MovieTagline">{{ movie.tagline }}</p>
        <p id="MovieGenre">{{ moviegenre }}</p>
        <div id="MovieDetail" class="d-flex">
          <p id="MovieVote">⭐ {{ movie.vote_average }}</p>
          <p id="Movieruntime">{{ movie.runtime }}분</p>
          <p id="ReleaseDate">{{ movie.release_date }}</p>
        </div>
        <p id="MovieOverview">
          {{ movie.overview }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieInfo",
  data() {
    return {
      isLikedBtn: false,
      isTodayMovieBtn: false,
    }
  },
  props: {
    movie: Object,
  },
  computed: {
    url() {
      return "https://image.tmdb.org/t/p/w500" + this.movie.poster_path
    },
    moviegenre() {
      let result = this.movie.genres["0"].name
      for (let i = 1; i < this.movie.genres.length; i++) {
        result += "·" + this.movie.genres[i].name
      }
      return result
    },
  },
  methods: {
    ClickLike() {
      this.isLikedBtn = !this.isLikedBtn
    },
    ClickTodayMovie() {
      this.isTodayMovieBtn = !this.isTodayMovieBtn
    },
  },
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
#MovieVote {
  margin-right: 30px;
}
#Movieruntime {
  margin-right: 30px;
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
#Btn1 {
  width: 50px;
  height: 50px;
  margin-left: 10px;
}
#Btn2 {
  width: 50px;
  height: 50px;
  margin-left: 10px;
}
</style>
