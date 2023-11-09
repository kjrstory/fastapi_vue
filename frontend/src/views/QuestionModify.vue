<template>
  <div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 수정</h5>
    <form @submit.prevent="updateQuestion" class="my-3">
      <div class="mb-3">
        <label for="content">내용</label>
        <textarea class="form-control" rows="10" v-model="content"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">수정하기</button>
    </form>
  </div>
</template>

<script>
import fastapi from '../lib/api'

export default {
  props: {
    question_id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      subject: '',
      content: '',
    }
  },
  mounted() {
    let url = '/api/question/detail/' + this.question_id;
    fastapi("get", url, {}, (json) => {
        this.subject = json.subject
        this.content = json.content
    })
  },
  methods: {
    updateQuestion() {
      let url = '/api/question/update';
      let params = {
        question_id: this.question_id,
        subject: this.subject,
        content: this.content
      };
      fastapi('put', url, params, () => {
          this.$router.push("/detail/"+this.question_id)
      })
    }
  }
};
</script>
