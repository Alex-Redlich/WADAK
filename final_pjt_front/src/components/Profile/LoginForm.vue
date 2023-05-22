<template>
  <div class="LoginForm">
    <div class="createform">
      <h1>Login</h1>
      <div id="LoginForm_ID" class="mb-3">
        <label for="Id" class="form-label">아이디(ID)</label>
        <input class="form-control" id="id" placeholder="아이디를 입력하세요" />
      </div>
      <div id="LoginForm_Password" class="mb-3">
        <label for="password" class="form-label">패스워드(PASSWORD)</label>
        <input class="form-control" id="password" placeholder="패스워드를 입력하세요" />
      </div>
      <button type="button" class="btn btn-warning btn-lg mt-5">로그인하기</button>
      <div class="mt-5">
        <button type="button" class="btn btn-outline-warning btn-lg">아직 아이디가 없으신가요?</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  components: {},
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
.createform {
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
