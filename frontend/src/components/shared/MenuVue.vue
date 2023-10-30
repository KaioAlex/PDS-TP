<template>
  <div class="menu">
    <div class="menu-links">
      <RouterLink class="menu-link" to="/dashboard">
        <img
          v-if="selectedMenu == 'dashboard'"
          src="@/assets/images/menu/home-selected.png"
          class="header__logo"
        />
        <img v-else src="@/assets/images/menu/home.png" class="header__logo" />
        <span
          class="menu-link__label"
          :class="selectedMenu == 'dashboard' ? 'selected' : ''"
        >
          Início
        </span>
      </RouterLink>
      <RouterLink class="menu-link" to="/dashboard/profile">
        <img
          v-if="selectedMenu == 'profile'"
          src="@/assets/images/menu/profile-selected.png"
          class="header__logo"
        />
        <img
          v-else
          src="@/assets/images/menu/profile.png"
          class="header__logo"
        />
        <span
          class="menu-link__label"
          :class="selectedMenu == 'profile' ? 'selected' : ''"
          >Meu Perfil</span
        >
      </RouterLink>
      <RouterLink class="menu-link" to="/dashboard/help">
        <img
          v-if="selectedMenu == 'help'"
          src="@/assets/images/menu/help-selected.png"
          class="header__logo"
        />
        <img v-else src="@/assets/images/menu/help.png" class="header__logo" />
        <span
          class="menu-link__label"
          :class="selectedMenu == 'help' ? 'selected' : ''"
          >Ajuda</span
        >
      </RouterLink>
      <RouterLink class="menu-link" to="/dashboard/friends">
        <img
          v-if="selectedMenu == 'friends'"
          src="@/assets/images/menu/friends-selected.png"
          class="header__logo"
        />
        <img
          v-else
          src="@/assets/images/menu/friends.png"
          class="header__logo"
        />
        <span
          class="menu-link__label"
          :class="selectedMenu == 'friends' ? 'selected' : ''"
          >Amigos</span
        >
      </RouterLink>
      <RouterLink class="menu-link" to="/dashboard/cards">
        <img
          v-if="selectedMenu == 'cards'"
          src="@/assets/images/menu/card-selected.png"
          class="header__logo"
        />
        <img v-else src="@/assets/images/menu/card.png" class="header__logo" />
        <span
          class="menu-link__label"
          :class="selectedMenu == 'cards' ? 'selected' : ''"
          >Cartões</span
        >
      </RouterLink>
    </div>
    <RouterLink class="menu-link" to="/" @click="loggout">
      <img src="@/assets/images/menu/logout.png" class="header__logo" />
      <span class="menu-link__label">Sair</span>
    </RouterLink>
  </div>
</template>

<script>
export default {
  name: "MenuVue",
  data() {
    return {
      selectedMenu: "dashboard",
    };
  },
  methods: {
    loggout() {
      this.$store.dispatch("loggout");
    },
  },
  mounted() {
    const path = window.location.pathname;

    if (path.includes("profile")) this.selectedMenu = "profile";
    else if (path.includes("help")) this.selectedMenu = "help";
    else if (path.includes("friends")) this.selectedMenu = "friends";
    else if (path.includes("cards")) this.selectedMenu = "cards";
    else this.selectedMenu = "dashboard";
  },
};
</script>

<style scoped lang="scss">
.menu {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: var(--color-background-dashboard);
  padding-top: 157px;
  width: 500px;
  height: 100vh;
  .menu-links {
    display: flex;
    flex-direction: column;
  }
  .menu-link {
    display: flex;
    align-items: center;
    padding: 24px 50px;
    gap: 24px;
    color: var(--color-text-menu);
    text-decoration: none;
    .menu-link__label {
      font-size: 25px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
      &.selected,
      &:hover {
        color: var(--color-text-primary);
      }
    }
  }
}
</style>
