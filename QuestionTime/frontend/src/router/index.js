import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Question from "../views/Question.vue";
import QuestionEditor from "../views/QuestionEditor.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/ask",
    name: "QuestionEditor",
    component: QuestionEditor
  },
  {
    path: "/question/:slug",
    name: "Question",
    component: Question,
    props: true
  },

];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
