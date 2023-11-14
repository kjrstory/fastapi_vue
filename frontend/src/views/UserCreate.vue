<template>
  <div class="container">
    <h5 class="my-3 border-bottom pb-2">회원 가입</h5>
    <ErrorComponent :error="error" />
    <form @submit.prevent="postUser">
      <div class="mb-3">
        <label for="username">사용자 이름</label>
        <input type="text" class="form-control" id="username" v-model="username">
      </div>
      <div class="mb-3">
        <label for="password1">비밀번호</label>
        <input type="password" class="form-control" id="password1" v-model="password1">
      </div>
      <div class="mb-3">
        <label for="password2">비밀번호 확인</label>
        <input type="password" class="form-control" id="password2" v-model="password2">
      </div>
      <div class="mb-3">
        <label for="email">이메일</label>
        <input type="text" class="form-control" id="email" v-model="email">
      </div>
      <button type="submit" class="btn btn-primary">생성하기</button>
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
      username: '',
      password1: '',
      password2: '',
      email: ''
    }
  },
  methods: {
    postUser() {
      let url = "/api/user/create"
      let params = {
        username: this.username,
        password1: this.password1,
        password2: this.password2,
        email: this.email
      }
      fastapi('post', url, params,
        () => {
          this.$router.push("/user-login")
        },
        (json_error) => {
            this.error=json_error
        }
      )
    }
  }
}
</script>
