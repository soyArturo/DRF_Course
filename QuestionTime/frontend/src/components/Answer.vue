<template>
    <div class="card shadow mb-2">
        <div class="card-body">
            <p class="text-muted">
                <strong class="author-name">{{answer.author}}</strong>
                &#8901; {{answer.created_at}}
            </p>
            <p>{{answer.body}}</p>
            <div v-if="isAnswerAuthor">
                <button class="btn btn-sm btn-outline-secondary mx-1" >Edit</button>
                <button class="btn btn-sm btn-outline-danger" @click="triggerDeleteAnswer">Delete</button>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        },
        requestUser: {
            type: String,
            required: true
        }
    },
    computed: {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        }
    },
    methods: {
        toggleLike() {
            this.userLikedAnswer === false
                ? this.likeAnswer()
                : this.unLikeAnswer();
        },
        likeAnswer() {
            this.userLikedAnswer = true;
            this.likesCounter += 1;
            let endpoint = `/api/answers/${this.answer.id}/like/`;
            apiService(endpoint, "POST");
        },
        unLikeAnswer() {
            this.userLikedAnswer = false;
            this.likesCounter -= 1;
            let endpoint = `/api/answers/${this.answer.id}/like/`;
            apiService(endpoint, "DELETE");
        },
        triggerDeleteAnswer() {
            // emit an event to delete an answer instance
            this.$emit("delete-answer", this.answer);
        }
    }
};
</script>

<style scoped>
.card {
    background-color: white;
    border: 0px;
}
.card-body {
    color: #111;
}
.author-name {
    text-transform: capitalize;
}
</style>