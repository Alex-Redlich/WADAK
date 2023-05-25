<template>
  <div class="CreateComments d-flex justify-content-center">
    <h2 style="height: 40px; margin-right: 10px">남기기 :</h2>
    <input type="text" v-model.trim="content" @keyup.enter="createTodo" style="height: 40px; margin-right: 10px" />
    <button @click="createcomments" class="btn btn-dark" style="height: 40px">댓글 추가</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CreateComments",
  props: {
    reviewpk: Number,
  },
  data() {
    return {
      title: null,
    };
  },
  methods: {
    createcomments() {
      console.log("ok");
      const commentdata = {
        content: this.content,
        userID: this.$store.state.userID,
      };
      if (!this.content) {
        alert("댓글을 입력하세요");
        return;
      }
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1/communities/review/${this.reviewpk}/comment/create/`,
        data: commentdata,
      })
        .then(() => {})
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style></style>
