<template>
  <div class="first-step-form">
    <label class="first-step-form__label" for="username"
      >ID ou nome de usuário</label
    >
    <input
      v-model="user"
      class="first-step-form__input"
      type="text"
      name="username"
      placeholder="ID ou nome de usuário"
    />
  </div>
  <div
    class="first-step-btn app-btn app-btn-primary"
    @click="$emit('next', user)"
  >
    Continuar
  </div>
</template>

<script>
export default {
  name: "FirstStep",
  data: function () {
    return {
      user: "",
    };
  },
};
</script>

<style lang="scss" scoped>
.first-step-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 46px;
  .first-step-form__label {
    color: var(--color-text-menu);
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }
  .first-step-form__input {
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
}
.first-step-btn {
  display: flex;
  height: 67px;
  padding: 19px 0px 18px 0px;
  justify-content: center;
  align-items: center;
  border-radius: 15px;
  cursor: pointer;
}
</style>
