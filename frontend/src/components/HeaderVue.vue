<template>
  <div :class="isLogged ? 'header logged' : 'header'">
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
  data() {
    return {
      isLogged: true,
    };
  },
};
</script>

<style scoped lang="scss">
.header {
  position: absolute;
  top: 0;
  width: 100vw;
  padding: 33px 0;
  &.logged {
    background-color: var(--color-background-header);
    padding: 20px 0;
    .container {
      padding: 0 50px;
      max-width: none;
      .navbar {
        display: none;
      }
    }
  }
  .container {
    position: relative;
    .header__logo {
      cursor: pointer;
    }
    .navbar {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      width: 100%;
      padding-right: 20px;
      gap: 32px;
    }
  }
}

@media screen and (max-width: 820px) {
  .navbar {
    display: none;
  }
}
</style>
