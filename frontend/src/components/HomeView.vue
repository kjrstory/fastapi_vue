<template>
  <ul>
    <li v-for="question in questionList" :key="question.id">{{ question.subject }}</li>
  </ul>
</template>

<script>
  import fastapi from "../lib/api"

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
        fastapi('get', '/api/question/list', {}, (json) => {
            this.questionList = json
        });
    },
  },
};
</script>
