<template>
  <div class="ReviewCardList">
    <div class="row">
      <div class="col d-flex justify-content-center flex-wrap">
        <div id="ReviewCardList" v-for="card in 20" :key="card">
          <ReviewCard />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewCard from "@/components/MovieDetail/ReviewCard"
export default {
  name: "ReviewCardList",
  components: {
    ReviewCard,
  },
}
</script>

<style>
.ReviewCardList {
  display: flex;
  margin-top: 50px;
}
#ReviewCardList {
  width: 300px;
  margin: 15px;
}
</style>
