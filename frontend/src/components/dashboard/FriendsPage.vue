<template>
  <div class="friends">
    <div class="friends-list" v-if="!showForm">
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
        <div
          class="friend__actions app-btn app-btn-alert"
          @click="removeFriend(friend.id)"
        >
          Remove
        </div>
      </div>
    </div>
    <div class="friends-form" v-else>
      <label class="friends-form__label" for="username"
        >ID ou nome de usuário</label
      >
      <input
        v-model="userStr"
        class="friends-form__input"
        type="text"
        name="username"
        placeholder="ID ou nome de usuário"
      />
    </div>
    <div
      class="friends-add__btn app-btn app-btn-primary"
      @click="!showForm ? form() : addFriend()"
    >
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
      friends: [],
      userStr: "",
      newFriend: {},
      showForm: false,
    };
  },
  methods: {
    form() {
      this.showForm = true;
    },
    listFriends() {
      this.$store
        .dispatch("getFriends", this.$store.getters.getUserId)
        .then((res) => {
          this.friends = res ?? [];
        });
    },
    removeFriend(id) {
      const body = {
        user_id1: this.$store.getters.getUserId,
        user_id2: id,
      };

      this.$store.dispatch("deleteFriend", body).then((success) => {
        if (success) {
          this.$notify({
            title: "Friend",
            text: "Your friend has been deleted!",
            type: "success",
          });
          this.listFriends();
        } else {
          this.$notify({
            title: "Friend",
            text: "Error removing friend, please try again",
            type: "error",
          });
        }
      });
    },
    findFriend() {
      this.$store.dispatch("getUserByUsername", this.userStr).then((res) => {
        this.newFriend = res ?? [];
        const body = {
          user_id1: this.$store.getters.getUserId,
          user_id2: this.newFriend.id,
        };

        this.$store.dispatch("addFriend", body).then((success) => {
          this.showForm = false;
          if (success) {
            this.listFriends();
            this.$notify({
              title: "Friend",
              text: "New friend has been added to your list!",
              type: "success",
            });
          } else {
            this.$notify({
              title: "Friend error",
              text: "Something went wrong, please try again",
              type: "error",
            });
          }
        });
      });
    },
    async addFriend() {
      await this.findFriend();
    },
  },
  mounted() {
    this.listFriends();
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
    overflow: scroll;
    &::-webkit-scrollbar {
      display: none;
    }
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
        background-color: var(--color-background-circle);
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
        cursor: pointer;
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
    margin-top: 24px;
    padding: 17px;
    cursor: pointer;
  }
  .friends-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    border-radius: 15px;
    background: var(--color-background-cards-dark);
    padding: 30px;
    .friends-form__label {
      color: var(--color-text-menu);
      font-size: 16px;
      font-style: normal;
      font-weight: 400;
      line-height: normal;
    }
    .friends-form__input {
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
}
</style>
