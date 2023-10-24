<template>
  <div class="friends">
    <div class="friends-list">
      <div v-for="(friend, index) in friends" :key="index" class="friend">
        <div class="friend__icon-circle">
          <img
            src="@/assets/images/menu/profile.png"
            class="friend__icon"
            alt="User"
          />
        </div>
        <div class="friend__info">
          <span class="friend__name">{{ friend.name }}</span>
        </div>
        <div class="friend__actions app-btn app-btn-alert">Remove</div>
      </div>
    </div>
    <div class="friends-add__btn app-btn app-btn-primary">
      <img src="@/assets/images/icons/add.png" alt="Add" />
      Adicionar amigo
    </div>
  </div>
</template>

<script>
export default {
  name: "FriendsPage",
  data() {
    return {
      friends: [
        {
          name: "Fulano",
          username: "fulano123",
        },
        {
          name: "Ciclano",
          username: "ciclano456",
        },
        {
          name: "Beltrano",
          username: "beltrano789",
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.friends {
  width: 100%;
  height: 100vh;
  padding: 157px 157px 79px 0;
  background-color: var(--color-background-dashboard);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  .friends-list {
    display: flex;
    flex-direction: column;
    gap: 24px;
    .friend {
      display: flex;
      align-items: center;
      gap: 24px;
      padding: 24px 50px;
      background-color: var(--color-background-cards);
      border-radius: 8px;
      .friend__icon-circle {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background-color: #2e2e2e;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid var(--color-border);
        .friend__icon {
          width: 52px;
          height: 52px;
        }
      }
      .friend__info {
        display: flex;
        flex-direction: column;
        gap: 4px;
        width: 80%;
        .friend__name {
          font-size: 30px;
          font-style: normal;
          font-weight: 400;
          line-height: normal;
          color: var(--color-text);
        }
      }
      .friend__actions {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 10px 25px;
        font-size: 25px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
      }
    }
  }
  .friends-add__btn {
    height: 79px;
    font-size: 30px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    gap: 29px;
  }
}
</style>
