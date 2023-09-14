<template>
  <div class="explore">
    <div class="container">
      <div class="explore-content">
        <h2 class="explore-content__title">
          Explore todas as possibilidades com SplitWallet
        </h2>
        <p class="explore-content__text">
          Experimente controlar suas finanças de maneira mais fácil e
          concentrada em apenas um app
        </p>
        <div class="explore-content__btn btn btn-alternative">
          <RouterLink to="/register">Cadastre-se agora</RouterLink>
        </div>
      </div>
      <img
        class="explore-content__img"
        src="@/assets/images/home/iphone-explore.png"
      />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.explore {
  background-color: var(--color-background-green);
  display: flex;
  margin-top: 370px;
  max-height: 511px;
  .container {
    .explore-content__img {
      margin-top: -78px;
      margin-right: -100px;
    }
    .explore-content {
      .explore-content__title {
        color: var(--color-text-dark);
        font-size: 38px;
        font-style: normal;
        font-weight: 700;
        line-height: 55.02px;
        margin-bottom: 16px;
      }
      .explore-content__text {
        color: var(--color-text-dark);
        font-size: 18px;
        font-style: normal;
        font-weight: 400;
        line-height: 32.004px;
        margin-bottom: 32px;
        max-width: 500px;
      }
      .explore-content__btn {
        max-width: 261px;
      }
    }
  }
}
</style>
