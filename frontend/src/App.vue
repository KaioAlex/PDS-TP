<script setup>
import { RouterView } from "vue-router";
import Header from "./components/HeaderVue.vue";
import Footer from "./components/FooterVue.vue";
</script>

<template>
  <Header />
  <RouterView />
  <Footer />
</template>
