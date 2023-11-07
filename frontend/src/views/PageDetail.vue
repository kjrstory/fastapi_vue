<template>
  <div>
    <h1>{{ question.subject }}</h1>
    <div>{{ question.content }}</div>
  </div>
</template>

<script>
import fastapi from '../lib/api';

export default {
  props: {
    question_id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      question: {}
    };
  },
  methods: {
    getQuestion() {
      fastapi('get', `/api/question/detail/${this.question_id}`, {}, (json) => {
        this.question = json;
      });
    }
  },
  created() {
    this.getQuestion();
  }
}
</script>
