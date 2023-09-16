import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/login",
    name: "login",
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/LoginView.vue");
    },
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
