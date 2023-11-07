<template>
  <ul>
    <li v-for="question in questionList" :key="question.id">
      <router-link :to="'/detail/' + question.id">{{ question.subject }}</router-link>
    </li>
  </ul>
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
