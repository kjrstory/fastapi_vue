<template>
<div class="container my-3">
    <div class="row my-3">
      <div class="col-6">
       <a :href="'/question-create?category_id=' + category_id" 
          class="btn btn-primary" :class="{ disabled: !is_login }">
        질문 등록하기
       </a>
     </div>
     <div class="col-6">
       <div class="input-group">
         <input type="text" class="form-control" v-model="kw">
         <button class="btn btn-outline-secondary" 
         @click="$store.commit('setKeyword', kw);
                 $store.commit('setPage', 0)">
           찾기
         </button>
       </div>
      </div>
    </div>
    <table class="table">
        <thead>
        <tr class="text-center table-dark">
            <th>카테고리</th>
            <th>번호</th>
            <th style="width:50%">제목</th>
            <th>글쓴이</th>
            <th>작성일시</th>
        </tr>
        </thead>
    <tbody>
    <tr v-for="(question,i) in questionList" :key="question.id" class="text-center">
      <td>{{ question.category.subject }}</td>
      <td>{{ total - page * size - i }}</td>
      <td class="text-start">
        <router-link :to="'/detail/' + question.id"
                     @click="$store.commit('setAnswerPage', 0);
                             $store.commit('setSortBy', 'create_date');
                             $store.commit('setDesc', true);"
                     >{{ question.subject }}</router-link>
        <span v-if="question.answers.length > 0" 
              class="text-danger small mx-2">{{question.answers.length}}</span>
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
        <button class="page-link" @click="$store.commit('setPage', page - 1)">이전</button>
      </li>
      <template v-for="(_, loop_page) in Array.from({ length: totalPage })" :key="loop_page">
        <li class="page-item" 
            v-if="loop_page >= page - 5 && loop_page <= page + 5"
            :class="{ active: loop_page === page }">
          <button class="page-link" @click="$store.commit('setPage', loop_page)">{{ loop_page + 1 }}</button>
        </li>
      </template>
      <li class="page-item" :class="{ disabled: page >= totalPage - 1 }">
        <button class="page-link" @click="$store.commit('setPage', page + 1)">다음</button>
      </li>
    </ul>
    <!-- 페이징처리 끝 -->
</div>    
</template>

<script>
  import fastapi from '../lib/api';
  import moment from 'moment'
  import 'moment/locale/ko'

  moment.locale('ko')

  export default {
    props: {
      category_id: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        questionList: [],
        size: 10,
        total: 0,
        kw: "",
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
      keyword() {
        return this.$store.state.keyword;
      },
    },
    methods: {
      getQuestionList() {
        let url = "/api/question/list"
        let params = { 
            page: this.page,
            size: this.size,
            keyword: this.keyword,
            category_id: this.category_id,
        }
        fastapi('get', url, params, (json) => {
          this.questionList = json.question_list;
          this.total = json.total;
          this.kw = this.keyword
        });
      },
      formatDate(date) {
        return moment(date).format('YYYY년 MM월 DD일 hh:mm a');
      }
    },
    watch: {
      page() {
        this.getQuestionList();
      },
      keyword() {
        this.getQuestionList();
      },
      category_id() {
        this.getQuestionList();
      }
    },
    created() {
      this.getQuestionList();
    }
  }
</script>
