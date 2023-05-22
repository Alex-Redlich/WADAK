<template>
  <div class="MovieCardLarge">
    <div class="card" style="width: 500px">
      <img
        id="MovieCardLarge"
        src="https://image.tmdb.org/t/p/w500/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg"
        class="card-img-top"
        style="border: 0px"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCardLarge",
};
</script>

<style>
.MovieCardLarge {
  width: 500px;
}
#MovieCardLarge {
  box-shadow: 3px 3px 5px rgb(212, 212, 212);
  /* border: 0; */
}
</style>
