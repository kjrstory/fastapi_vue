<template>
  <ul>
    <li v-for="question in questionList" :key="question.id">{{ question.subject }}</li>
  </ul>
</template>

<script>
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
      fetch("http://localhost:8000/api/question/list").then((response) => {
        response.json().then((json) => {
          this.questionList = json;
        });
      });
    },
  },
};
</script>
