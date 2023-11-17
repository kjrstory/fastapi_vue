<template>
  <!-- 댓글 목록 -->
  <div v-if="answer.comments.length > 0" class="card my-3">
    <div v-for="comment in answer.comments" :key="comment.id" class="my-1">
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
     <span @click="postCommentAnswer"
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
    answer_id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      error: { detail: [] },  
      answer: { comments:[] },
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
    getAnswer() {
      let url = `/api/answer/detail/${this.answer_id}`
      fastapi('get', url, {}, (json) => {
        this.answer = json;
      });
    },
    formatDate(date) {
      return moment(date).format('YYYY년 MM월 DD일 hh:mm a');
    },
    postCommentAnswer() {
        let url = `/api/comment/create/answer/${this.answer_id}`
        let params = {
          content: this.content
        }
        fastapi('post', url, params, () => {
          this.content = ''
          this.getAnswer()
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
          this.getAnswer()
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
          this.getAnswer()
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
    this.getAnswer();
  },

};
</script>
