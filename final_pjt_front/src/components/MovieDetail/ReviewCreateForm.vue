<template>
  <div class="ReviewCreateForms">
    <div class="createform">
      <h1>리뷰작성</h1>
      <h2>영화는 이거다</h2>
      <div id="ReviewcreateTitle" class="mb-3">
        <label for="title" class="form-label">리뷰 제목</label>
        <input class="form-control" id="title" placeholder="제목을 입력하세요" />
      </div>
      <div id="ReviewcreateVote" class="mb-3">
        <label for="vote" class="form-label">평점</label>
        <input class="form-control" id="vote" placeholder="1-10점으로 표현하세요" />
      </div>
      <div id="Reviewcreatecontents" class="mb-3">
        <label for="content" class="form-label">리뷰 내용</label>
        <textarea class="form-control" id="content" rows="20" placeholder="내용을 입력하세요"></textarea>
      </div>
      <button type="button" class="btn btn-warning btn-lg">작성하기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewCreateForm",
}
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
  height: 1000px;
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
