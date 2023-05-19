<template>
  <div class="MovieDetailView">
    <h1>MovieDetail Page</h1>
    <MovieInfo />
    <MovieInfo2 />
    <ReviewCardList />
    <ReviewCreateForm />
    <ReviewDetail />
  </div>
</template>

<script>
import MovieInfo from "@/components/MovieDetail/MovieInfo"
import MovieInfo2 from "@/components/MovieDetail/MovieInfo2"
import ReviewCardList from "@/components/MovieDetail/ReviewCardList"
import ReviewCreateForm from "@/components/MovieDetail/ReviewCreateForm"
import ReviewDetail from "@/components/MovieDetail/ReviewDetail"

export default {
  name: "MovieDetailView",
  components: {
    MovieInfo,
    MovieInfo2,
    ReviewCardList,
    ReviewCreateForm,
    ReviewDetail,
  },
}
</script>
