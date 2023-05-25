<template>
  <div class="CommentsList">
    <CreateComments :reviewpk="this.reviewpk" />
    <CommentsItem v-for="comment in comments" :key="comment.id" :comment="comment" />
  </div>
</template>

<script>
import CreateComments from "@/components/Comments/CreateComments";
import CommentsItem from "@/components/Comments/CommentsItem";
import axios from "axios";
export default {
  name: "CommentsList",
  props: {
    reviewpk: Number,
  },
  data() {
    return {
      comments: {},
    };
  },
  components: {
    CreateComments,
    CommentsItem,
  },
  methods: {
    getComments() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/communities/review/${this.reviewpk}/comment/`,
      })
        .then((res) => {
          this.comments = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getComments();
  },
  mounted() {
    this.getComments();
  },
};
</script>

<style></style>
