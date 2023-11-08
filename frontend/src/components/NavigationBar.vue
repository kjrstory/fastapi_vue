<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand" @click="setPage(0)">Pybo</router-link>
      <button 
        class="navbar-toggler" 
        type="button" 
        data-bs-toggle="collapse" 
        data-bs-target="#navbarNav" 
        aria-controls="navbarNav" 
        aria-expanded="false" 
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item" v-if="is_login">
             <a class="nav-link" href="/user-login" @click.prevent="logoutUser">로그아웃 ({{ username }})</a>
          </li>
          <li class="nav-item" v-if="!is_login">
            <router-link to="/user-create" class="nav-link">회원가입</router-link>
          </li>  
          <li class="nav-item" v-if="!is_login">  
            <router-link to="/user-login" class="nav-link">로그인</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  computed: {
      is_login() {
        return this.$store.state.is_login;
      },
      username() {
        return this.$store.state.username;
      },
  },
  methods: {
    setPage(page) {
      this.$store.dispatch('setPage', page);
    },
    logoutUser() {
      this.$store.dispatch("setAccessToken", "")
      this.$store.dispatch("setUsername", "")
      this.$store.dispatch("setIsLogin", false)
    }
  }
}
</script>
