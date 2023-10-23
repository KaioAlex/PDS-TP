<script setup>
import Menu from "@/components/shared/MenuVue.vue";
import DashBoard from "@/components/dashboard/DashBoard.vue";
</script>

<template>
  <main class="dashboard">
    <Menu />
    <DashBoard />
  </main>
</template>

<style scoped>
.dashboard {
  display: flex;
}
</style>
