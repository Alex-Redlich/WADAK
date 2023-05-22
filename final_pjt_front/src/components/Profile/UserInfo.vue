<template>
  <div class="UserInfo">
    <div id="UserInfo">
      <div class="row">
        <dlv id="UserImagediv" class="col-4">
          <img id="UserImage" src="@/assets/profile.jpg" alt="" />
          <button id="EditBtn" class="btn btn-warning">Edit Profile</button>
        </dlv>
        <div id="UserDetail" class="col-4">
          <p>칭호</p>
          <p>닉네임</p>
          <p>아 하기싫어..아 하기싫어..</p>
        </div>
        <div id="Userintro" class="col-4">
          <p>팔로잉 : 0 명</p>
          <p>팔로워 : 0 명</p>
          <p>내 게시글 : 0 명</p>
          <p>내 코멘트 : 0 명</p>
          <div class="expoint">경험치바</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserInfo",
  components: {},
}
</script>

<style>
.UserInfo {
  display: flex;
  justify-content: center;
}
#UserImagediv {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#UserImage {
  border-radius: 3000px;
  width: 300px;
  height: 300px;
  margin: 25px;
}
#EditBtn {
  width: 200px;
  border-radius: 30px;
  margin-bottom: 20px;
}
#UserInfo {
  background-color: white;
  width: 1500px;
  color: black;
  border-radius: 30px;
}
#UserDetail {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
#Userintro {
  margin-top: 30px;
}
.expoint {
  height: 100px;
  background-color: blueviolet;
}
</style>
