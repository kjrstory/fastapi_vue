<template>
  <div class="container my-3">
    <h4>질문 등록</h4>
    <form @submit.prevent="postQuestion">
      <div class="mb-3">
        <label for="subject" class="form-label">제목</label>
        <input type="text" class="form-control" id="subject" v-model="subject" required>
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea class="form-control" id="content" rows="10" v-model="content" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">저장하기</button>
    </form>
  </div>
</template>

<script>
  import fastapi from "../lib/api"

  export default {
    data() {
      return {
        error: { detail: [] },
        subject: "",
        content: "",
      };
    },
    methods: {
      postQuestion() {
        let url = "/api/question/create"
        let params = {
          subject: this.subject,
          content: this.content,
        }
        fastapi('post', url, params, 
          () => {
            this.$router.push("/")
          },
          (json_error) => {
            this.error = json_error
          }
        )
      }
    }
  }
</script>
