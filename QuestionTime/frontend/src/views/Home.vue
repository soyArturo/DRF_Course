<template>
    <div class="home">
        <div class="container mt-5">
            <div class v-for="question in questions" :key="question.pk">
                <div class="card shadow mb-2">
                    <div class="card-body">
                        <p class="mb-2  card-title">
                            Posted by:
                            <span class="author-name">{{ question.author }}</span>
                        </p>
                        <h2 class="card-text">
                          <router-link class="link-question" :to="{name: 'Question', params:{slug:question.slug} }">{{question.content}}</router-link>
                          
                          </h2>
                        <p class="card-subtitle">Answers: {{question.answer_count}}</p>
                    </div>
                </div>

            </div>
            <div class="my-4">
                <p v-show="loadingQuestions">...loading...</p>
                <button v-show="next"
                @click="getQuestions"
                class="btn btn-sm btn-outline-success">
                Load more
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
    name: "Home",
    data() {
        return {
            questions: [],
            next: null,
            loadingQuestions:false
        };
    },
    methods: {
        getQuestions() {
            let endpoint = "/api/questions/";
            if (this.next) {
                endpoint = this.next;
            }
            this.loadingQuestions = true
            apiService(endpoint).then(data => {
                this.questions.push(...data.results)
                this.loadingQuestions = false
                if (data.next) {
                    this.next = data.next;
                }else{
                    this.next = null;
                }
            });
        }
    },
    created() {
        this.getQuestions();
        document.title = "QuestionTime";
    }
};
</script>

<style scoped>
.card{
  background-color: white;
  border: 0px;
}
.card-title{
  color: #111;
}
.card-body{
  color: #111;
}
.author-name {
    font-weight: bold;
    color: #1b5299;
    text-transform: capitalize;
}
.link-question{
  color: #111;
}
.link-question:hover{
  color: #1b5299;
  text-decoration: none;
}
</style>
