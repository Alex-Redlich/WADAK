<template>
  <div class="CommentsList">
    <CreateComments />
    <!-- <Comment v-for="comment in comments " -->
  </div>
</template>

<script>

import CreateComments from "@/components/Comments/CreateComments"
export default {
  name: "CommentsList",
  data() {
    return {
      comments : []
    }
  },
  components: {
    CreateComments,
  },
}
</script>

<style></style>
