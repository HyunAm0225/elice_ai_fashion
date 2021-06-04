import { atom, selector } from "recoil";

export const idState = atom({
  key: "idState",
  default: "",
});

export const passwordState = atom({
  key: "passwordState",
  default: "",
});

export const passwordCheckState = atom({
  key: "passwordCheckState",
  default: "",
});

export const usernameState = atom({
  key: "usernameState",
  default: "",
});

export const toastState = atom({
  key: "toastState",
  default: false,
});
export const textState = atom({
  key: "textState",
  default: "",
});
export const severityState = atom({
  key: "severityState",
  default: "",
});

export const testState = atom({
  key: "testState",
  default: "test",
});
