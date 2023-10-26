<template>
  <div class="add-card">
    <div class="add-card-header">
      <div class="add-card-header-back">
        <img
          class="add-card-header__close"
          src="@/assets/images/icons/arrow-back.png"
          alt="Back"
          @click="$emit('close')"
        />
        <h2 class="add-card-header__title">Adicionar Cartão</h2>
      </div>
      <div class="add-card-header-btn app-btn app-btn-primary">
        Adicionar Cartão
      </div>
    </div>
    <div class="add-card-img">
      <img src="@/assets/images/cards/create-card.png" alt="Cards" />
    </div>
    <div class="card-form">
      <label class="card-form__label" for="password">Número do cartão</label>
      <input
        class="card-form__input"
        type="password"
        name="password"
        placeholder="Número do cartão"
      />
      <label class="card-form__label" for="password">Nome no cartão</label>
      <input
        class="card-form__input"
        type="password"
        name="password"
        placeholder="Nome no cartão"
      />
      <div class="card-form-side-inputs">
        <div class="card-form-input-block">
          <label class="card-form__label" for="password"
            >Data de vencimento</label
          >
          <input
            class="card-form__input"
            type="password"
            name="password"
            placeholder="Data de vencimento"
          />
        </div>
        <div class="card-form-input-block">
          <label class="card-form__label" for="password"
            >Código de segurança</label
          >
          <input
            class="card-form__input"
            type="password"
            name="password"
            placeholder="Código de segurança"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardForm",
  data: function () {
    return {};
  },
  props: {},
};
</script>

<style lang="scss" scoped>
.add-card {
  border-radius: 15px;
  background: var(--color-background-cards-dark);
  padding: 30px;
  .add-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 30px;
    &__close {
      width: 30px;
      height: 30px;
      margin-right: 10px;
      cursor: pointer;
    }
    &__title {
      color: var(--color-text-menu);
      text-align: center;
      font-size: 23px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
    }
    .add-card-header-back {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .add-card-header-btn {
      padding: 17px;
      cursor: pointer;
    }
  }
  .add-card-img {
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
    img {
      width: 100%;
      max-width: 300px;
    }
  }
  .card-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    .card-form__label {
      color: var(--color-text-menu);
      font-size: 16px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
    }
    .card-form__input {
      width: 100%;
      height: 50px;
      border-radius: 15px;
      border: none;
      padding: 0 20px;
      background: var(--color-background-gray-input);
      font-size: 16px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
      color: var(--color-text);
    }
    .card-form-side-inputs {
      display: flex;
      gap: 20px;
      .card-form-input-block {
        display: flex;
        flex-direction: column;
        width: 100%;
        gap: 20px;
      }
    }
  }
}
</style>
