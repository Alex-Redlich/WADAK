<template>
  <div class="MovieCardOne">
    <div class="card" style="width: 500px">
      <img
        id="MovieCardOne"
        src="https://image.tmdb.org/t/p/w500/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg"
        class="card-img-top"
        style="border: 0px"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCardOne",
};
</script>

<style scoped>
.MovieCardOne {
  width: 500px;
  margin: 20px;
  margin-bottom: 100px;
}
#MovieCardOne {
  box-shadow: 3px 3px 5px rgb(212, 212, 212);
  /* border: 0; */
}
</style>
