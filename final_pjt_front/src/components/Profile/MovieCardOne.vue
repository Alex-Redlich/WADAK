<template>
  <div class="MovieCardOne">
    <div class="card hovering6" style="width: 500px; border-radius: 20px" @click="GoDetail">
      <img id="MovieCardOne" :src="url" class="card-img-top" />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MovieCardOne",
  data() {
    return {
      movie: {},
    };
  },
  props: {
    userinfo: Object,
  },
  computed: {
    url() {
      return "https://image.tmdb.org/t/p/w500" + this.movie.poster_path;
    },
  },
  methods: {
    getMovieDetail() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/movies/${this.userinfo.today_movie}/`,
      })
        .then((res) => {
          this.movie = res.data;
        })
        .catch((err) => console.log(err));
    },
    GoDetail() {
      this.$router.push({ name: "moviedetail", params: { moviePK: this.movie.id, movie: this.movie } });
    },
  },
  created() {
    this.getMovieDetail();
  },
};
</script>

<style scoped>
.MovieCardOne {
  width: 500px;
  margin: 20px;
}
#MovieCardOne {
  box-shadow: 13px 13px 5px rgb(0, 0, 0);
  border: 0px;
  height: 800px;
  border-radius: 20px;
  /* border: 0; */
}
.hovering6:hover {
  -webkit-transform: scale(1.2);
  transform: scale(1.2);
}
</style>
