<template>
  <div class="MovieDetailView">
    <MovieInfo />
    <div id="SelectMenu" class="d-flex justify-content-center">
      <div id="Select1" @click="SelectTurn1" :class="{ isSelected: selectcolor1, isnotSelected: selectcolor2 }">팝콘머신 보기</div>
      <div id="blank">|</div>
      <div id="Select2" @click="SelectTurn2" :class="{ isSelected: selectcolor2, isnotSelected: selectcolor1 }">영화 상세정보</div>
    </div>
    <div v-if="SelectMenu1">
      <ReviewCardList />
      <div class="ReviewCreateForm">리 뷰 작 성</div>
    </div>
    <div v-else>
      <MovieInfo2 />
    </div>
  </div>
</template>

<script>
import MovieInfo from "@/components/MovieDetail/MovieInfo"
import MovieInfo2 from "@/components/MovieDetail/MovieInfo2"
import ReviewCardList from "@/components/MovieDetail/ReviewCardList"

export default {
  name: "MovieDetailView",
  components: {
    MovieInfo,
    MovieInfo2,
    ReviewCardList,
  },
  data() {
    return {
      selectcolor1: true,
      selectcolor2: false,
      SelectMenu1: true,
    }
  },
  methods: {
    SelectTurn1() {
      this.SelectMenu1 = true
      this.selectcolor1 = !this.selectcolor1
      this.selectcolor2 = !this.selectcolor2
    },
    SelectTurn2() {
      this.SelectMenu1 = false
      this.selectcolor1 = !this.selectcolor1
      this.selectcolor2 = !this.selectcolor2
    },
  },
}
</script>
<style scoped>
.MovieDetailView {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
}
#SelectMenu {
  margin-top: 30px;
  font-size: 30px;
}
#blank {
  margin-left: 30px;
  margin-right: 30px;
}
.isSelected {
  color: #f5df4d;
}
.isnotSelected {
  color: white;
}
.ReviewCreateForm {
  position: fixed;
  width: 1500px;
  bottom: 50px;
  left: 300px;
  background: #f5df4d;
  opacity: 0.9;
  font-size: 40px;
  border-radius: 30px;
}
</style>
