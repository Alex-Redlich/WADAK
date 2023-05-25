<template>
  <div class="MovieInfo2">
    <div class="row">
      <div id="iframe" class="col-7">
        <h1>관련 영상 보러가기</h1>
        <iframe :src="videoURL" frameborder="0"></iframe>
      </div>
      <div id="similar" class="col-5">
        <h1>이런 영화는 어때요?</h1>
        <div class="d-flex justify-content-center" style="margin: 20px">
          <MovieCardLarge :similar-movie="similarmovie" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const API_URL = "https://www.googleapis.com/youtube/v3/search";
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
// const API_KEY = "AIzaSyDIjfZ49Ye10W7qN1ilixlTCzKILYagQvI";

import MovieCardLarge from "@/components/MovieDetail/MovieCardLarge";
import axios from "axios";

export default {
  name: "MovieInfo2",
  components: {
    MovieCardLarge,
  },
  props: {
    moviepk: String,
    movie: Object,
  },
  data() {
    return {
      similarmovie: {},
      videoURL: null,
    };
  },
  methods: {
    getSmilar() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/movies/${this.moviepk}/similar`,
      })
        .then((res) => {
          this.similarmovie = res.data;
        })
        .catch(() => {});
    },
    getVideoURL() {
      axios
        .get(API_URL, {
          params: {
            key: API_KEY,
            type: "video",
            part: "snippet",
            q: `${this.movie.title}`,
          },
        })
        .then((response) => {
          this.videoId = response.data.items[0].id.videoId;
          this.videoURL = `https://youtube.com/embed/${this.videoId}`;
        });
    },
  },
  created() {
    this.getSmilar();
    this.getVideoURL();
  },
};
</script>

<style>
.MovieInfo2 {
  margin-top: 50px;
}
#iframe {
  margin-bottom: 100px;
}
#similar {
  border-left: solid 1px white;
  display: flex;
  flex-direction: column;
}
iframe {
  width: 950px;
  height: 550px;
  margin: 20px;
}
</style>
