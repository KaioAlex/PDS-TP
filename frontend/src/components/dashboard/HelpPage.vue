<template>
  <div class="help-list">
    <div v-for="(topic, index) in topics" :key="index" class="help">
      <span class="help__title">{{ topic.question }}</span>
      <img
        src="@/assets/images/icons/expand.png"
        alt="See Answer"
        class="help__icon"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "HelpPage",
  data() {
    return {
      topics: [
        {
          question: "Como faço para criar uma conta?",
          answer:
            "Para criar uma conta, basta clicar no botão “Cadastre-se” na tela inicial do aplicativo e preencher os dados solicitados.",
        },
        {
          question: "Como faço para criar uma conta?",
          answer:
            "Para criar uma conta, basta clicar no botão “Cadastre-se” na tela inicial do aplicativo e preencher os dados solicitados.",
        },
        {
          question: "Como faço para criar uma conta?",
          answer:
            "Para criar uma conta, basta clicar no botão “Cadastre-se” na tela inicial do aplicativo e preencher os dados solicitados.",
        },
        {
          question: "Como faço para criar uma conta?",
          answer:
            "Para criar uma conta, basta clicar no botão “Cadastre-se” na tela inicial do aplicativo e preencher os dados solicitados.",
        },
        {
          question: "Como faço para criar uma conta?",
          answer:
            "Para criar uma conta, basta clicar no botão “Cadastre-se” na tela inicial do aplicativo e preencher os dados solicitados.",
        },
        {
          question: "Como faço para criar uma conta?",
          answer:
            "Para criar uma conta, basta clicar no botão “Cadastre-se” na tela inicial do aplicativo e preencher os dados solicitados.",
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.help-list {
  width: 100%;
  height: 100vh;
  padding: 157px 157px 79px 0;
  background-color: var(--color-background-dashboard);
  display: flex;
  flex-direction: column;
  gap: 42px;
  overflow: scroll;
  &::-webkit-scrollbar {
    display: none;
  }
  .help {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 11px;
    padding: 11px 40px 10px 73px;
    border-radius: 15px;
    background-color: var(--color-background-cards);
    box-shadow: 1px 1px 20px 1px rgba(0, 0, 0, 0.09);
    min-height: 131px;
    .help__title {
      font-size: 30px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
      color: var(--color-text);
    }
    .help__icon {
      width: 24px;
      height: 24px;
    }
  }
}
</style>
