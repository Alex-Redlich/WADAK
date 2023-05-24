<template>
  <div class="CommentsItem">
    <div>{{ comment.content }}</div>
  </div>
</template>

<script>
export default {
  name: "CommentsItem",
  props: {
    comment: Object,
  },
  data() {
    return {};
  },
  components: {},
};
</script>

<style></style>
