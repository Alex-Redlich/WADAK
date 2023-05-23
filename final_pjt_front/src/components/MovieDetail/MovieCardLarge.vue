<template>
  <div class="MovieCardLarge1">
    <div class="card hovering" style="width: 500px; height: 747px" @click="GoDetail">
      <figure><img id="MovieCardLarge1" :src="url" class="card-img-top" style="border: 0px" /></figure>
      <div class="movieCard__overlay">
        <h3>자세히 보러가기</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCardLarge",
  data() {
    return {
      poster_path: "/3JT1oE0JIA6CQJaZDG00y3S0kP3.jpg",
    }
  },
  computed: {
    url() {
      return "https://image.tmdb.org/t/p/w500" + this.similarMovie.poster_path
    },
  },
  props: {
    similarMovie: Object,
  },
  methods: {
    GoDetail() {
      this.$router.push({ name: "moviedetail", params: { moviePK: this.similarMovie.id } })
    },
  },
}
</script>

<style>
.MovieCardLarge1 {
  width: 500px;
  display: flex;
}
#MovieCardLarge1 {
  box-shadow: 3px 3px 5px rgb(212, 212, 212);
  /* border: 0; */
}
.figure {
  width: 400px;
}
.hovering figure img {
  -webkit-filter: grayscale(0) blur(0);
  filter: grayscale(0) blur(0);
  -webkit-transition: 0.3s ease-in-out;
  transition: 0.3s ease-in-out;
  -webkit-transform: scale(1);
  transform: scale(1);
}
.hovering figure:hover img {
  -webkit-filter: grayscale(100%) blur(2px);
  filter: grayscale(50%) blur(2px);
  -webkit-transform: scale(1.05);
  transform: scale(1.05);
}
.movieCard__overlay {
  position: absolute;
  top: 50%;
  left: 30%;
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
.movieCard__overlay h3 {
  color: #f5df4d;
  font-size: 20px;
  text-align: center;
}
.hovering:hover .movieCard__overlay {
  opacity: 1;
}
</style>
