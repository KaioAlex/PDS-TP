<template>
  <div class="cards">
    <div class="cards-header">
      <div class="cards-header__icon-circle">
        <img src="@/assets/images/cards/credit-card.png" alt="Cards" />
      </div>
      <span class="cards-header__title">Meus Cartões</span>
    </div>
    <div class="cards-list">
      <div
        v-for="(card, index) in cards"
        :key="index"
        class="card"
        :style="`background: linear-gradient(249deg, ${card.backgrondColor.from} 0%, ${card.backgrondColor.to} 100.65%)`"
      >
        <div class="card-info">
          <span class="card-info__numbers">.... {{ card.lastNumbers }}</span>
          <div class="card-info-brand">
            <img v-if="card.isVisa" src="@/assets/images/cards/Visa.png" />
            <img v-else src="@/assets/images/cards/MasterCard.png" />
            <span class="card-info__debit">Debit</span>
          </div>
        </div>
        <img src="@/assets/images/icons/delete.png" />
      </div>
    </div>
    <div class="cards-add__btn app-btn app-btn-primary">
      <img src="@/assets/images/icons/add.png" alt="Add" />
      Adicionar Cartão
    </div>
  </div>
</template>

<script>
export default {
  name: "CardsPage",
  data() {
    return {
      cards: [
        {
          lastNumbers: "1234",
          backgrondColor: {
            from: "#4BFF93",
            to: "#32A528",
          },
          isVisa: false,
        },
        {
          lastNumbers: "5678",
          backgrondColor: {
            from: "#FFB74B",
            to: "#A53E28",
          },
          isVisa: true,
        },
        {
          lastNumbers: "9012",
          backgrondColor: {
            from: "#4B7DFF",
            to: "#284AA5",
          },
          isVisa: true,
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.cards {
  width: 100%;
  height: 100vh;
  padding: 157px 157px 79px 0;
  background-color: var(--color-background-dashboard);
  display: flex;
  flex-direction: column;
  .cards-header {
    width: 100%;
    border-radius: 15px;
    background-color: #3d3d3d;
    display: flex;
    align-items: center;
    padding: 25px 43px;
    gap: 34px;
    margin-bottom: 24px;
    .cards-header__icon-circle {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background-color: #2e2e2e;
      display: flex;
      align-items: center;
      justify-content: center;
      img {
        width: 45px;
        height: 45px;
      }
    }
    .cards-header__title {
      color: var(--color-text);
      font-size: 30px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
    }
  }
  .cards-list {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 24px;
    overflow: scroll;
    &::-webkit-scrollbar {
      display: none;
    }
    .card {
      height: 165px;
      border-radius: 15px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      padding: 21px 26px;
      .card-info {
        display: flex;
        flex-direction: column;
        gap: 24px;
        justify-content: space-between;
        .card-info__numbers {
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 6px 17px 7px 17px;
          border-radius: 8px;
          background: rgba(61, 61, 61, 0.22);
          font-size: 22px;
          font-style: normal;
          font-weight: 700;
          line-height: 33px;
        }
        .card-info-brand {
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          .card-info__debit {
            font-size: 12px;
            font-style: normal;
            font-weight: 400;
            line-height: 35px;
          }
        }
      }
    }
  }
  .cards-add__btn {
    height: 79px;
    font-size: 30px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    gap: 29px;
    margin-top: 24px;
    padding: 17px;
  }
}
</style>
