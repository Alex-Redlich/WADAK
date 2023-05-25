<template>
  <div class="SignupForm">
    <form @submit.prevent="Signup" class="signup">
      <h1>Sign Up</h1>
      <div id="signForm_ID" class="mb-3">
        <label for="Id" class="form-label">아이디(ID)</label>
        <input class="form-control" id="id" placeholder="아이디를 입력하세요" v-model="username" />
      </div>
      <div id="signForm_Password" class="mb-3">
        <label for="password" class="form-label">패스워드(PASSWORD)</label>
        <input
          type="password"
          class="form-control"
          id="password"
          placeholder="패스워드를 입력하세요"
          v-model="password"
        />
      </div>
      <div id="signForm_Password" class="mb-3">
        <label for="password2" class="form-label">패스워드(CHECK)</label>
        <input
          type="password"
          class="form-control"
          id="password2"
          placeholder="패스워드를 확인하세요"
          v-model="password2"
        />
      </div>
      <div id="signForm_Nickname" class="mb-3">
        <label for="nickname" class="form-label">닉네임(NICKNAME)</label>
        <input class="form-control" id="nickname" placeholder="닉네임을 입력하세요" v-model="nickname" />
      </div>
      <div id="signForm_intro" class="mb-3">
        <label for="intro" class="form-label">자기소개</label>
        <textarea class="form-control" id="intro" placeholder="자기소개를 입력하세요" v-model="intro" />
      </div>
      <button type="submit" class="btn btn-warning btn-lg mt-5">회원 가입</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignupForm",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      nickname: "",
      intro: "",
    };
  },
  methods: {
    Signup() {
      const userdata = {
        username: this.username,
        password: this.password,
        password2: this.password2,
        nickname: this.nickname,
        intro: this.intro,
      };
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/v1/accounts/signup/",
        data: userdata,
      })
        .then(() => {
          this.$router.push({ name: "login" });
        })
        .catch((err) => console.log(err));
      console.log(userdata);
    },
  },
};
</script>

<style>
.SignupForm {
  margin-top: 70px;
  padding-top: 100px;
  margin-left: 200px;
  background-color: black;
  display: flex;
  justify-content: center;
}
.signup {
  width: 1000px;
  height: 1000px;
}
#signForm_ID {
  text-align: start;
  font-size: 30px;
}

#signForm_Password {
  text-align: start;
  font-size: 30px;
}
#signForm_Nickname {
  text-align: start;
  font-size: 30px;
}
#signForm_intro {
  text-align: start;
  font-size: 30px;
}
#intro {
  height: 300px;
}
</style>
