<template>
  <div class="container">
    <div class="register">
      <img
        src="@/assets/images/auth/register-icon.svg"
        class="register__icon"
        alt="Register Icon"
      />
      <h2 class="register__title">Realizar Cadastro</h2>
      <p class="register__subtitle">
        Informe seus dados para realizar seu cadastro.
      </p>
      <label class="register__label" for="name" v-if="showRegisterLabel"
        >Nome Completo</label
      >
      <input
        class="register__input"
        type="text"
        name="name"
        placeholder="Nome Completo"
      />
      <label class="register__label" for="email" v-if="showRegisterLabel"
        >E-mail</label
      >
      <input
        class="register__input"
        type="mail"
        name="email"
        placeholder="E-mail"
      />
      <label class="register__label" for="username" v-if="showRegisterLabel"
        >Username</label
      >
      <input
        class="register__input"
        type="text"
        name="username"
        placeholder="Username"
      />
      <label class="register__label" for="birthday" v-if="showRegisterLabel"
        >Data de Nascimento</label
      >
      <input
        class="register__input"
        type="date"
        name="birthday"
        placeholder="Data de Nascimento"
      />
      <label class="register__label" for="password" v-if="showRegisterPassword"
        >Senha</label
      >
      <input
        class="register__input"
        type="password"
        name="password"
        placeholder="Senha"
      />
      <label
        class="register__label"
        for="passwordConfirm"
        v-if="showRegisterPassword"
        >Confirme sua Senha</label
      >
      <input
        class="register__input"
        type="password"
        name="passwordConfirm"
        placeholder="Confirme sua Senha"
      />
      <button class="register__btn btn btn-primary">Register</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegisterForm",
  data: function () {
    return {
      showRegisterLabel: false,
      showRegisterPassword: false,
    };
  },
};
</script>

<style lang="scss" scoped>
.register {
  width: 579px;
  border-radius: 30px;
  padding: 28px 44px;
  background: var(--color-background-form);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  .register__icon {
    margin-bottom: 31px;
  }
  .register__title {
    color: var(--color-text-primary);
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    margin-bottom: 14px;
  }
  .register__subtitle {
    color: var(--color-text-gray);
    text-align: center;
    font-size: 17px;
    font-style: normal;
    font-weight: 400;
    line-height: 135%;
    margin-bottom: 66px;
  }
  .register__label {
    color: var(--color-text-gray);
    text-align: left;
    font-size: 17px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }
  .register__input {
    background-color: var(--color-background-gray-input);
    border-radius: 15px;
    border: none;
    height: 67px;

    color: var(--color-text-gray);
    font-size: 17px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;

    margin-bottom: 24px;
  }
  .register__btn {
    margin-top: 47px;
    width: 100%;
    border: none;
    border-radius: 15px;

    font-size: 17px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
  }
}
</style>
