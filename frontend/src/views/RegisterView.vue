<script setup>
import RegisterForm from "@/components/auth/RegisterForm.vue";
</script>

<template>
  <main>
    <RegisterForm />
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
