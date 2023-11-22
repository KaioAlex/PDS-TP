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
    </div>
    <div class="add-card-img">
      <img src="@/assets/images/cards/create-card.png" alt="Cards" />
    </div>
    <div class="card-form">
      <label class="card-form__label" for="num_card">Número do cartão</label>
      <input
        v-model="form.num_card"
        class="card-form__input num_card"
        type="text"
        name="num_card"
        v-maska="'#### #### #### ####'"
        placeholder="Número do cartão"
      />
      <label class="card-form__label" for="username">Nome no cartão</label>
      <input
        v-model="form.username"
        class="card-form__input username"
        type="text"
        name="username"
        placeholder="Nome no cartão"
      />
      <div class="card-form-side-inputs">
        <div class="card-form-input-block">
          <label class="card-form__label" for="card_validity"
            >Data de vencimento</label
          >
          <input
            v-model="form.card_validity"
            class="card-form__input card_validity"
            type="date"
            name="card_validity"
            v-maska="'##/##'"
            placeholder="Data de vencimento"
          />
        </div>
        <div class="card-form-input-block">
          <label class="card-form__label" for="security_code"
            >Código de segurança</label
          >
          <input
            v-model="form.security_code"
            class="card-form__input security_code"
            type="text"
            name="security_code"
            maxlength="3"
            placeholder="Código de segurança"
          />
        </div>
      </div>
      <div
        class="add-card-header-btn app-btn app-btn-primary"
        @click="createNewCard"
      >
        Adicionar Cartão
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "CardForm",
  data: function () {
    return {
      form: {
        id_user: this.$store.getters.getUserId,
        num_card: "",
        username: "",
        card_validity: "",
        security_code: "",
      },
    };
  },
  computed: {
    ...mapGetters(),
    userId() {
      return this.$store.state.user.id;
    },
  },
  methods: {
    createNewCard() {
      const date = this.form.card_validity.split("/");
      this.form.card_validity = date.reverse().join("-");

      this.$store.dispatch("addCard", this.form).then((success) => {
        if (success) {
          this.$emit("close");
          this.$notify({
            title: "Card created",
            text: "Your card has been created!",
            type: "success",
          });
        } else {
          this.$notify({
            title: "Card error",
            text: "Something went wrong, please try again",
            type: "error",
          });
        }
      });
    },
  },
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
    .add-card-header-btn {
      padding: 17px;
      margin-top: 20px;
      cursor: pointer;
    }
  }
}
</style>
