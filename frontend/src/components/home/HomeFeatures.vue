<template>
  <div class="container">
    <div class="features">
      <div class="feature">
        <img src="@/assets/images/home/features-mobile.png" />
        <div class="feature-content">
          <h2 class="feature-content__title">
            Realize seus pagamentos de forma fácil e rápida
          </h2>
          <p class="feature-content__text">
            Pague seus amigos pelo app, de forma fácil e rápida, sem perder o
            controle das divisões
          </p>
          <div class="feature-content-list">
            <div class="feature-content-list-item">
              <div class="feature-content-list-item-img">
                <img src="@/assets/images/home/icons/arrow-down-icon.svg" />
              </div>
              <span class="feature-content-list-item__text">
                Sem taxas na realização de pagamentos
              </span>
            </div>
            <div class="feature-content-list-item">
              <div class="feature-content-list-item-img">
                <img src="@/assets/images/home/icons/ray-icon.svg" />
              </div>
              <span class="feature-content-list-item__text">
                Transação rápida e segura
              </span>
            </div>
            <div class="feature-content-list-item">
              <div class="feature-content-list-item-img">
                <img src="@/assets/images/home/icons/locker-icon.svg" />
              </div>
              <span class="feature-content-list-item__text">
                Criptografia de ponta a ponta
              </span>
            </div>
          </div>
        </div>
      </div>
      <div class="features-shadow"></div>
      <div class="feature">
        <div class="feature-content">
          <h2 class="feature-content__title">
            Controle todos seus cartões em um único app
          </h2>
          <p class="feature-content__text">
            Controle facilitado e unificado de seus cartões
          </p>
          <div class="feature-content-list">
            <div class="feature-content-list-item">
              <div class="feature-content-list-item-img">
                <img src="@/assets/images/home/icons/shield-icon.svg" />
              </div>
              <span class="feature-content-list-item__text">
                Dados 100% privados
              </span>
            </div>
            <div class="feature-content-list-item">
              <div class="feature-content-list-item-img">
                <img src="@/assets/images/home/icons/message-icon.svg" />
              </div>
              <span class="feature-content-list-item__text">
                Suporte dedicado 24/7
              </span>
            </div>
          </div>
        </div>
        <div class="feature-image">
          <img src="@/assets/images/home/features-desk.png" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeFeatures",
};
</script>

<style lang="scss" scoped>
.features {
  display: flex;
  flex-direction: column;
  gap: 120px;
  position: relative;
  .features-shadow {
    width: 680px;
    height: 465px;
    background-color: var(--color-shadow);
    position: absolute;
    filter: blur(200px);
    left: -500px;
    bottom: 500px;
  }
  .feature {
    display: flex;
    gap: 167px;
    align-items: center;
    img {
      position: relative;
      z-index: 1;
    }
    .feature-image {
      margin-right: -390px;
    }
    .feature-content {
      .feature-content__title {
        font-size: 38px;
        font-style: normal;
        font-weight: 700;
        line-height: 55.02px;
        margin-bottom: 19px;
      }
      .feature-content__text {
        font-size: 18px;
        font-style: normal;
        font-weight: 400;
        line-height: 32.004px;
        margin-bottom: 32px;
      }
      .feature-content-list {
        display: flex;
        flex-direction: column;
        gap: 17px;
      }
      .feature-content-list-item {
        display: flex;
        gap: 17px;
        align-items: center;
        .feature-content-list-item-img {
          width: 46px;
          height: 46px;
          display: flex;
          padding: 7px;
          justify-content: center;
          align-items: center;
          border-radius: 13px;
          background-color: var(--color-background-green);
        }
        .feature-content-list-item__text {
          font-size: 18px;
          font-style: normal;
          font-weight: 400;
          line-height: 32.004px;
        }
      }
    }
  }
}
</style>
