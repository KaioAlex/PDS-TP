<template>
  <div class="payment">
    <div class="payment-header">
      <div class="payment-header__icon-circle">
        <img src="@/assets/images/icons/green-transfer.png" alt="Back" />
      </div>
      <span class="payment-header__title">
        {{ getTitle }}
      </span>
    </div>
    <PaymentCard @back="prevStep">
      <FirstStep v-if="step == 1" @next="nextStep" />
      <SecondStep v-if="step == 2" @next="nextStep" />
      <ThirdStep v-if="step == 3" @next="nextStep" />
    </PaymentCard>
  </div>
</template>

<script>
import PaymentCard from "./payment/PaymentCard.vue";
import FirstStep from "./payment/FirstStep.vue";
import SecondStep from "./payment/SecondStep.vue";
import ThirdStep from "./payment/ThirdStep.vue";

export default {
  name: "CardsPage",
  components: {
    PaymentCard,
    FirstStep,
    SecondStep,
    ThirdStep,
  },
  data() {
    return {
      step: 2,
    };
  },
  computed: {
    getTitle() {
      if (this.step == 1) {
        return "Insira os dados do destinatário";
      } else if (this.step == 2) {
        return "Insira o valor que deseja transferir";
      }
      return "Confira os dados da trsnferencia";
    },
  },
  methods: {
    nextStep() {
      this.step++;
    },
    prevStep() {
      if (this.step == 1) {
        this.$router.push("/dashboard");
      }

      this.step--;
    },
  },
};
</script>

<style lang="scss" scoped>
.payment {
  width: 100%;
  height: 100vh;
  padding: 157px 157px 79px 0;
  background-color: var(--color-background-dashboard);
  display: flex;
  flex-direction: column;
  .payment-header {
    width: 100%;
    border-radius: 15px;
    background-color: var(--color-background-cards-dark);
    display: flex;
    align-items: center;
    padding: 25px 43px;
    gap: 34px;
    margin-bottom: 24px;
    .payment-header__icon-circle {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background-color: var(--color-background-header);
      display: flex;
      align-items: center;
      justify-content: center;
      img {
        width: 45px;
        height: 45px;
      }
    }
    .payment-header__title {
      color: var(--color-text);
      font-size: 30px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
    }
  }
}
</style>
