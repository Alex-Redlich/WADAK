<template>
  <div class="CreateComments">
    <input type="text" v-model.trim="title" @keyup.enter="createTodo" />
    <button @click="createcomments">댓글 추가</button>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "CreateComments",
  data() {
    return {
      title: null,
    }
  },
  methods: {
    createcomments() {
      console.log("ok")
      const title = this.title
      if (!title) {
        alert("댓글을 입력하세요")
        return
      }
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/v1/accounts/signup/",
        data: { title },
      })
        .then(() => {
          this.$router.push({ name: "TodoList" })
        })
        .catch((err) => console.log(err))
    },
  },
}
</script>

<style></style>
