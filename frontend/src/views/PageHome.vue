<template>
<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="text-center table-dark">
            <th>번호</th>
            <th style="width:50%">제목</th>
            <th>글쓴이</th>
            <th>작성일시</th>
        </tr>
        </thead>
    <tbody>
    <tr v-for="(question,i) in questionList" :key="question.id" class="text-center">
      <td>{{ total - page * size - i }}</td>
      <td class="text-start">
        <router-link :to="'/detail/' + question.id">{{ question.subject }}</router-link>
        <span v-if="question.answers.length > 0" class="text-danger small mx-2">{{question.answers.length}}</span>
      </td>
      <td v-if="question.user">{{ question.user.username }}</td>
      <td v-else></td>
      <td>{{ formatDate(question.create_date) }}</td>
    </tr>
    </tbody>
    </table>
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
      <li class="page-item" :class="{ disabled: page <= 0 }">
        <button class="page-link" @click="getQuestionList(page - 1)">이전</button>
      </li>
      <template v-for="(value, index) in Array.from({ length: totalPage })" :key="index">
        <li class="page-item" v-if="index >= page - 5 && index <= page + 5" :class="{ active: index === page }">
          <button class="page-link" @click="getQuestionList(index)">{{ index + 1 }}</button>
        </li>
      </template>
      <li class="page-item" :class="{ disabled: page >= totalPage - 1 }">
        <button class="page-link" @click="getQuestionList(page + 1)">다음</button>
      </li>
    </ul>
    <!-- 페이징처리 끝 -->
    <div class="d-flex justify-content-start">
      <router-link to="/question-create" class="btn btn-primary" :class="{ 'disabled': !is_login }">질문 등록하기</router-link>
    </div>  
</div>    
</template>

<script>
  import fastapi from '../lib/api';
  import moment from 'moment'
  import 'moment/locale/ko'
  moment.locale('ko')

  export default {
    data() {
      return {
        questionList: [],
        size: 10,
        total: 0,
      };
    },
    computed: {
      is_login() {
        return this.$store.state.is_login;
      },
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
          this.$store.dispatch('setPage',_page);
          this.total = json.total;
        });
      },
      formatDate(date) {
        return moment(date).format('YYYY년 MM월 DD일 HH:mm:ss');
      }
    },
    created() {
      this.getQuestionList(this.$store.getters.getPage);
    }
  }
</script>
