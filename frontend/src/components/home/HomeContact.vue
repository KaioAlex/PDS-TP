<template>
  <div class="container">
    <div class="contact">
      <h1 class="contact__title">Fale conosco</h1>
      <div class="contact-content">
        <div class="contact-left">
          <div class="contact-left-personal-info">
            <div class="contact-field">
              <label class="contact-field-label" for="name">Nome</label>
              <input
                class="contact-field-input"
                type="text"
                name="name"
                placeholder="Nome Completo"
              />
            </div>
            <div class="contact-field">
              <label class="contact-field-label" for="email">Email</label>
              <input
                class="contact-field-input"
                type="email"
                name="email"
                placeholder="email@exemple.com"
              />
            </div>
          </div>
          <div class="contact-field">
            <label class="contact-field-label" for="subject">Assunto</label>
            <input
              class="contact-field-input"
              type="text"
              name="subject"
              placeholder="Como podemos te ajudar?"
            />
          </div>
          <div class="contact-field">
            <label class="contact-field-label" for="message">Mensagem</label>
            <textarea
              class="contact-field-input textarea"
              name="message"
              cols="30"
              rows="10"
              placeholder="Digite sua mensagem aqui"
            ></textarea>
          </div>
          <button class="btn btn-primary">Enviar</button>
        </div>
        <div class="contact-right">
          <h3 class="contact-right__title">Emails para contato</h3>
          <div class="contact-right-list">
            <div
              class="contact-right-list-item"
              v-for="(feature, index) in getEmails"
              :key="index"
            >
              <div class="contact-right-list-item-img">
                <img src="@/assets/images/home/icons/mail-icon.svg" />
              </div>
              <span class="contact-right-list-item__text">{{ feature }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeFeatures",
  computed: {
    getEmails() {
      return [
        "contact@example.com",
        "support@example.com",
        "press@example.com",
      ];
    },
  },
};
</script>

<style lang="scss" scoped>
.contact {
  padding: 258px 0;
  .contact__title {
    font-size: 66px;
    font-style: normal;
    font-weight: 700;
    line-height: 79.992px;
    letter-spacing: -1px;
    margin-bottom: 52px;
  }
  .contact-content {
    display: flex;
    gap: 63px;
    .contact-left {
      width: 753px;
      .contact-left-personal-info {
        display: flex;
        gap: 25px;
      }
      .contact-field {
        display: flex;
        flex-direction: column;
        gap: 12px;
        width: 100%;
        margin-bottom: 32px;
        .contact-field-label {
          font-size: 18px;
          font-style: normal;
          font-weight: 700;
          line-height: 25px;
          letter-spacing: 0.9px;
          text-transform: uppercase;
        }
        .contact-field-input {
          padding: 20.5px 24px;
          align-items: flex-start;
          border-radius: 100px;
          border: 1px solid var(--color-background);
          background: var(--color-background-input);
          color: var(--color-text);
          &.textarea {
            border-radius: 14px;
          }
        }
      }
    }
    .contact-right {
      .contact-right__title {
        font-size: 22px;
        font-style: normal;
        font-weight: 700;
        line-height: 30px;
        letter-spacing: 0.22px;
        margin-bottom: 27px;
      }
      .contact-right-list {
        display: flex;
        flex-direction: column;
        gap: 24px;
        .contact-right-list-item {
          display: flex;
          gap: 17px;
          align-items: center;
          .contact-right-list-item-img {
            display: flex;
            width: 38px;
            padding: 10px 8px 9px 8px;
            justify-content: center;
            align-items: center;
            border-radius: 1000px;
            background: var(--color-background-green);
          }
          .contact-right-list-item__text {
            font-size: 18px;
            font-style: normal;
            font-weight: 500;
            line-height: 29px;
          }
        }
      }
    }
  }
}
</style>
