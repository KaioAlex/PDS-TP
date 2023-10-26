<template>
  <div class="conclusion">
    <h1 class="conclusion__title">Pronto!</h1>
    <h1 class="conclusion__title">Transferencia realizada com sucesso.</h1>
    <img class="conclusion__img" src="@/assets/images/payment/conclusion.png" />
    <div
      class="conclusion-btn app-btn app-btn-primary"
      @click="$router.push('/dashboard')"
    >
      Voltar para o inicio
    </div>
  </div>
</template>

<script>
export default {
  name: "ConclusionVue",
  data: function () {
    return {};
  },
  props: {},
};
</script>

<style lang="scss" scoped>
.conclusion {
  display: flex;
  flex-direction: column;
  align-items: center;
  .conclusion__title {
    color: var(--color-text-primary);
    font-size: 30px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    text-align: center;
  }
  .conclusion__img {
    width: 100%;
    height: 100%;
    max-width: 260px;
    max-height: 260px;
    margin: 46px 0;
  }
  .conclusion-btn {
    display: flex;
    width: 100%;
    height: 67px;
    padding: 19px 0px 18px 0px;
    justify-content: center;
    align-items: center;
    border-radius: 15px;
    cursor: pointer;
  }
}
</style>
