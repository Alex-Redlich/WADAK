<template>
  <div class="MainView">
    <h1>Main Page</h1>
    <RankerList />
    <UserLikeList />
    <PopularList />
    <UserToday />
    <UpcomingList />
    <UserReviewList />
    <div>풋터</div>
  </div>
</template>

<script>
import RankerList from "@/components/Main/RankerList"
import UserLikeList from "@/components/Main/UserLikeList"
import PopularList from "@/components/Main/PopularList"
import UserToday from "@/components/Main/UserToday"
import UpcomingList from "@/components/Main/UpcomingList"
import UserReviewList from "@/components/Main/UserReviewList"

export default {
  name: "MainView",
  components: {
    RankerList,
    UserLikeList,
    PopularList,
    UserToday,
    UpcomingList,
    UserReviewList,
  },
}
</script>
<style scoped>
.MainView {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
  border: solid white;
}
</style>
