import { createRouter, createWebHistory } from "vue-router";
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
      return import(/* webpackChunkName: "login" */ "../views/LoginView.vue");
    },
  },
  {
    path: "/register",
    name: "register",
    component: function () {
      return import(
        /* webpackChunkName: "register" */ "../views/RegisterView.vue"
      );
    },
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: function () {
      return import(
        /* webpackChunkName: "register" */ "../views/DashboardView.vue"
      );
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
