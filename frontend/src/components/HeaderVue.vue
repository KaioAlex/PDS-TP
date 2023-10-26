<template>
  <div :class="isLogged ? 'header logged' : 'header'">
    <div class="container">
      <img
        src="@/assets/images/logo.png"
        class="header__logo"
        alt="Logo"
        @click="isLogged ? $router.push('/dashboard') : $router.push('/')"
      />
      <div class="navbar">
        <div class="btn btn-secondary">
          <RouterLink to="/login">Login</RouterLink>
        </div>
        <div class="btn btn-primary">
          <RouterLink to="/register">Cadastrar</RouterLink>
        </div>
      </div>
      <div class="notifications">
        <img
          src="@/assets/images/menu/notification.png"
          class="notifications__logo"
          alt="Notification"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HeaderVue",
  data() {
    return {
      isLogged: window.location.pathname.includes("dashboard") ? true : false,
    };
  },
  watch: {
    $route() {
      if (window.location.pathname.includes("dashboard")) {
        this.isLogged = true;
      } else {
        this.isLogged = false;
      }
    },
  },
};
</script>

<style scoped lang="scss">
.header {
  position: absolute;
  top: 0;
  width: 100vw;
  padding: 33px 0;
  z-index: 1000;
  &.logged {
    background-color: var(--color-background-header);
    padding: 20px 0;
    .container {
      padding: 0 50px;
      max-width: none;
      justify-content: space-between;
      .navbar {
        display: none;
      }
      .notifications {
        display: block;
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
    .notifications {
      display: none;
    }
  }
}

@media screen and (max-width: 820px) {
  .navbar {
    display: none;
  }
}
</style>
