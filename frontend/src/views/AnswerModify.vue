<template>
  <div class="container">
    <ErrorComponent :error="error" />
    <h5 class="my-3 border-bottom pb-2">답변 수정</h5>
    <form @submit.prevent="updateAnswer" class="my-3">
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
import ErrorComponent from "../components/ErrorComponent.vue"

export default {
  components: {
    ErrorComponent
  },
  props: {
    answer_id: {
      type: String,
      required: true
    },
  },
  data() {
    return {
      error: { detail: [] },
      question_id: 0,  
      content: '',
    }
  },
  mounted() {
    fastapi("get", "/api/answer/detail/" + this.answer_id, {}, (json) => {
        this.question_id = json.question_id
        this.content = json.content
    })
  },
  methods: {
    updateAnswer() {
      let url = '/api/answer/update';
      let params = {
        answer_id: this.answer_id,
        content: this.content
      };
      fastapi('put', url, params, () => {
          this.$router.push("/detail/"+this.question_id)
      }),
        (json_error) => {
          this.error = json_error
      }
    }
  }
};
</script>
