<template>
  <div class="ReviewList">
    <div class="Reviewlistbox">
      <table id="ReviewTable" class="table">
        <thead>
          <tr>
            <th scope="col-2">영화이름</th>
            <th scope="col-3">제목</th>
            <th scope="col-1">평점</th>
            <th scope="col-2">작성자</th>
            <th scope="col-1">작성시간</th>
            <th scope="col-1">추천 수</th>
          </tr>
        </thead>
        <tbody>
          <!-- for문돌기 -->
          <tr v-for="review in reviews" :key="review.id">
            <th @click="GoDetail(review.id, review.movie, review)" scope="row">{{ review.movie.title }}</th>
            <td @click="GoDetail(review.id, review.movie, review)">{{ review.title }}</td>
            <td @click="GoDetail(review.id, review.movie, review)">⭐ {{ review.rating }}</td>
            <td @click="GoDetail(review.id, review.movie, review)">
              [{{ review.user.chingho }}] {{ review.user.nickname }}
            </td>
            <td @click="GoDetail(review.id, review.movie, review)">{{ review.created_at }}</td>
            <td @click="GoDetail(review.id, review.movie, review)">{{ review.like_users_count }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ReviewList",
  data() {
    return {
      reviews: [],
    };
  },
  methods: {
    getAllList() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/communities/allreviews/",
      })
        .then((res) => {
          console.log("요청성공!");
          this.reviews = res.data;
        })
        .catch((err) => console.log(err));
    },
    GoDetail(id, movie, review) {
      this.$router.push({ name: "reviewdetail", params: { reviewID: id, moviePK: movie, review_detail: review } });
    },
  },
  created() {
    this.getAllList();
  },
};
</script>

<style>
.ReviewList {
  display: flex;
  justify-content: center;
}
.Reviewlistbox {
  width: 1500px;
}
#ReviewTable {
  color: white;
}
</style>
