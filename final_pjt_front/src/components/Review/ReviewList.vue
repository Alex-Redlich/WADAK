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
          <tr>
            <th scope="row">슈퍼마리오</th>
            <td>지금까지 이런 영화는 없었다</td>
            <td>⭐ 7</td>
            <td>[고독한 마블매니아] 알렉스킴</td>
            <td>2023-05-22</td>
            <td>123</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewList",
  components: {},
}
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
