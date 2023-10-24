<template>
  <div class="profile">
    <div class="profile-header">
      <div class="profile-icon-circle">
        <img
          src="@/assets/images/menu/profile-selected.png"
          class="profile-header__logo"
        />
      </div>
      <span class="profile-header__text">{{ `Oi ${user.name}!` }}</span>
    </div>
    <div class="profile-info">
      <div class="profile-info-section">
        <span class="profile-info-section__title">ID</span>
        <span class="profile-info-section__value">{{ user.id }}</span>
        <div class="profile-info-section-actions">
          <img
            src="@/assets/images/icons/copy.png"
            class="profile-info-section__image"
            alt="Copy"
          />
        </div>
      </div>
      <div class="profile-info-section">
        <span class="profile-info-section__title">Username</span>
        <span class="profile-info-section__value">{{ user.username }}</span>
        <div class="profile-info-section-actions">
          <img
            src="@/assets/images/icons/edit.png"
            class="profile-info-section__image"
            alt="Edit"
          />
          <img
            src="@/assets/images/icons/copy.png"
            class="profile-info-section__image"
            alt="Copy"
          />
        </div>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script>
export default {
  name: "ProfilePage",
  data() {
    return {
      user: {
        name: "Fulano",
        id: "123456",
        username: "fulano123",
      },
    };
  },
};
</script>

<style lang="scss" scoped>
.profile {
  width: 100%;
  height: 100vh;
  padding: 157px 157px 79px 0;
  background-color: var(--color-background-dashboard);
  display: flex;
  flex-direction: column;
  gap: 24px;
  .profile-header {
    display: flex;
    align-items: center;
    gap: 24px;
    background-color: var(--color-background-cards);
    box-shadow: 1px 1px 20px 1px rgba(0, 0, 0, 0.09);
    border-radius: 15px;
    padding: 42px 25px;
    .profile-icon-circle {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 80px;
      height: 80px;
      border-radius: 85.106px;
      background: #2e2e2e;
      .profile-header__logo {
        width: 53px;
        height: 53px;
      }
    }
    .profile-header__text {
      color: #fcfcfc;
      font-size: 30px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
    }
  }
  .profile-info {
    display: flex;
    flex-direction: column;
    gap: 40px;
    padding: 53px 52px;
    background-color: var(--color-background-cards);
    box-shadow: 1px 1px 20px 1px rgba(0, 0, 0, 0.09);
    border-radius: 15px;
    .profile-info-section {
      display: flex;
      justify-content: space-between;
      align-items: center;
      .profile-info-section__title {
        color: var(--color-title-card);
        font-size: 30px;
        font-style: normal;
        font-weight: 500;
        line-height: normal;
        width: 300px;
      }
      .profile-info-section__value {
        color: #d9d9d9;
        font-size: 23px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        width: 80%;
      }
      .profile-info-section-actions {
        display: flex;
        gap: 24px;
        min-width: 84px;
        justify-content: flex-end;
        .profile-info-section__image {
          width: 30px;
          height: 30px;
          cursor: pointer;
        }
      }
    }
  }
}
</style>
