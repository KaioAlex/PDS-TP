<template>
  <div class="footer">
    <div class="container">
      <div class="footer-logo">
        <img src="@/assets/images/logo.png" alt="Logo" />
      </div>
      <div class="footer-social">
        <a href="#"
          ><img src="@/assets/images/facebook-icon.png" alt="Facebook"
        /></a>
        <a href="#"
          ><img src="@/assets/images/insta-icon.png" alt="Instagram"
        /></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FooterVue",
};
</script>

<style lang="scss" scoped>
.footer {
  position: relative;
  background: var(--color-background-footer);
  padding-top: 33px;
  .container {
    justify-content: space-between;
    .footer-social {
      display: flex;
      gap: 12px;
    }
  }
}
</style>
