import { createStore } from "vuex";
import axios from "axios";

const API_GATEWAY = "http://127.0.0.1:5000/api";
const _user = "/user";
const _card = "/card";
const _transaction = "/transaction";

export default createStore({
  state: {
    isLogged: false,
    user: {
      id: "",
      name: "",
      username: "",
      email: "",
      balance: "",
      score: "",
    },
  },
  getters: {
    getUser: function (state) {
      return state.user;
    },
    getUserId: function (state) {
      return state.user.id;
    },
    getBalance: function (state) {
      return state.user.balance;
    },
  },
  mutations: {
    setUser(state, payload) {
      const data = payload.users;
      if (data.id) {
        state.user = data;
      } else {
        state.user = {
          id: data[0],
          name: data[1],
          username: data[2],
          email: data[3],
          balance: data[5],
          score: data[6],
        };
      }
      state.isLogged = true;
    },
    loggout(state) {
      state.user = {
        id: "",
        name: "",
        username: "",
        email: "",
        balance: "",
        score: "",
      };
      state.isLogged = false;
    },
  },
  actions: {
    login(context, payload) {
      return axios
        .get(
          `${API_GATEWAY}${_user}/login/${payload.username}/${payload.password}`,
          {
            "Access-Control-Allow-Origin": "*",
          }
        )
        .then((res) => {
          if (res.status == 200) {
            context.commit("setUser", res.data);
            return true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    register(context, payload) {
      return axios
        .post(`${API_GATEWAY}${_user}`, payload, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          if (res.status == 200) {
            context.commit("setUser", res.data);
            return true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getUser(context, payload) {
      return axios
        .get(`${API_GATEWAY}${_user}/${payload}`, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          if (res.status == 200) {
            return res.data;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getUserByUsername(context, payload) {
      return axios
        .get(`${API_GATEWAY}${_user}/username/${payload}`, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          if (res.status == 200) {
            return res.data.user;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getTransactions(context, payload) {
      return axios
        .get(`${API_GATEWAY}${_transaction}/${payload}`, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          if (res.status == 200) {
            const transactions = res.data.transactions;
            const result = [];

            transactions.forEach((element) => {
              result.push({
                id: element[0],
                id_src: element[1],
                name: element[6],
                value: element[3],
                date: element[4],
                isDebit: this.state.user.id == element[2] ?? false,
              });
            });

            return result;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    newTransaction(context, payload) {
      return axios
        .post(`${API_GATEWAY}${_transaction}`, payload, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          if (res.status == 200) {
            return true;
          }
          return false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getCartoes(context, payload) {
      return axios
        .get(`${API_GATEWAY}${_card}/${payload}${_user}`, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          if (res.status == 200) {
            const cards = res.data.cards;
            const result = [];

            cards.forEach((element) => {
              result.push({
                id: element[0],
                id_user: element[1],
                username: element[2],
                num_card: element[3],
                lastNumbers: element[3].slice(-4),
                card_validity: element[4],
                security_code: element[5],
              });
            });

            return result;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addCard(context, payload) {
      return axios
        .post(`${API_GATEWAY}${_card}`, payload, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          if (res.status == 200) {
            return true;
          }
          return false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteCartoes(context, payload) {
      return axios
        .delete(`${API_GATEWAY}${_card}/${payload}`, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          if (res.status == 200) {
            return true;
          }
          return false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    loggout(context) {
      context.commit("loggout");
    },
  },
  modules: {},
});
