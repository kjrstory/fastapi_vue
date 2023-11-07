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
</div>    
</template>

<script>

import fastapi from '../lib/api';

export default {
  data() {
    return {
      questionList: []
    };
  },
  created() {
    fastapi('get', '/api/question/list', {}, (json) => {
      this.questionList = json;
    });
  }
}
</script>
