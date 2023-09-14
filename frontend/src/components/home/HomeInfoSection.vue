<template>
  <div class="container">
    <div class="info-section">
      <h1 class="info-section__title">Conheça mais sobre o SplitWallet</h1>
      <p class="info-section__subtitle">
        A solução do seu controle financeiro, você encontra aqui!
      </p>
      <div class="info-section-cards">
        <div class="info-section-cards-side">
          <div class="info-section-card">
            <div class="info-section-card-img">
              <img
                src="@/assets/images/home/icons/arrow-icon.svg"
                alt="Arrow Icon"
              />
            </div>
            <p class="info-section-card-title">Pague e receba</p>
            <p class="info-section-card-text">
              Pague e receba de seus amigos a qualquer momento de maneira rápida
              e fácil
            </p>
          </div>
          <div class="info-section-card">
            <div class="info-section-card-img">
              <img
                src="@/assets/images/home/icons/wallet-icon.svg"
                alt="Wallet Icon"
              />
            </div>
            <p class="info-section-card-title">Carteira 100% segura</p>
            <p class="info-section-card-text">
              Controle seus cartões de maneira unificada e segura com o
              SplitWallet
            </p>
          </div>
        </div>
        <div class="info-section-cards-center">
          <p class="info-section-card-title">Use em qualquer lugar</p>
          <p class="info-section-card-text">
            Seja em casa ou na rua, acesse o app a qualquer momento para nunca
            perder controle de suas contas
          </p>
          <img
            src="@/assets/images/home/home-iphone.png"
            alt="Imagem da Dashboard do App Mobile"
          />
        </div>
        <div class="info-section-cards-side">
          <div class="info-section-card">
            <div class="info-section-card-img">
              <img
                src="@/assets/images/home/icons/person-icon.svg"
                alt="Person Icon"
              />
            </div>
            <p class="info-section-card-title">100% Gratuito</p>
            <p class="info-section-card-text">
              Crie sua conta e começe a utilizar o Splitwallt de forma 100%
              gratúita
            </p>
          </div>
          <div class="info-section-card">
            <div class="info-section-card-img">
              <img
                src="@/assets/images/home/icons/money-icon.svg"
                alt="Money Icon"
              />
            </div>
            <p class="info-section-card-title">Controle em tempo real</p>
            <p class="info-section-card-text">
              Tenha controle de suas finanças em tempo real
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeInfoSection",
};
</script>

<style lang="scss" scoped>
.info-section {
  margin: 160px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  .info-section__title {
    text-align: center;
    font-size: 42px;
    font-style: normal;
    font-weight: 700;
    line-height: 55.02px;
    margin-bottom: 31px;
  }
  .info-section__subtitle {
    text-align: center;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: 32.004px;
    margin-bottom: 96px;
  }
  .info-section-cards {
    display: flex;
    gap: 27px;
    .info-section-cards-side {
      display: flex;
      flex-direction: column;
      gap: 32px;
      .info-section-card {
        width: 325px;
        height: 295px;
        padding: 48px 24px;
        border-radius: 40px;
        background: var(--color-card);
        .info-section-card-img {
          display: inline-flex;
          padding: 14px 13px 13px 13px;
          justify-content: center;
          align-items: center;
          background-color: var(--color-background-green);
          border-radius: 20px;
          margin-bottom: 20px;
        }
        .info-section-card-title {
          font-size: 18px;
          font-style: normal;
          font-weight: 700;
          line-height: 25.992px;
          letter-spacing: 0.9px;
          text-transform: uppercase;
          margin-bottom: 7px;
        }
        .info-section-card-text {
          font-size: 16px;
          font-style: normal;
          font-weight: 400;
          line-height: 26px;
        }
      }
    }
    .info-section-cards-center {
      width: 477px;
      height: 622px;
      padding: 33px 44px 0;
      background-color: var(--color-background-green);
      border-radius: 40px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      .info-section-card-title {
        font-size: 20px;
        font-style: normal;
        font-weight: 700;
        line-height: 26px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 9px;
        color: var(--color-text-dark);
      }
      .info-section-card-text {
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        line-height: 26px;
        margin-bottom: 28px;
        color: var(--color-text-dark);
      }
    }
  }
}
</style>
