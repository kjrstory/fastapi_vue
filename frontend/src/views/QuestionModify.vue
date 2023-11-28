<template>
  <div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 수정</h5>
    <ErrorComponent :error="error" />
    <form @submit.prevent="updateQuestion" class="my-3">
      <div class="form-group">
        <label for="category">카테고리</label>
        <div class="col-md-2">
        <select class="form-control" id="category" v-model="selectedCategory">
          <option v-for="(category, id) in categoryOptions" :key="id" :value="category">{{ category }}</option>
        </select>
        </div>
      </div>
      <div class="mb-3">
        <label for="subject" class="form-label">제목</label>
        <input type="text" class="form-control" id="subject" v-model="subject">
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea class="form-control" id="content" rows="10" v-model="content"></textarea>
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
    question_id: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      error: { detail: [] },
      subject: '',
      content: '',
      selectedCategory: "질문답변",
      categories: {
        '질문답변': 1,
        '강좌': 2,
        '자유게시판': 3,
      },

    }
  },
  computed: {
    categoryOptions() {
      return Object.keys(this.categories);
    },
  },

  mounted() {
    let url = '/api/question/detail/' + this.question_id;
    fastapi("get", url, {}, (json) => {
        this.subject = json.subject
        this.content = json.content
        this.selectedCategory = json.category.subject
    })
  },
  methods: {
    updateQuestion() {
      let url = '/api/question/update';
      let params = {
        question_id: this.question_id,
        subject: this.subject,
        content: this.content,
        category_id: this.categories[this.selectedCategory]
      };
      fastapi('put', url, params, () => {
          this.$router.push("/detail/"+this.question_id)
      },
      (err_json) => {
          this.error = err_json
      })
    }
  }
};
</script>
