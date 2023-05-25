<template>
  <div class="RankerList mb-4">
    <!-- <h1>랭커리스트</h1> -->
    <!-- 백그라운드 비디오 -->
    <div class="mainVideo">
      <video muted autoplay loop>
        <source src="@/assets/intro2.mp4" type="video/mp4;" />
      </video>
    </div>
    <!-- 랭커 표시-->
    <div class="RankerSection">
      <div data-aos="fade-right" data-aos-duration="1000" data-aos-delay="500">
        <p class="m-0" style="padding-left: 30px">[{{ userInfo.chingho }}]</p>
        <div class="d-flex align-items-baseline">
          <p style="font-size: 7rem; text-shadow: 5px 5px 15px black; font-weight: 1000" @click="GoProfile">
            {{ userInfo.ranker_nickname }}
          </p>
          <p style="font-size: 2rem">의 Ranker Pick</p>
        </div>
      </div>
    </div>
    <!-- 영화설명 란 -->
    <div class="mainSection">
      <div data-aos="flip-up" data-aos-duration="2000" data-aos-delay="1000">
        <p class="avatarTitle" style="line-height: 110%; margin-left: -7px; font-weight: 700">
          {{ ranker_movies.title }}
        </p>

        <div class="avatarHead">
          <button type="button" class="btn btn-warning btn-lg" style="font-weight: 700" @click="GoDetail">
            자세히 보러가기
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RankerList",
  data() {
    return {
      ranker_movies: {},
      userInfo: {},
    };
  },
  methods: {
    GoProfile() {
      console.log(this.userInfo.id);
      this.$router.push({ name: "profile", params: { userID: this.userInfo.id } });
    },
    GoDetail() {
      this.$router.push({ name: "moviedetail", params: { moviePK: this.ranker_movies.id } });
    },
    getRanker() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/movies/ranker/",
      })
        .then((res) => {
          this.ranker_movies = res.data.movies;
          this.userInfo = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getRanker();
  },
  mounted() {
    this.getRanker();
  },
};
</script>

<style>
video {
  width: 105%;
  height: 100%;
}
.mainVideo {
  right: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  margin: 0px;
  object-fit: fill;
  z-index: 0;
}
.RankerSection {
  color: white;
  position: absolute;
  top: 15%;
  left: 13%;
  font-family: Staatliches;
  text-align: left;
  font-size: 3rem;
  z-index: 3;
  margin: 0px;
}
.mainSection {
  color: white;
  text-align: center;
  position: absolute;
  top: 40%;
  left: 13%;
  font-family: Staatliches;
  text-align: left;
  font-size: 4rem;
  z-index: 3;
}
.avatarHead {
  font-family: Staatliches;
  font-size: 1rem;
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: baseline;
  z-index: 3;
}
</style>
