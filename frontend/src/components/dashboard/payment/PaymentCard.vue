<template>
  <div class="payment-card">
    <div class="payment-card-header">
      <div class="payment-card-header-back">
        <img
          class="payment-card-header__close"
          src="@/assets/images/icons/arrow-back.png"
          alt="Back"
          @click="$emit('back')"
        />
      </div>
    </div>
    <slot />
  </div>
</template>

<script>
export default {
  name: "PaymentCard",
};
</script>

<style lang="scss" scoped>
.payment-card {
  border-radius: 15px;
  background: var(--color-background-cards-dark);
  padding: 30px;
  .payment-card-header {
    display: flex;
    align-items: center;
    margin-bottom: 30px;
    &__close {
      width: 30px;
      height: 30px;
      margin-right: 10px;
      cursor: pointer;
    }
    .payment-card-header-back {
      display: flex;
      align-items: center;
      gap: 10px;
    }
  }
}
</style>
