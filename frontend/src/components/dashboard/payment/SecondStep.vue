<template>
  <div class="second-step">
    <div class="second-step-amount">
      <input
        ref="inputRef"
        type="text"
        placeholder="$ 0,00"
        class="second-step-amount__value"
        :value="amount"
        @change="amount = $event"
      />
      <span class="second-step-amount__balance">$1.232 disponível.</span>
    </div>
    <div class="second-step-values">
      <div class="second-step-values__btn" @click="setAmount(500)">$500</div>
      <div class="second-step-values__btn" @click="setAmount(1000)">$1.000</div>
      <div class="second-step-values__btn" @click="setAmount(1500)">$1.500</div>
    </div>
    <div class="second-step-btn app-btn app-btn-primary" @click="$emit('next')">
      Continuar
    </div>
  </div>
</template>

<script>
import { useCurrencyInput } from "vue-currency-input";

export default {
  name: "SecondStep",
  data: function () {
    return {
      amount: null,
    };
  },
  setup() {
    const { inputRef, setValue } = useCurrencyInput({ currency: "BRL" });

    function setAmount(value) {
      setValue(value);
    }

    return { inputRef, setAmount };
  },
};
</script>

<style lang="scss" scoped>
.second-step {
  display: flex;
  flex-direction: column;
  gap: 20px;
  .second-step-amount {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin-bottom: 60px;
    .second-step-amount__value {
      font-size: 59px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
      color: var(--color-text);
      border: none;
      background: none;
      outline: none;
      text-align: center;
    }
    .second-step-amount__balance {
      font-size: 25px;
      font-style: normal;
      font-weight: 400;
      line-height: 135%;
      color: var(--color-text-menu);
    }
  }
  .second-step-values {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    .second-step-values__btn {
      width: 180px;
      height: 48px;
      padding: 8px 52px 9px 52px;
      border-radius: 500px;
      background: var(--color-payment-btn);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 25px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
      color: var(--color-text-gray);
      cursor: pointer;
      &:hover {
        background-color: var(--color-background-app-btn-primary);
        color: var(--color-text-primary);
      }
    }
  }
  .second-step-btn {
    display: flex;
    height: 67px;
    padding: 19px 0px 18px 0px;
    justify-content: center;
    align-items: center;
    border-radius: 15px;
    cursor: pointer;
  }
}
</style>
