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
        <span class="dashboard-balance__value">
          {{ balance }}
        </span>
      </div>
      <div class="dashboard-buttons">
        <div
          class="dashboard-buttons__btn app-btn app-btn-primary"
          @click="$router.push('/dashboard/payment')"
        >
          Pagar Conta
        </div>
        <div class="dashboard-buttons__btn app-btn app-btn-alternative">
          Criar Despesa
        </div>
      </div>
      <div class="dashboard-cards dashboard-block">
        <span class="dashboard-cards__title">Cartões</span>
        <div class="dashboard-cards-soon">
          <span class="dashboard-cards-soon__label">Coming Soon!</span>
        </div>
      </div>
      <div class="dashboard-news dashboard-block">
        <div class="dashboard-news-circle"></div>
        <div class="dashboard-news-circle-content">
          <div class="dashboard-news-tag">New</div>
          <span class="dashboard-news-message">Bem vindo ao SplitWallet!</span>
        </div>
        <div class="dashboard-news-right">
          <div class="dashboard-icon-circle">
            <img src="@/assets/images/icons/green-transfer.png" />
          </div>
          <span class="dashboard-news-right__message">
            Comece agora a ter controle das duas finanças!
          </span>
        </div>
      </div>
    </div>
    <div class="dashboard-right">
      <div class="dashboard-history dashboard-block">
        <span class="dashboard-history__label">Extrato</span>
        <div class="dashboard-history-transactions" v-if="transactions.length">
          <div
            v-for="(transaction, index) in transactions"
            :key="index"
            class="dashboard-history-transaction"
          >
            <div class="dashboard-icon-circle">
              <img
                v-if="transaction.isDebit"
                src="@/assets/images/icons/money.svg"
              />
              <img v-else src="@/assets/images/icons/transfer.png" />
            </div>
            <div class="dashboard-history-transactions-left">
              <span class="dashboard-history-transactions-left__label">{{
                getLabel(transaction)
              }}</span>
              <span class="dashboard-history-transactions-info">{{
                getNameText(transaction)
              }}</span>
            </div>
            <div class="dashboard-history-transactions-right">
              <span
                class="dashboard-history-transactions-right__value"
                :class="transaction.isDebit ? 'debit' : 'credit'"
                >{{
                  transaction.value.toLocaleString("pt-br", {
                    style: "currency",
                    currency: "BRL",
                  })
                }}</span
              >
              <span class="dashboard-history-transactions-info">{{
                transaction.date.slice(0, 16)
              }}</span>
            </div>
          </div>
        </div>
        <div class="empty-dashboard" v-else>
          <h2>Nenhuma transação realizada!</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DashBoard",
  data() {
    return {
      transactions: [],
      balance: 0,
    };
  },
  methods: {
    getLabel(transaction) {
      return transaction.isDebit
        ? "Transferencia Recebida"
        : "Transferencia Feita";
    },
    getNameText(transaction) {
      const prefix = transaction.isDebit ? "De" : "Para";
      return `${prefix} ${transaction.name}`;
    },
    getBalance() {
      const res = this.$store.getters.getBalance;

      this.balance = res.toLocaleString("pt-br", {
        style: "currency",
        currency: "BRL",
      });
    },
  },
  mounted() {
    this.getBalance();
    this.$store
      .dispatch("getTransactions", this.$store.getters.getUserId)
      .then((res) => {
        this.transactions = res ?? [];
      });
  },
};
</script>

<style scoped lang="scss">
.dashboard {
  width: 100%;
  height: 100vh;
  padding: 157px 157px 79px 0;
  background-color: var(--color-background-dashboard);
  gap: 48px;
  display: flex;
  .dashboard-block {
    padding: 20px 30px;
    background-color: var(--color-background-cards);
    border-radius: 18.039px;
  }
  .dashboard-icon-circle {
    display: flex;
    width: 70.033px;
    height: 70.033px;
    padding: 19.1px;
    justify-content: center;
    align-items: center;
    border-radius: 486.343px;
    background: var(--color-background-circle);
  }
  .dashboard-left {
    display: flex;
    flex-direction: column;
    width: 50%;
    gap: 24px;
    .dashboard-balance {
      display: flex;
      flex-direction: column;
      width: 100%;
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
        cursor: pointer;
      }
    }
    .dashboard-cards {
      display: flex;
      flex-direction: column;

      height: 244px;
      .dashboard-cards__title {
        color: var(--color-title-card);
        font-size: 18px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
      }
      .dashboard-cards-soon {
        display: flex;
        height: 92px;
        width: 300px;
        justify-content: center;
        align-items: center;
        border-radius: 9px;
        background: var(--color-background-cards-dark);
        box-shadow: 15px 20px 20px 0.6px var(--color-shadow-black);
        margin: auto;
        .dashboard-cards-soon__label {
          color: var(--color-text-card);
          font-size: 28px;
          font-style: normal;
          font-weight: 400;
          line-height: normal;
        }
      }
    }
    .dashboard-news {
      position: relative;
      overflow: hidden;
      height: 188px;
      .dashboard-news-circle {
        width: 270px;
        border-radius: 270px;
        background: var(--vt-c-green-soft);
        position: absolute;
        height: 250px;
        left: -70px;
        top: -30px;
        z-index: 0;
      }
      .dashboard-news-circle-content {
        position: relative;
        z-index: 1;
        max-width: 120px;
        display: flex;
        flex-direction: column;
        gap: 26px;
        top: calc(50% - 60px);
        .dashboard-news-tag {
          display: flex;
          padding: 5px;
          max-width: 100px;
          justify-content: center;
          align-items: center;

          border-radius: 7.428px;
          background: var(--color-background-green);

          color: var(--color-text-dashboard);
          font-size: 14px;
          font-style: normal;
          font-weight: 600;
          line-height: normal;
        }
        .dashboard-news-message {
          color: var(--color-text-dashboard);
          font-size: 18px;
          font-style: normal;
          font-weight: 600;
          line-height: normal;
        }
      }
      .dashboard-news-right {
        display: inline-flex;
        height: 92px;
        justify-content: flex-end;
        align-items: center;
        border-radius: 9.106px;
        background: var(--color-background-cards-dark);
        position: absolute;
        right: -50px;
        top: calc(50% - 46px);
        padding: 0 60px 0 20px;
        box-shadow: 15px 20px 20px 0.60706px var(--color-shadow-black);
        gap: 21px;
        .dashboard-news-right__message {
          width: 198px;
        }
      }
    }
  }
  .dashboard-right {
    width: 50%;
    .dashboard-history {
      height: 100%;
      overflow: scroll;
      &::-webkit-scrollbar {
        display: none;
      }
      .dashboard-history__label {
        color: var(--color-title-card);
        font-size: 18px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
      }
      .empty-dashboard {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 50px;
      }
      .dashboard-history-transactions {
        margin-top: 22px;
        .dashboard-history-transaction {
          display: flex;
          gap: 14px;
          justify-content: space-between;
          align-items: center;
          height: 137.944px;
          .dashboard-history-transactions-left {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            width: 60%;
            .dashboard-history-transactions-left__label {
              color: var(--color-text-gray);
              font-size: 18px;
              font-style: normal;
              font-weight: 400;
              line-height: normal;
            }
          }
          .dashboard-history-transactions-right {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            .dashboard-history-transactions-right__value {
              font-size: 18px;
              font-style: normal;
              font-weight: 600;
              line-height: normal;
              &.debit {
                color: var(--color-text-primary);
              }
              &.credit {
                color: var(--color-text-credit);
              }
            }
          }
          .dashboard-history-transactions-info {
            color: var(--color-title-card);
            font-size: 16px;
            font-style: normal;
            font-weight: 400;
            line-height: normal;
          }
        }
      }
    }
  }
}
</style>
