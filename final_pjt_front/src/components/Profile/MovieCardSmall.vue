<template>
  <div class="MovieCardSmall">
    <div class="card hovering7" style="width: 200px" @click="GoDetail">
      <img
        id="MovieCardSmall2"
        :src="url"
        class="card-img-top"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCardSmall",
  props: {
    movie : Object
  },
  computed: {
    url() {
      return "https://image.tmdb.org/t/p/w500" + this.movie.poster_path
    },
  },
  methods: {
    GoDetail() {
      this.$router.push({ name: "moviedetail", params: { moviePK: this.movie.id, movie:this.movie} })
    },
  }
}
</script>

<style>
.MovieCardSmall {
  width: 220px;
  margin: 35px;
}
#MovieCardSmall2 {
  box-shadow: 10px 10px 5px rgb(134, 134, 134);
  border-radius: 10px;
}
.hovering7:hover {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
