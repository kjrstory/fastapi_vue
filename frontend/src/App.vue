<template>
  <NavigationBar />
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-2">
        <SideBar />
      </div>
      <main role="main" class="col-md-10">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script>
import NavigationBar from "./components/NavigationBar.vue"
import SideBar from "./components/SideBar.vue"

export default {
  name: 'App',
  components: {
     NavigationBar,
     SideBar
  }
}
</script>

