import { createStore } from "vuex";
import { auth } from "./auth.module.js";

const store = createStore({
  ...auth
});

export default store;