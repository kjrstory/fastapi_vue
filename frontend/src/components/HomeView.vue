<template>
  <ul>
    <li v-for="question in questionList" :key="question.id">{{ question.subject }}</li>
  </ul>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questionList: [],
    };
  },
  created() {
      this.getQuestionList();
  },
  methods: {
    getQuestionList() {
      axios.get("http://localhost:8000/api/question/list").then(response => {
        this.questionList = response.data;
      }).catch(error => {
        console.log(error);
      });
    },
  },
};
</script>
