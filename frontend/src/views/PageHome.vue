<template>
<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="table-dark">
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
        </tr>
        </thead>
    <tbody>
    <tr v-for="(question,i) in questionList" :key="question.id">
      <td>{{ i+1 }}</td>
      <td>
        <router-link :to="'/detail/' + question.id">{{ question.subject }}</router-link>
      </td>
      <td>{{question.create_date}}</td>
    </tr>
    </tbody>
    </table>
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
      <li class="page-item" :class="{ disabled: page <= 0 }">
        <button class="page-link" @click="getQuestionList(page - 1)">이전</button>
      </li>
      <template v-for="(_, loop_page) in Array.from({ length: totalPage })" :key="loop_page">
        <li class="page-item" 
            v-if="loop_page >= page - 5 && loop_page <= page + 5"
            :class="{ active: loop_page === page }">
          <button class="page-link" @click="getQuestionList(loop_page)">{{ loop_page + 1 }}</button>
        </li>
      </template>
      <li class="page-item" :class="{ disabled: page >= totalPage - 1 }">
        <button class="page-link" @click="getQuestionList(page + 1)">다음</button>
      </li>
    </ul>
    <!-- 페이징처리 끝 -->    
    <div class="d-flex justify-content-start">
      <router-link to="/question-create" class="btn btn-primary">질문 등록하기</router-link>
    </div>  
</div>    
</template>

<script>
  import fastapi from '../lib/api';

  export default {
    data() {
      return {
        questionList: [],
        size: 10,
        total: 0,
      };
    },
    computed: {
      page() {
        return this.$store.state.page;
      },  
      totalPage() {
        return Math.ceil(this.total / this.size);
      },
    },
    methods: {
      getQuestionList(_page) {
        let url = "/api/question/list"
        let params = { 
            page: _page,
            size: this.size}
        fastapi('get', url, params, (json) => {
          this.questionList = json.question_list;
          this.$store.commit('setPage',_page);
          this.total = json.total;
        });
      }
    },
    created() {
      this.getQuestionList(this.$store.state.page);
    }
  }
</script>
