<template>
  <div class="ReviewCreateForms">
    <div class="createform">
      <h1>리뷰작성</h1>
      <h6>지금 작성하는 리뷰의 영화는</h6>
      <h2>{{ movieTITLE }}</h2>
      <form @submit.prevent="CreateReview" class="createreview">
        <div id="ReviewcreateTitle" class="mb-3">
          <label for="title" class="form-label">리뷰 제목</label>
          <input class="form-control" id="title" placeholder="제목을 입력하세요" v-model="title" />
        </div>
        <div id="ReviewcreateVote" class="mb-3">
          <label for="vote" class="form-label">평점</label>
          <input class="form-control" id="vote" placeholder="1-10점으로 표현하세요" v-model="rating" />
        </div>
        <div id="Reviewcreatecontents" class="mb-3">
          <label for="content" class="form-label">리뷰 내용</label>
          <textarea
            class="form-control"
            id="content"
            rows="20"
            placeholder="내용을 입력하세요"
            v-model="content"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-warning btn-lg">작성하기</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ReviewCreateForm",
  data() {
    return {
      movieTITLE: this.$route.params.movieTITLE,
      moviePK: this.$route.params.moviePK,

      title: "",
      rating: "",
      content: "",
    };
  },
  methods: {
    CreateReview() {
      const data = {
        userID: this.$store.state.userID,
        title: this.title,
        rating: this.rating,
        content: this.content,
      };
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1/communities/movie/${this.moviePK}/review/create/`,
        data: data,
      })
        .then(() => {})
        .catch((err) => console.log(err));
      this.$router.push({ name: "moviedetail", params: { moviePK: this.moviePK } });
    },
  },
};
</script>

<style>
.ReviewCreateForms {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
  display: flex;
  justify-content: center;
}
.createform {
  width: 1000px;
  margin: 100px;
}
#ReviewcreateTitle {
  text-align: start;
}
#ReviewcreateVote {
  text-align: start;
}
#Reviewcreatecontents {
  text-align: start;
}
</style>
