<template>
    <div class="container mt-5">
        <div class="card shadow mb-2">
            <div class="card-body">
                <h1 class="card-text">{{question.content}}</h1>
                <p class="mb-2 card-title">
                    Posted by:
                    <span class="author-name">{{ question.author }}</span>
                </p>

                <p class="card-subtitle">{{question.created_at}}</p>
            </div>
        </div>
        <hr />
        <div v-if="userHasAnswered">
            <p class="answer-added">You've written an answer!</p>
        </div>
        <div v-else-if="showForm">
            <form class="card shadow" @submit.prevent="onSubmit">
                <div class="card-title mt-3 ml-3">
                    <h3>Answer the Question</h3>
                </div>
                <div class="card-body px-3">
                    <textarea
                        v-model="newAnswerBody"
                        class="form-control"
                        placeholder="Share Your Knowledge!"
                        rows="5"
                    ></textarea>
                    <div class="mt-3">
                        <button
                            type="submit"
                            class="btn btn-sm btn-success mr-2"
                            style="background-color: #1b5299; border-color:#1b5299;"
                        >Submit Your Answer</button>
                        <button
                            @click="showForm = false"
                            type="reset"
                            class="btn btn-sm btn-danger"
                        >Cancel</button>
                    </div>
                </div>
            </form>
            <p v-if="error" class="error mt-2">{{ error }}</p>
        </div>
        <div v-else>
            <button
                class="btn btn-sm btn-success"
                style="background-color: #1b5299; border-color:#1b5299;"
                @click="showForm = true"
            >Answer the Question</button>
        </div>
        <hr />
        <div class="container">
            <h3>Answers</h3>
            <AnswerComponent
                class="full-w"
                v-for="answer in answers"
                :answer="answer"
                :requestUser="requestUser"
                :key="answer.id"
                 @delete-answer="deleteAnswer"
            />
        </div>
        <div class="my-4 text-center">
            <p v-show="loadingAnswers">...loading...</p>
            <button
                v-show="next"
                @click="getQuestionAnswers"
                class="btn btn-sm btn-outline-success"
            >Load More</button>
        </div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import AnswerComponent from "@/components/Answer.vue";
export default {
    name: "Question",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    components: {
        AnswerComponent
    },
    data() {
        return {
            question: {},
            answers: [],
            newAnswerBody: null,
            error: null,
            userHasAnswered: false,
            showForm: false,
            next: null,
            loadingAnswers: false,
            requestUser: null
        };
    },
     computed: {
    isQuestionAuthor() {
      // return true if the logged in user is also the author of the question instance
      return this.question.author === this.requestUser;
    }
  },
    methods: {
        setPageTitle(title) {
            // set a given title string as the webpage title
            document.title = title;
        },
        setRequestUser() {
            // the username has been set to localStorage by the App.vue component
            this.requestUser = window.localStorage.getItem("username");
        },
        getQuestionData() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint).then(data => {
                this.question = data;
                this.userHasAnswered = data.user_has_answered;
                this.setPageTitle(data.content);
            });
        },
        getQuestionAnswers() {
            // get a page of answers for a single question from the REST API's paginated 'Questions Endpoint'
            let endpoint = `/api/questions/${this.slug}/answers/`;
            if (this.next) {
                endpoint = this.next;
            }
            this.loadingAnswers = true;
            apiService(endpoint).then(data => {
                this.answers.push(...data.results);
                this.loadingAnswers = false;
                if (data.next) {
                    this.next = data.next;
                } else {
                    this.next = null;
                }
            });
        },
        onSubmit() {
            // Tell the REST API to create a new answer for this question based on the user input, then update some data properties
            if (this.newAnswerBody) {
                let endpoint = `/api/questions/${this.slug}/answer/`;
                apiService(endpoint, "POST", { body: this.newAnswerBody }).then(
                    data => {
                        this.answers.unshift(data);
                    }
                );
                this.newAnswerBody = null;
                this.showForm = false;
                this.userHasAnswered = true;
                if (this.error) {
                    this.error = null;
                }
            } else {
                this.error = "You can't send an empty answer!";
            }
        },
        async deleteAnswer(answer) {
            // delete a given answer from the answers array and make a delete request to the REST API
            let endpoint = `/api/answers/${answer.id}/`;
            try {
                await apiService(endpoint, "DELETE");
                this.$delete(this.answers, this.answers.indexOf(answer));
                this.userHasAnswered = false;
            } catch (err) {
                console.log(err);
            }
        }
    },
    created() {
        this.getQuestionData();
        this.getQuestionAnswers();
        this.setRequestUser();
    }
};
</script>

<style scoped>
.card {
    background-color: white;
    border: 0px;
}
.card-title {
    color: #111;
}
.card-body {
    color: #111;
}
.author-name {
    font-weight: bold;
    color: #1b5299;
    text-transform: capitalize;
}
.answer-added {
    font-weight: bold;
    color: #99231b;
}
textarea {
    border-radius: 10px;
    border: 2px solid #111;
}
textarea:focus {
    outline: none;
}
.error {
    font-weight: bold;
    color: red;
}
</style>