<template>
  <div>
    <h1>{{ question.subject }}</h1>
    <div>{{ question.content }}</div>
    <ul>
    <li v-for="answer in question.answers" :key="answer.id">{{ answer.content }}</li>
    </ul>
    <form @submit.prevent="postAnswer">
      <textarea rows="15" v-model="content"></textarea>
      <input type="submit" value="답변등록">
    </form>
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
      question: { answers: [] },
      content: "",
    };
  },
  methods: {
    getQuestion() {
      let url = `/api/question/detail/${this.question_id}`
      fastapi('get', url, {}, (json) => {
        this.question = json;
      });
    },
    postAnswer() {
      let url = `/api/answer/create/${this.question_id}`
      let params = {
        content: this.content
      }
      fastapi('post', url, params, () => {
        this.content = ""
        this.error = { detail: [] }
        this.getQuestion()
       },
      )
    },
  },  
  created() {
    this.getQuestion();
  }
}
</script>

<style>
    textarea {
        width:100%;
    }
    input[type=submit] {
        margin-top:10px;
    }
</style>
