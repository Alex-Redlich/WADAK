<template>
  <div class="UpdateForm">
    <form @submit.prevent="UpdateProfile" class="UpdateProfile">
      <h1>프로필 수정</h1>
      <div id="updateForm_Nickname" class="mb-3">
        <label for="update_Nickname" class="form-label">닉네임(NICKNAME)</label>
        <input class="form-control" id="update_Nickname" placeholder="닉네임을 입력하세요" v-model="Nickname" />
      </div>
      <div id="updateForm_intro" class="mb-3">
        <label for="update_intro" class="form-label">자기소개</label>
        <input class="form-control" id="update_intro" placeholder="자기소개를 입력하세요" v-model="Intro" />
      </div>
      <button type="submit" class="btn btn-warning btn-lg mt-5">수정하기</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UpdateForm",
  data() {
    return {
      Nickname: "",
      Intro: "",
      userID: this.$store.state.userID,
      Userinfo: {},
    };
  },
  components: {},
  methods: {
    UpdateProfile() {
      const userdata = {
        nickname: this.Nickname,
        intro: this.Intro,
        userID: this.$store.state.userID,
      };
      axios({
        method: "put",
        url: `http://127.0.0.1:8000/api/v1/accounts/update/${this.$store.state.userID}/`,
        data: userdata,
      })
        .then((res) => {
          console.log(res.data)
          this.$router.go({ name: "profile", params: { userID: this.$store.state.id, Userinfo: this.Userinfo } });
        })
        .catch((err) => console.log(err));
      console.log(userdata);
    },
  },
};
</script>

<style>
.UpdateForm {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
  display: flex;
  justify-content: center;
}
.UpdateProfile {
  width: 1000px;
  height: 1000px;
  margin: 300px;
}
#updateForm_Nickname {
  text-align: start;
  font-size: 30px;
}
#update_Nickname {
  font-size: 30px;
}
#updateForm_intro {
  text-align: start;
  font-size: 30px;
}
#update_intro {
  font-size: 30px;
}
</style>
