<script setup>
import { RouterView } from "vue-router";
import Header from "./components/HeaderVue.vue";
</script>

<template>
  <Header />
  <RouterView />
  <notifications position="bottom right" />
</template>
