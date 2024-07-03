<template>
  <aside class="bd-sidebar">
    <div class="offcanvas-lg offcanvas-start" id="bdSidebar" aria-labelledby="bdSidebarOffcanvasLabel">
      <div class="offcanvas-body">
        <nav class="bd-links w-100" id="bd-docs-nav" aria-label="문서 내비게이션">
           <strong class="bd-links-heading d-flex w-100 align-items-center fw-semibold fs-5">
            카테고리
           </strong>
           <ul class="nav nav-pills flex-column">              
           <li class="nav-item">
             <router-link :to="'/list/0'" class="nav-link" :class="{ active: $route.path === '/list/0' }" >
             모두
             </router-link>
           </li>
           <li>
             <router-link :to="'/list/1'" class="nav-link" :class="{ active: $route.path === '/list/1' }">
             질문답변
             </router-link>
          </li>
          <li>
             <router-link :to="'/list/2'" class="nav-link" :class="{ active: $route.path === '/list/2' }">
             강좌
             </router-link>
          </li>
          <li>
             <router-link :to="'/list/3'" class="nav-link" :class="{ active: $route.path === '/list/3' }" >
             자유게시판
             </router-link>
          </li> 
          </ul>
        </nav>
      </div>
    </div>
  </aside>
</template>

<script>

</script>
