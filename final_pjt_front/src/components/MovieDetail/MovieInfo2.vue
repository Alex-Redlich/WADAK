<template>
  <div class="MovieInfo2">
    <div class="row">
      <div id="iframe" class="col-6">
        <h1>관련 영상 보러가기</h1>
        <iframe src="https://www.youtube.com/embed/9mLpChKFV80">관련영상1</iframe>
        <iframe src="https://www.youtube.com/embed/4jhz2NU-24Q">관련영상2</iframe>
      </div>
      <div id="similar" class="col-6">
        <h1>이런 영화는 어때요?</h1>
        <div class="d-flex justify-content-center" style="margin: 20px">
          <MovieCardLarge :similarmovie="similarmovie" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardLarge from "@/components/MovieDetail/MovieCardLarge"
import axios from "axios"

export default {
  name: "MovieInfo2",
  components: {
    MovieCardLarge,
  },
  props: {
    movieId: String,
  },
  data() {
    return {
      similarmovie: [],
    }
  },
  methods: {
    getSmilar() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/movies/${this.movieId}/similar`,
      })
        .then((res) => {
          console.log(res.data)
          this.similarmovie = res.data
        })
        .catch((err) => console.log(err))
    },
  },
}
</script>

<style>
.MovieInfo2 {
  margin-top: 50px;
}
#iframe {
  border-right: solid 1px white;
  margin-bottom: 100px;
}
#similar {
  display: flex;
  flex-direction: column;
}
iframe {
  width: 600px;
  height: 350px;
  margin: 20px;
}
</style>
