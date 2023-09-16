<template>
  <div class="container">
    <div class="home-banner">
      <div class="home-banner-left">
        <h1 class="home-banner-left__title">
          O futuro do controle de finanças está aqui
        </h1>
        <p class="home-banner-left__subtitle">
          Descubra como é fácil controlar suas contas com SplitWallet
        </p>
        <div class="home-banner-left__btn btn btn-primary">
          <RouterLink to="/register">Cadastre-se agora</RouterLink>
        </div>
      </div>
      <div class="home-banner-right">
        <img
          class="home-banner-right__img"
          src="@/assets/images/home/home-computer.png"
          alt="Imagem da Dashboard do App"
        />
      </div>
      <div class="home-banner-shadow shadow1"></div>
      <div class="home-banner-shadow shadow2"></div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.home-banner {
  margin-top: 170px;
  display: flex;
  padding: 100px 0;
  position: relative;
  .home-banner-left {
    display: flex;
    flex-direction: column;
    justify-content: center;
    .home-banner-left__title {
      font-size: 66px;
      font-style: normal;
      font-weight: 700;
      line-height: 79.992px;
      letter-spacing: -1px;
      margin-bottom: 25px;
    }
    .home-banner-left__subtitle {
      font-size: 18px;
      font-style: normal;
      font-weight: 400;
      line-height: 32.004px;
      margin-bottom: 52px;
    }
    .home-banner-left__btn {
      max-width: 280px;
    }
  }
  .home-banner-right {
    .home-banner-right__img {
      margin-right: -380px;
      position: relative;
      z-index: 1;
    }
  }
  .home-banner-shadow {
    background-color: var(--color-shadow);
    position: absolute;
    filter: blur(200px);
    &.shadow1 {
      width: 300px;
      height: 200px;
      right: -300px;
      bottom: 300px;
    }
    &.shadow2 {
      width: 500px;
      height: 400px;
      right: -100px;
      bottom: -200px;
    }
  }
}
</style>
