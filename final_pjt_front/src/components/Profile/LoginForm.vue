<template>
  <div class="LoginForm">
    <form @submit.prevent="Login" class="login">
      <h1>Login</h1>
      <div id="LoginForm_ID" class="mb-3">
        <label for="Id" class="form-label">아이디(ID)</label>
        <input class="form-control" id="id" placeholder="아이디를 입력하세요" v-model="username" />
      </div>
      <div id="LoginForm_Password" class="mb-3">
        <label for="password" class="form-label">패스워드(PASSWORD)</label>
        <input class="form-control" id="password" type="password" placeholder="패스워드를 입력하세요" v-model="password" />
      </div>
      <button type="submit" class="btn btn-warning btn-lg mt-5">로그인하기</button>
    </form>
    <!-- <div class="mt-5">
      <button type="button" class="btn btn-outline-warning btn-lg">아직 아이디가 없으신가요?</button>
    </div> -->
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "LoginForm",
  components: {},
  data() {
    return {
      username: "",
      password: "",
    }
  },
  methods: {
    Login() {
      const userdata = {
        username: this.username,
        password: this.password,
      }
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/v1/accounts/login/",
        data: userdata,
      })
        .then((res) => {
          if (res.data.status === "success") {
            console.log(res);
            this.$store.dispatch("Login", res.data.userID)
            this.$store.dispatch("UserInteractionUpdate", res.data)
            this.$router.push("/")
          } else {
            alert("비밀번호가 틀렸습니다!")
          }
        })
        .catch((err) => console.log(err))
    },
  },
}
</script>

<style>
.LoginForm {
  margin-top: 70px;
  margin-left: 200px;
  background-color: black;
  display: flex;
  justify-content: center;
}
.login {
  width: 1000px;
  height: 1000px;
  margin: 300px;
}
#LoginForm_ID {
  text-align: start;
  font-size: 30px;
}

#LoginForm_Password {
  text-align: start;
  font-size: 30px;
}
</style>
