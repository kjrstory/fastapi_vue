<template>
<div class="container my-3">
    <!-- 질문 -->
    <h2 class="border-bottom py-2">{{ question.subject }}</h2>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" v-html="markContent(question.content)"></div>
            <div class="d-flex justify-content-end">
                <div v-if="question.modify_date" class="badge bg-light text-dark p-2 text-start mx-3">
                    <div class="mb-2">modified at</div>
                    <div>{{ formatDate(question.modify_date) }}</div>
                </div>

                <div class="badge bg-light text-dark p-2 text-start">
                    <div class="mb-2" v-if="question.user">{{ question.user.username }}</div>
                    <div class="mb-2" v-else></div>
                    <div>{{ formatDate(question.create_date) }}</div>
                </div>
            </div>

            <button class="btn btn-sm btn-outline-secondary" @click="voteQuestion(question.id)">
               추천
               <span class="badge rounded-pill bg-success">{{ question.voter.length }}</span>
            </button>

            <div class="my-3" v-if="question.user && this.$store.state.username === question.user.username">
               <router-link :to="'/question-modify/' + question.id" class="btn btn-sm btn-outline-secondary">수정</router-link>
               <button class="btn btn-sm btn-outline-secondary" @click="deleteQuestion(question.id)">삭제</button>
            </div>

        </div>
    </div>

    <!-- 댓글(질문) 목록 -->
      <div class="card-header">댓글 리스트</div>

        <div v-if="is_login">
          <button class="btn btn-sm btn-outline-secondary mb-3" @click="toggleCommentInput">댓글 작성</button>
        </div>
        <div v-if="showCommentInput">
           <textarea v-model="commentContent" class="form-control mb-3"
            maxlength="500"
            placeholder="댓글을 입력하세요."></textarea>
        <button class="btn btn-sm btn-outline-secondary mb-3" @click="postCommentQuestion">작성</button>
        <button class="btn btn-sm btn-outline-secondary mb-3" @click="toggleCommentInput">취소</button>
        </div>
    <div v-if="question.comments.length > 0" class="card my-3">
      <div v-for="(comment, index) in question.comments" :key="comment.id" class="my-1">
        <div v-if="index === editIndex">
          <textarea v-model="comment.content" class="form-control mb-3"
              :disabled="is_login ? false : true"
              maxlength="500"
              placeholder="Edit comment"></textarea>
          <button class="btn btn-sm btn-outline-secondary mb-3" @click="updateComment">수정</button>
          <button class="btn btn-sm btn-outline-secondary mb-3" @click="stopEditing">취소</button>
        </div>
          {{comment.content}}, <em>{{comment.user.username}}</em> - <em>{{ formatDate(comment.create_date)}}</em>
           <span v-if="is_login && !isEditing" class="text-muted">
             <button class="btn btn-sm btn-outline-secondary" @click="startEditing(index)">수정</button>
             <button class="btn btn-sm btn-outline-secondary" @click="deleteComment(comment.id)">삭제</button>
          </span>
      </div>
    </div>
    <!-- 끝 -->
    
    <div class="mt-4">
      <router-link to="/" class="btn btn-secondary">
        목록으로
      </router-link>
    </div>

    <!-- 답변 목록 -->
    <div class="row">
     <div class="col-6">
      <h5 class="border-bottom my-3 py-2 mb-0">{{total}}개의 답변이 있습니다.</h5>
     </div>
     <div class="col-6 d-flex justify-content-end align-items-center">
      <button class="btn mr-2 btn-outline-primary" 
              :class="{ active: sort_by === 'voter_count'}"
              @click="this.$store.dispatch('setSortBy', 'voter_count');
                      this.$store.dispatch('setDesc', true)">추천순</button>
      <button class="btn btn-outline-primary" 
              :class="{ active: sort_by === 'create_date' && desc === true}"
              @click="this.$store.dispatch('setSortBy', 'create_date');
                      this.$store.dispatch('setDesc', true)">최신순</button>
      <button class="btn btn-outline-primary" 
              :class="{ active: sort_by === 'create_date' && desc === false}"
              @click="this.$store.dispatch('setSortBy', 'create_date');
                      this.$store.dispatch('setDesc', false)">오래된순</button>
     </div>
    </div>
    <div v-for="answer in answerList" :key="answer.id" class="card my-3">
        <div class="card-body">
            <div class="card-text" v-html="markContent(answer.content)"></div>
            <div class="d-flex justify-content-end">
                <div v-if="answer.modify_date" class="badge bg-light text-dark p-2 text-start mx-3">
                    <div class="mb-2">modified at</div>
                    <div>{{ formatDate(answer.modify_date) }}</div>
                </div>
                <div class="badge bg-light text-dark p-2 text-start">
                   <div class="mb-2" v-if="answer.user">{{ answer.user.username }}</div>
                   <div class="mb-2" v-else></div>
                   <div>{{ formatDate(question.create_date) }}</div>
                </div>
            </div>

            <button class="btn btn-sm btn-outline-secondary" @click="voteAnswer(answer.id)">
               추천
               <span class="badge rounded-pill bg-success">{{ answer.voter.length }}</span>
            </button>

            <div class="my-3" v-if="answer.user && this.$store.state.username === answer.user.username">
               <router-link :to="'/answer-modify/' + answer.id" class="btn btn-sm btn-outline-secondary">수정</router-link>
               <button class="btn btn-sm btn-outline-secondary" @click="deleteAnswer(answer.id)">삭제</button>
            </div>

        </div>
    </div>

    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
      <li class="page-item" :class="{ disabled: answer_page <= 0 }">
        <button class="page-link" @click="this.$store.dispatch('setAnswerPage', answer_page - 1)">이전</button>
      </li>
      <template v-for="(value, index) in Array.from({ length: totalPage })" :key="index">
        <li class="page-item" v-if="index >= answer_page - 5 && index <= answer_page + 5" :class="{ active: index === answer_page }">
          <button class="page-link" @click="this.$store.dispatch('setAnswerPage', index)">{{ index + 1 }}</button>
        </li>
      </template>
      <li class="page-item" :class="{ disabled: answer_page >= totalPage - 1 }">
        <button class="page-link" @click="this.$store.dispatch('setAnswerPage', answer_page + 1)">다음</button>
      </li>
    </ul>
    <!-- 페이징처리 끝 -->

    <!-- 답변 등록 -->
    <form @submit.prevent="postAnswer" class="my-3">
      <div class="mb-3">
        <textarea rows="10" v-model="content" 
               class="form-control"
               :class="{ 'disabled': !is_login }"></textarea>
      </div>
      <input type="submit" value="답변등록" class="btn btn-primary" :class="{ 'disabled': !is_login }">
    </form>
</div>
  
</template>

<script>
import fastapi from '../lib/api';
import moment from 'moment';
import 'moment/locale/ko';
import { parse } from 'marked';

moment.locale('ko')

export default {
  props: {
    question_id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      question: { answers: [], voter:[], content:'', comments:[]  },
      content: "",
      answerList: [],
      size: 5,
      total: 0,
      showCommentInput: false, // 댓글 입력창 토글 상태
      commentContent: "", // 댓글 내용
      isEditing: false, // 댓글 수정창 토글 상태
      editIndex: -1, // 수정할 댓글의 인덱스
    };
  },
  computed: {
      is_login() {
        return this.$store.state.is_login;
      },
      markContent() {
        return (content) => parse(content);
      },
      totalPage() {
        return Math.ceil(this.total / this.size);
      },
      answer_page() { 
          return this.$store.state.answer_page 
      },
      sort_by() { 
          return this.$store.state.sort_by 
      },
      desc() {
           return this.$store.state.desc 
      },
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
        this.content = ''
        this.getQuestion()
       },
      )
    },
    formatDate(date) {
      return moment(date).format('YYYY년 MM월 DD일 HH:mm:ss');
    },
    deleteQuestion(question_id) {
      if(confirm('정말로 삭제하시겠습니까?')) {
        let url = "/api/question/delete";
        let params = {
          question_id: question_id
        }
        fastapi('delete', url, params, () => {
          this.$router.push("/")
        })    
      }
    },
    deleteAnswer(answer_id) {
      if(confirm('정말로 삭제하시겠습니까?')) {
        let url = "/api/answer/delete";
        let params = {
          answer_id: answer_id
        }
        fastapi('delete', url, params, () => {
            this.getQuestion()
        })
      }
    },
    voteQuestion(question_id) {
      if(confirm('정말로 추천하시겠습니까?')) {
        let url = "/api/question/vote";
        let params = {
          question_id: question_id
        }
        fastapi('post', url, params, () => {
            this.getQuestion()
        })
      }
    },
    voteAnswer(answer_id) {
      if(confirm('정말로 추천하시겠습니까?')) {
        let url = "/api/answer/vote";
        let params = {
          answer_id: answer_id
        }
        fastapi('post', url, params, () => {
            this.getQuestion()
        })
      }
    },
    getAnswerList() {
      let url = "/api/answer/list"
      let params = { 
          question_id: this.question_id,
          page: this.answer_page,
          size: this.size,
          sort_by: this.sort_by,
          desc: this.desc
      }
      fastapi('get', url, params, (json) => {
        this.answerList = json.answer_list;
        this.total = json.total;
      });
    },
    toggleCommentInput() {
      this.showCommentInput = !this.showCommentInput;
      this.commentContent = ""; // 댓글 내용 초기화
    },
    startEditing(index) {
      this.editIndex = index;
      this.isEditing = true;
    },
    stopEditing() {
      this.isEditing = false;
      this.editIndex = -1;
    },

    postCommentQuestion() {
      let url = `/api/comment/create/question/${this.question_id}`
      let params = {
        content: this.commentContent
      }
      fastapi('post', url, params, () => {
        this.commentContent = ''
        this.getQuestion()
        this.getAnswerList()
       },
      ),
      this.toggleCommentInput()
    },
    
    updateComment() {
      const comment = this.question.comments[this.editIndex]
      let url = `/api/comment/update`
      let params = {
         content: comment.content
      }
      fastapi('put', url, params, () => {
        this.commentContent = ''
       },
      ),
      this.getQuestion()
      this.getAnswerList()
      this.stopEditing()
    },
    deleteComment(commentId) {
      let url = `/api/comment/delete`
      let params = {
           comment_id: commentId
      }
      fastapi('delete', url, params, () => {
        this.getQuestion()
        this.getAnswerList()
       },
      ),
      this.stopEditing()
    },
    

  },  
  watch: {
    answer_page() {
        this.getAnswerList();
    },
    sort_by() {
        this.getAnswerList();
    },
    desc() {
        this.getAnswerList();
    }
  },
  created() {
    this.getQuestion();
    this.$store.dispatch('setAnswerPage', 0)
    this.$store.dispatch('setSortBy', 'create_date');
    this.$store.dispatch('setDesc', true)
    this.getAnswerList();
  }
}
</script>
