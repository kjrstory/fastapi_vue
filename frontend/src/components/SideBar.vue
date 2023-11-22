<template>
  <div class="d-flex flex-column flex-shrink-0 p-3 text-black bg-light" style="width: 280px;">
    <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-black text-decoration-none">
      <span class="fs-4">카테고리</span>
    </a>
    <hr>
    <ul class="nav nav-pills flex-column mb-auto">
      <li class="nav-item">
        <router-link :to="'/list/0'" class="nav-link text-black fs-5"
                     :class="{ active: $route.path === '/list/0' } ">
          모두
        </router-link>
      </li>
      <li>
        <router-link :to="'/list/1'" class="nav-link text-black fs-5"
                     :class="{ active: $route.path === '/list/1' } ">
          질문답변
        </router-link>
      </li>
      <li>
        <router-link :to="'/list/2'" class="nav-link text-black fs-5"
                     :class="{ active: $route.path === '/list/2' } ">
          강좌
        </router-link>
      </li>
      <li>
        <router-link :to="'/list/3'" class="nav-link text-black fs-5"
                     :class="{ active: $route.path === '/list/3' } ">
          자유게시판
        </router-link>
      </li>
    </ul>
    <hr>
  </div>
</template>

<script>

</script>
