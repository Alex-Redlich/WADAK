<template>
  <div class="MovieCardSmall1">
    <div class="card" style="width: 300px">
      <img id="MovieCardSmall" src="https://image.tmdb.org/t/p/w500/sz6mTIDDQmR3DYgJudiTmoW2gR5.jpg" class="card-img-top" />
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCardSmall",
}
</script>

<style>
.MovieCardSmall1 {
  width: 300px;
}
#MovieCardSmall {
  box-shadow: 3px 3px 5px rgb(212, 212, 212);
}
</style>
