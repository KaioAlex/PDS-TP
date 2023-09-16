<script setup>
import LoginForm from "@/components/auth/LoginForm.vue";
</script>

<template>
  <main>
    <LoginForm />
  </main>
</template>

<style lang="scss" scoped>
main {
  background: url(@/assets/images/auth/auth-bg.png) no-repeat;
  background-size: cover;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
