<template>
  <div class="container">
    <h5 class="my-3 border-bottom pb-2">로그인</h5>
    <ErrorComponent :error="error" />
    <form @submit.prevent="loginUser">
      <div class="mb-3">
        <label for="username">사용자 이름</label>
        <input type="text" class="form-control" id="username" v-model="login_username">
      </div>
      <div class="mb-3">
        <label for="password">비밀번호</label>
        <input type="password" class="form-control" id="password" v-model="login_password">
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
import fastapi from "../lib/api"
import ErrorComponent from "../components/ErrorComponent.vue"

export default {
  components: {
    ErrorComponent
  },
  data() {
    return {
      error: { detail: [] },
      login_username: '',
      login_password: ''
    }
  },
  methods: {
    loginUser() {
      let url = "/api/user/login"
      let params = {
        username: this.login_username,
        password: this.login_password,
      }
      fastapi('login', url, params,
        (json) => {
          this.$store.dispatch("setAccessToken", json.access_token)
          this.$store.dispatch("setUsername", json.username)
          this.$store.dispatch("setIsLogin", true)
          this.$router.push("/")
        }
      )
    }
  }
}
</script>
