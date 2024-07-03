<template>
  <div class="container my-3">
    <h4>질문 등록</h4>
    <ErrorComponent :error="error" />
    <form @submit.prevent="postQuestion">
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
        {{ selectedCategory }} 
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea class="form-control" id="content" rows="10" v-model="content"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">저장하기</button>
    </form>
  </div>
</template>

<script>
import fastapi from "../lib/api"
import ErrorComponent from "../components/ErrorComponent.vue"

export default {
  components: {
    ErrorComponent
  },
  data() {
    return {
      error: { detail: [] },
      subject: "",
      content: "",
      selectedCategory: "질문답변",
      categories: {
        '질문답변': 1,
        '강좌': 2,
        '자유게시판': 3,
      },
      categoryMapping: {
        '1': '질문답변',
        '2': '강좌',
        '3': '자유게시판'
      },
    };
  },
  computed: {
    categoryOptions() {
      return Object.keys(this.categories);
    },
  },
  methods: {
    postQuestion() {
      let url = "/api/question/create"
      let params = {
        subject: this.subject,
        content: this.content,
        category_id: this.categories[this.selectedCategory]
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
  },
  created() {
    const urlParams = new URLSearchParams(window.location.search);
    const category_id = urlParams.get('category_id');
    if (category_id) {
      this.selectedCategory = this.categoryMapping[category_id]
    }
  },
}
</script>
