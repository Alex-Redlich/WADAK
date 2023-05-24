<template>
  <div class="ReviewDetail1">
    <div id="reviewtitle">
      <h3>리뷰 제목</h3>
      <div class="reviewtitle">{{ review_detail.title }}</div>
    </div>
    <div id="reviewuser">
      <h3>작성 유저</h3>
      <div class="reviewuser">{{ review_detail.user.nickname }}</div>
      <button type="button" class="btn btn-primary" @click="GoProfile">프로필 가기!</button>
    </div>
    <div id="reviewvote">
      <h3>평점</h3>
      <div class="reviewvote">⭐ {{ review_detail.rating }}</div>
    </div>
    <div id="reviewcontents">
      <h3>리뷰 내용</h3>
      <div class="reviewcontents">
        {{ review_detail.content }}
      </div>
    </div>
    <div id="deleteReview"><button type="button" class="btn btn-danger" @click="DeleteReview">삭제</button></div>
    <div id="LikeReview">
      <button v-if="!isLiked" type="button" class="btn btn-danger" @click="LikeReview">좋아요</button>
      <button v-else type="button" class="btn btn-light" @click="LikeReview">좋아요취소</button>
      <div>{{ review_detail.like_users_count }}</div>
    </div>
    <div class="review_comments">
      <CommentsList />
    </div>
    <button id="Callback" type="button" class="btn btn-warning" @click="Callback">다른 리뷰 보러 가기</button>
  </div>
</template>

<script>
import CommentsList from "@/components/Comments/CommentsList";
import axios from "axios";

export default {
  name: "ReviewDetail",
  components: {
    CommentsList,
  },
  data() {
    return {
      review_detail: this.$route.params.review_detail,
      reviewID: this.$route.params.reviewID,
      moviePK: this.$route.params.moviePK,
      isLiked: false,
      review_user_ID: this.$route.params.review_detail.user.id,
    };
  },
  methods: {
    GoProfile() {
      console.log(this.review_user_ID);
      this.$router.push({ name: "profile", params: { userID: this.review_user_ID } });
    },
    Callback() {
      this.$router.push({ name: "moviedetail", params: { moviePK: this.moviePK } });
    },
    DeleteReview() {
      axios({
        method: "DELETE",
        url: `http://127.0.0.1:8000/api/v1/communities/movie/${this.moviePK}/review/${this.reviewID}/delete/`,
      })
        .then(() => {
          console.log("리뷰 삭제 성공!");
          this.$router.push({ name: "moviedetail", params: { moviePK: this.moviePK } });
        })
        .catch((err) => console.log(err));
    },
    LikeReview() {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1/communities/movie/${this.moviePK}/review/${this.reviewID}/like/`,
        data: {
          userID: this.$store.state.userID,
        },
      })
        .then(() => {
          console.log("좋아요!");
          this.$router.push({ name: "moviedetail", params: { moviePK: this.moviePK } });
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style>
.ReviewDetail1 {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;

  padding: 30px;
}
#reviewtitle {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-bottom: 20px;
}
.reviewtitle {
  color: black;
  background-color: white;
  width: 1000px;
  font-size: 30px;
  padding: 10px;
  margin-bottom: 20px;
}
#reviewuser {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-bottom: 20px;
}
.reviewuser {
  color: black;
  background-color: white;
  width: 1000px;
  font-size: 30px;
  padding: 10px;
  margin-bottom: 20px;
}
#reviewvote {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-bottom: 20px;
}
.reviewvote {
  color: black;
  background-color: white;
  width: 1000px;
  font-size: 30px;
  padding: 10px;
  margin-bottom: 20px;
}
#reviewcontents {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-bottom: 20px;
}
.reviewcontents {
  color: black;
  background-color: white;
  width: 1000px;
  font-size: 30px;
  padding: 10px;
  margin-bottom: 20px;
}
.like {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-content: center;
  align-items: center;
}
#Callback {
  margin-top: 30px;
  font-size: 30px;
  width: 1000px;
}
#deleteReview {
  margin-bottom: 30px;
}
#LikeReview {
  margin-bottom: 30px;
}
</style>
