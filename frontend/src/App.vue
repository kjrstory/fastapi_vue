<template>
  <NavigationBar />
  <div class="container-xxl  bd-layout">
    <div class="d-flex">
    <SideBar />
    <main class="bd-main "  style="flex-grow: 1;">
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

