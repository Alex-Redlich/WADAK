<template>
  <div class="MovieCardSmall1">
    <div class="card hovering2" style="width: 300px; height: 447px" @click="GoDetail">
      <figure><img id="MovieCardSmall" :src="url" class="card-img-top" /></figure>
      <div class="movieCard__overlay2">
        <h3>자세히 보러가기</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCardSmall",
  props: {
    movie: Object,
  },
  date() {
    return {}
  },
  computed: {
    url() {
      return "https://image.tmdb.org/t/p/w500" + this.movie.poster_path
    },
  },
  methods: {
    GoDetail() {
      this.$router.push({ name: "moviedetail", params: { moviePK: this.movie.id } })
    },
  },
}
</script>

<style>
.MovieCardSmall1 {
  width: 300px;
}
#MovieCardSmall {
  box-shadow: 3px 3px 5px rgb(212, 212, 212);
}
.figure {
  width: 400px;
}
.hoverin2 figure img {
  -webkit-filter: grayscale(0) blur(0);
  filter: grayscale(0) blur(0);
  -webkit-transition: 0.3s ease-in-out;
  transition: 0.3s ease-in-out;
  -webkit-transform: scale(1);
  transform: scale(1);
}
.hovering2 figure:hover img {
  -webkit-filter: grayscale(100%) blur(2px);
  filter: grayscale(50%) blur(2px);
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
.movieCard__overlay2 {
  position: absolute;
  top: 50%;
  left: 20%;
  width: 180px;
  height: 25px;
  border-radius: 30px;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  opacity: 0;
  transition: opacity 1s ease;
  z-index: 0;
  margin: auto;
  padding: auto;
}
.movieCard__overlay2 h3 {
  color: #f5df4d;
  font-size: 20px;
  text-align: center;
}
.hovering2:hover .movieCard__overlay2 {
  opacity: 1;
}
</style>
