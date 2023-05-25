<template>
  <div class="MovieCardOneDetail1">
    <div id="MovieCardOneDetail1" class="card hovering5" style="max-width: 1300px" @click="GoDetail">
      <div class="row">
        <div class="col-4">
          <img :src="url" class="img-fluid rounded-start" />
        </div>
        <div class="col-8 p-5">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.release_date }}</p>
            <p class="card-text">⭐ {{ Math.round(movie.vote_average) }}</p>
            <p class="card-text-detail">
              {{ movie.overview }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCardOneDetail",
  props: {
    movie: Object,
  },
  date() {
    return {};
  },
  computed: {
    url() {
      return "https://image.tmdb.org/t/p/w500" + this.movie.poster_path;
    },
  },
  methods: {
    GoDetail() {
      this.$router.push({ name: "moviedetail", params: { moviePK: this.movie.id } });
    },
  },
};
</script>

<style>
.card-body {
  text-align: start;
}
.card-title {
  color: black;
  font-size: 50px;
  margin-bottom: 20px;
}
.card-text {
  color: grey;
  font-size: 30px;
}
.card-text-detail {
  color: grey;
  font-size: 20px;
}

#MovieCardOneDetail1 {
  box-shadow: 3px 3px 5px rgb(212, 212, 212);
}
.hovering5:hover {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
