<template>
  <div class="header">
    <div class="container">
      <img
        src="@/assets/images/logo.png"
        class="header__logo"
        alt="Logo"
        @click="$router.push('/')"
      />
      <div class="navbar">
        <div class="btn btn-secondary">
          <RouterLink to="/login">Login</RouterLink>
        </div>
        <div class="btn btn-primary">
          <RouterLink to="/register">Cadastrar</RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HeaderVue",
};
</script>

<style scoped>
.header {
  position: absolute;
  top: 0;
  width: 100vw;
  padding: 33px 0;
}

.header__logo {
  cursor: pointer;
}

.container {
  position: relative;
}

.navbar {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  width: 100%;
  padding-right: 20px;
  gap: 56px;
}

@media screen and (max-width: 820px) {
  .navbar {
    display: none;
  }
}
</style>
