<template>
  <div class="UserInfo">
    <div id="UserInfo">
      <div class="row">
        <dlv id="UserImagediv" class="col-4">
          <img id="UserImage" src="@/assets/profile.jpg" alt="" />
          <button id="EditBtn" class="btn btn-warning text-center" @click="GoUpdate">Edit Profile</button>
        </dlv>
        <div id="UserDetail" class="col-4">
          <div class="row align-items-center">
            <p id="chingho">[매일눈물흘리는 어린꿈나무]</p>
            <div>
              <!-- 인벤토리 버튼 -->
              <button v-if="userId" id="InvenBtn" class="btn btn-warning" @click="GoInventory">인벤토리</button>
              <div v-else>
                <!-- 본인 프로필이 아니라면 팔로우 버튼 생성 -->
                <button v-if="isFollowed" id="followBtn" class="btn btn-danger" @click="follow">팔로잉취소</button>
                <button v-else id="followBtn" class="btn btn-primary" @click="follow">팔로잉하기</button>
              </div>
            </div>
          </div>

          <div class="d-flex align-items-baseline">
            <p id="Nickname">세종시속도제한20KM</p>
            <img id="levelsymbol" src="@/assets/level/2.png" alt="" />
          </div>
          <p id="message">
            난 가끔 눈물을 흘린다난 가끔 눈물을 흘린다난 가끔 눈물을 흘린다난 가끔 눈물을 흘린다난 가끔 눈물을 흘린다난 가끔 눈물을 흘린다난 가끔 눈물을 흘린다난 가끔 눈물을 흘린다난 가끔 눈물을
            흘린다난 가끔 눈물을 흘린다
          </p>
        </div>
        <div id="Userintro" class="col-4">
          <p>팔로잉 : 0 명</p>
          <p>팔로워 : 0 명</p>
          <p>내 게시글 : 0 명</p>
          <p>내 코멘트 : 0 명</p>
          <!-- <div class="expoint">
            <p>User's EXP</p>
            <div id="totalex">
              <div id="todayex"></div>
            </div>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserInfo",
  components: {},
  data() {
    return {
      userId: false,
      isFollowed: true,
    }
  },
  methods: {
    GoInventory() {
      this.$router.push({ name: "inventory" })
    },
    GoUpdate() {
      this.$router.push({ name: "update", params: { userID: "" } })
    },
  },
}
</script>

<style>
.UserInfo {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
  padding-top: 30px;
}
#chingho {
  margin-top: 20px;
  font-size: 30px;
}
#Nickname {
  font-size: 40px;
  margin-bottom: 50px;
}
#message {
  font-size: 30px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
#levelsymbol {
  width: 30px;
  height: 30px;
  margin-left: 10px;
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
  margin-top: 50px;
  font-size: 20px;
}
.expoint {
  padding: 20px;
  margin-top: 60px;
  text-align: center;
  height: 100px;
}
#totalex {
  width: 450px;
  height: 10px;
  background-color: rgb(150, 150, 150);
}
#todayex {
  width: 50px;
  height: 10px;
  background-color: rgb(218, 196, 0);
}
</style>
