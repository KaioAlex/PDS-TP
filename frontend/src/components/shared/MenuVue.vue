<template>
  <div class="menu">
    <div class="menu-links">
      <RouterLink class="menu-link" to="/dashboard">
        <img
          src="@/assets/images/menu/home-selected.png"
          class="header__logo"
        />
        <span class="menu-link__label selected">Início</span>
      </RouterLink>
      <RouterLink class="menu-link" to="/profile">
        <img src="@/assets/images/menu/profile.png" class="header__logo" />
        <span class="menu-link__label">Meu Perfil</span>
      </RouterLink>
      <RouterLink class="menu-link" to="/help">
        <img src="@/assets/images/menu/help.png" class="header__logo" />
        <span class="menu-link__label">Ajuda</span>
      </RouterLink>
      <RouterLink class="menu-link" to="/friends">
        <img src="@/assets/images/menu/friends.png" class="header__logo" />
        <span class="menu-link__label">Amigos</span>
      </RouterLink>
      <RouterLink class="menu-link" to="/cards">
        <img src="@/assets/images/menu/card.png" class="header__logo" />
        <span class="menu-link__label">Cartões</span>
      </RouterLink>
    </div>
    <RouterLink class="menu-link" to="/logout">
      <img src="@/assets/images/menu/logout.png" class="header__logo" />
      <span class="menu-link__label">Sair</span>
    </RouterLink>
  </div>
</template>

<script>
export default {
  name: "MenuVue",
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
