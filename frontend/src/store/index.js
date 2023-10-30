import { createStore } from "vuex";
import axios from "axios";

const API_GATEWAY = "http://127.0.0.1:5000/api/";
const _user = "user/";
const _card = "card/";
const _transaction = "transaction/";

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
  },
  mutations: {},
  actions: {
    getUser(context, payload) {
      axios
        .get(`${API_GATEWAY}${_user}${payload}`, {
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
    getTransactions(context, payload) {
      axios
        .get(`${API_GATEWAY}${_transaction}${payload}`, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          debugger;
          if (res.status == 200) {
            return res.data;
          }
        })
        .catch((error) => {
          debugger;
          console.log(error);
        });
    },
    getCartoes(context, payload) {
      axios
        .get(`${API_GATEWAY}${_card}${payload}`, {
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
    addCard(context, payload) {
      axios
        .post(`${API_GATEWAY}${_card}`, payload, {
          "Access-Control-Allow-Origin": "*",
        })
        .then((res) => {
          debugger;
          if (res.status == 200) {
            return res.data;
          }
        })
        .catch((error) => {
          debugger;
          console.log(error);
        });
    },
  },
  modules: {},
});
