import "./assets/css/main.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Maska from "maska";
import Notifications from "@kyvg/vue3-notification";

createApp(App)
  .use(store)
  .use(router)
  .use(Maska)
  .use(Notifications)
  .mount("#app");
