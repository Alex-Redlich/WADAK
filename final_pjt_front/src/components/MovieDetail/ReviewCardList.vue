<template>
  <div class="ReviewCardList">
    <div class="row">
      <div class="col d-flex justify-content-center flex-wrap">
        <ReviewCard id="ReviewCardList" v-for="review in reviews" :key="review.id" :review="review" />
      </div>
    </div>
  </div>
</template>

<script>
import ReviewCard from "@/components/MovieDetail/ReviewCard"
import axios from "axios"

export default {
  name: "ReviewCardList",
  components: {
    ReviewCard,
  },
  data() {
    return {
      moviePK: this.$route.params.moviePK,
      reviews: {},
    }
  },
  methods: {
    getReviewList() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/communities/movie/${this.moviePK}/review/`,
      })
        .then((res) => {
          // console.log(res.data)
          this.reviews = res.data
        })
        .catch((err) => console.log(err))
    },
  },
  created() {
    this.getReviewList()
  },
  mounted() {
    this.getReviewList()
  }
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
