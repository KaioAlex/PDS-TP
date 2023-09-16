<template>
  <div class="container">
    <div class="login">
      <img
        src="@/assets/images/auth/login-icon.svg"
        class="login__icon"
        alt="Login Icon"
      />
      <h2 class="login__title">Bem Vindo!</h2>
      <p class="login__subtitle">Insira seus dados para realizar o login</p>
      <label class="login__label" for="username" v-if="showLoginLabel"
        >Username</label
      >
      <input
        class="login__input"
        type="text"
        name="username"
        placeholder="Username"
      />
      <label class="login__label" for="password" v-if="showLoginPassword"
        >Senha</label
      >
      <input
        class="login__input"
        type="password"
        name="password"
        placeholder="Senha"
      />
      <button class="login__btn btn btn-primary">Login</button>
      <a class="login__link" href="#">Esqueceu sua senha?</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  data: function () {
    return {
      showLoginLabel: false,
      showLoginPassword: false,
    };
  },
};
</script>

<style lang="scss" scoped>
.login {
  width: 579px;
  height: 687px;
  border-radius: 30px;
  padding: 28px 44px;
  background: var(--color-background-form);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  .login__icon {
    margin-bottom: 31px;
  }
  .login__title {
    color: var(--color-text-primary);
    font-size: 25px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
    margin-bottom: 14px;
  }
  .login__subtitle {
    color: var(--color-text-gray);
    text-align: center;
    font-size: 17px;
    font-style: normal;
    font-weight: 400;
    line-height: 135%;
    margin-bottom: 66px;
  }
  .login__label {
    color: var(--color-text-gray);
    text-align: left;
    font-size: 17px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }
  .login__input {
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
  .login__btn {
    margin-top: 47px;
    width: 100%;
    border: none;
    border-radius: 15px;

    font-size: 17px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;

    margin-bottom: 44px;
  }
  .login__link {
    color: var(--color-text-primary);
    font-size: 15px;
    font-style: normal;
    font-weight: 400;
    line-height: 135%;
    text-decoration-line: underline;
  }
}
</style>
