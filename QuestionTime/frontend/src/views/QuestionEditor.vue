<template>
    <div class="container mt-5">
        <h1 class="mb-2">Ask a Question</h1>
        <form @submit.prevent="onSubmit">
            <textarea
                v-model="question_body"
                class="form-control"
                placeholder="What do you want to ask?"
                rows="3"
            ></textarea>
            <br />
            <div class="text-end">
            <button type="submit" class="btn btn-lg btn-success ">Ask</button>
            </div>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
    name: "QuestionEditor",
    data() {
        return {
            question_body: null,
            error: null
        };
    },
    methods: {
        onSubmit() {
            if (!this.question_body) {
                this.error = "You can't send an empty question!";
            } else if (this.question_body.length > 240) {
                this.error =
                    "Ensure this field has no more than 240 characters!";
            } else {
                let endpoint = "/api/questions/";
                let method = "POST";
                if (this.slug !== undefined) {
                    endpoint += `${this.slug}/`;
                    method = "PUT";
                }
                apiService(endpoint, method, {
                    content: this.question_body
                }).then(question_data => {
                    this.$router.push({
                        name: "Question",
                        params: { slug: question_data.slug }
                    });
                });
            }
        }
    },
    created() {
        document.title = "Editor - QuestionTime";
    }
};
</script>

<style scoped>
textarea{
    border-radius: 10px;
    border: 2px solid #111;
    
}
.text-end{
    text-align: end !important;
}
</style>