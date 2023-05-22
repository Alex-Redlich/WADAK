<template>
  <div class="ReviewDetail1">
    <div id="reviewtitle">
      <h3>리뷰 제목</h3>
      <div class="reviewtitle">이영화맛나다!</div>
    </div>
    <div id="reviewvote">
      <h3>평점</h3>
      <div class="reviewvote">⭐ 10</div>
    </div>
    <div id="reviewcontents">
      <h3>리뷰 내용</h3>
      <div class="reviewcontents">
        영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영
        ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ영화 너무 재밋어영 ㅋ
      </div>
    </div>
    <div>
      <div class="buttons">
        <div><button type="button" class="btn btn-secondary">수정</button> | <button type="button" class="btn btn-danger">삭제</button></div>

        <button id="Callback" type="button" class="btn btn-warning">다른 리뷰 보러 가기</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewDetail",
}
</script>

<style>
.ReviewDetail1 {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
  display: flex;
  flex-direction: column;
  justify-content: center;
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
.buttons {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-content: center;
  align-items: center;
}
#Callback {
  margin-top: 30px;
  font-size: 30px;
}
</style>
