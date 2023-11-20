<template>
  <!-- 댓글 목록 -->
  <div v-if="question.comments.length > 0" class="card my-3">
    <div v-for="comment in question.comments" :key="comment.id" class="my-1">
      <div v-if="editIndex === comment.id">
        <input v-model="content" class="form-control mb-3"
            :disabled="is_login ? false : true"
            maxlength="500"
            placeholder="Edit comment">
        <span style="cursor: pointer; color: blue; margin: 2px;"
              @click="updateComment(comment.id)">저장</span>
        <span style="cursor: pointer; color: red; margin: 2px;"
              @click="stopEditing">취소</span>
      </div>
      <div v-if="editIndex !== comment.id">
      <span> {{comment.content}}, </span>
      <span class="text-muted"> - {{comment.user.username}}, </span>
      <span class="text-muted"> {{formatDate(comment.create_date)}} </span>
      <span v-if="comment.user && $store.state.username === comment.user.username" 
            @click="startEditing(comment.id, comment.content)"
            style="cursor: pointer; color: blue; margin: 2px;">
           수정</span>
      <span v-if="comment.user && $store.state.username === comment.user.username"
            @click="deleteComment(comment.id)"
            style="cursor: pointer; color: red; margin: 2px;">
           삭제</span>
      </div>     
    </div>
  </div>
  <!-- 댓글 목록 끝 -->
  <!-- 댓글 입력 -->
  <div>
    <ErrorComponent :error="error" />
    <button class="btn btn-sm btn-outline-secondary mb-3"
            @click="toggleCommentInput"
            :class="{ 'disabled': !is_login }">
            댓글 작성</button>
  </div>
  <div v-if="showCommentInput">
     <input v-model="content" class="form-control mb-3"
            maxlength="500"
            placeholder="댓글을 입력하세요.">
     <span @click="postCommentQuestion"
           style="cursor: pointer; color: blue; margin: 2px;">저장</span>
     <span @click="toggleCommentInput"
           style="cursor: pointer; color: red; margin: 2px;">취소</span>
  </div>
  <!-- 댓글 입력 끝 -->
</template>

<script>
import fastapi from '../lib/api';
import ErrorComponent from "../components/ErrorComponent.vue"
import moment from 'moment';
import 'moment/locale/ko';

moment.locale('ko')

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
      question: { answers: [], voter:[], content:'', comments:[] },
      isEditing: false, // 댓글 수정창 토글 상태
      editIndex: -1, // 수정할 댓글의 인덱스
      content: "",
      showCommentInput: false,
    }
  },
  computed: {
    is_login() {
      return this.$store.state.is_login;
    }
  },
  methods: {
    getQuestion() {
      let url = `/api/question/detail/${this.question_id}`
      fastapi('get', url, {}, (json) => {
        this.question = json;
      });
    },
    formatDate(date) {
      return moment(date).format('YYYY년 MM월 DD일 hh:mm a');
    },
    postCommentQuestion() {
        let url = `/api/comment/create/question/${this.question_id}`
        let params = {
          content: this.content
        }
        fastapi('post', url, params, () => {
         this.content = ''
         this.getQuestion()
         this.toggleCommentInput()
        },
        (err_json) => {
          this.error = err_json
        }
      )
    },
    updateComment(commentId) {
        let url = `/api/comment/update`
        let params = {
          comment_id: commentId, 
          content: this.content,
        }
        fastapi('put', url, params, () => {
          this.getQuestion()
          this.stopEditing()
        },
        (err_json) => {
          this.error = err_json
        }
      )
    },
    deleteComment(commentId) {
      if(confirm('정말로 삭제하시겠습니까?')) {  
        let url = `/api/comment/delete`
        let params = {
          comment_id: commentId
        }
        fastapi('delete', url, params, () => {
          this.getQuestion()
          },
          (err_json) => {
            this.error = err_json
        })
      }
    },
    toggleCommentInput() {
      this.showCommentInput = !this.showCommentInput;
      this.content = "";
    },
    startEditing(index,_content) {
      this.editIndex = index;
      this.isEditing = true;
      this.content = _content;
    },
    stopEditing() {
      this.isEditing = false;
      this.editIndex = -1;
    },
  },
  created() {
    this.getQuestion();
  },

};
</script>

