<template>
  <div class="dashboard">
    <div class="dashboard-left">
      <div class="dashboard-balance dashboard-block">
        <div class="dashboard-balance-header">
          <span class="dashboard-balance-header__label">Saldo</span>
          <div class="dashboard-balance-header__btn app-btn app-btn-primary">
            Meus Dados
          </div>
        </div>
        <span class="dashboard-balance__value">R$ 1.232</span>
      </div>
      <div class="dashboard-buttons">
        <div class="dashboard-buttons__btn app-btn app-btn-primary">
          Pagar Conta
        </div>
        <div class="dashboard-buttons__btn app-btn app-btn-alternative">
          Criar Despesa
        </div>
      </div>
      <div class="dashboard-cards dashboard-block">
        <span class="dashboard-cards__title">Cartões</span>
      </div>
      <div class="dashboard-news dashboard-block">
        <div class="dashboard-news-circle"></div>
        <div class="dashboard-news-circle-content">
          <div class="dashboard-news-tag">New</div>
          <span class="dashboard-news-message">Bem vindo ao SplitWallet!</span>
        </div>
      </div>
    </div>
    <div class="dashboard-right">
      <div class="dashboard-history dashboard-block"></div>
    </div>
  </div>
</template>

<script></script>

<style scoped lang="scss">
.dashboard {
  width: 100vw;
  height: 100vh;
  padding-top: 157px;
  background-color: var(--color-background-dashboard);
  .dashboard-left {
    display: flex;
    flex-direction: column;

    gap: 24px;
    .dashboard-block {
      padding: 20px 30px;
      background-color: var(--color-background-cards);
      border-radius: 18.039px;
    }
    .dashboard-balance {
      display: flex;
      flex-direction: column;
      width: 537px;
      .dashboard-balance-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        .dashboard-balance-header__label {
          color: var(--color-title-card);
          font-size: 18px;
          font-style: normal;
          font-weight: 400;
          line-height: normal;
        }
        .dashboard-balance-header__btn {
          padding: 9px 20px;
        }
      }
      .dashboard-balance__value {
        color: var(--color-text-card);
        font-size: 59.814px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        padding: 20px;
      }
    }
    .dashboard-buttons {
      display: flex;
      gap: 20px;
      .dashboard-buttons__btn {
        width: 50%;
        padding: 15px 0;
      }
    }
    .dashboard-cards {
      .dashboard-cards__title {
        color: var(--color-title-card);
        font-size: 18px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
      }
    }
    .dashboard-news {
      position: relative;
      overflow: hidden;
      .dashboard-news-circle {
        width: 270px;
        border-radius: 270px;
        background: #d9ffff;
        position: absolute;
        height: 250px;
        left: -70px;
        top: -50px;
        z-index: 0;
      }
      .dashboard-news-circle-content {
        position: relative;
        z-index: 1;
        max-width: 120px;
        display: flex;
        flex-direction: column;
        gap: 26px;
        .dashboard-news-tag {
          display: flex;
          padding: 5px;
          max-width: 100px;
          justify-content: center;
          align-items: center;

          border-radius: 7.428px;
          background: #4bffb3;

          color: #222;
          font-size: 14px;
          font-style: normal;
          font-weight: 600;
          line-height: normal;
        }
        .dashboard-news-message {
          color: #222;
          font-size: 18px;
          font-style: normal;
          font-weight: 600;
          line-height: normal;
        }
      }
    }
  }
}
</style>
