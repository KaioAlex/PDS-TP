<template>
  <div class="third-step">
    <h3 class="third-step__title">Valor</h3>
    <span class="third-step__value">$ 500,00</span>
    <h3 class="third-step__title">Para</h3>
    <p class="third-step__info">Julieta Carolina Sosa</p>
    <p class="third-step__info">Mercado Pago</p>
    <p class="third-step__info">ID 0000003100068949510855</p>
  </div>
  <div class="third-step-btn app-btn app-btn-primary" @click="$emit('next')">
    Realizar Transferencia
  </div>
</template>

<script>
export default {
  name: "FirstStep",
  data: function () {
    return {};
  },
  props: {},
};
</script>

<style lang="scss" scoped>
.third-step {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
  .third-step__title {
    color: var(--color-text-menu);
    font-size: 23px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }
  .third-step__value {
    font-size: 40px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    color: var(--color-text);
    margin-bottom: 43px;
  }
  .third-step__info {
    font-size: 23px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    color: var(--color-text);
  }
}
.third-step-btn {
  width: 100%;
  display: flex;
  height: 67px;
  padding: 19px 0px 18px 0px;
  justify-content: center;
  align-items: center;
  border-radius: 15px;
  margin-top: 59px;
  cursor: pointer;
}
</style>
