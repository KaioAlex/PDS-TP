<template>
  <div class="help-list">
    <div
      v-for="(topic, index) in topics"
      :key="index"
      class="help"
      :ref="`help-card-${index}`"
    >
      <div class="help-header">
        <span class="help__title">{{ topic.question }}</span>
        <img
          src="@/assets/images/icons/expand.png"
          alt="See Answer"
          class="help__icon expand"
          @click="toggleHelp(index)"
        />
        <img
          src="@/assets/images/icons/close.png"
          alt="See Answer"
          class="help__icon close"
          @click="toggleHelp(index)"
        />
      </div>
      <div class="help-answer">
        <span class="help__title">{{ topic.answer }}</span>
      </div>
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
  methods: {
    toggleHelp(index) {
      const helpCard = this.$refs[`help-card-${index}`][0];
      helpCard.classList.toggle("open");
    },
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
    flex-direction: column;
    gap: 11px;
    padding: 11px 40px 10px 73px;
    border-radius: 15px;
    background-color: var(--color-background-cards);
    box-shadow: 1px 1px 20px 1px var(--color-shadow-2);
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
      cursor: pointer;
    }
    .help-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin: 35px 0;
    }
    .help-answer {
      display: none;
    }
    .expand {
      display: block;
    }
    .close {
      display: none;
    }
    &.open {
      .help-answer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: 0 0 35px;
      }
      .expand {
        display: none;
      }
      .close {
        display: block;
      }
    }
  }
}
</style>
