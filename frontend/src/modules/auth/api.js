import API from "../../shared/utils/apiClient";


export function login(credentials) {
  return API.post("/auth/login", credentials);
}


export function loginWithGoogle(token) {
  return API.post("/auth/google", { token });
}


export function registerUser(payload) {
  return API.post("/auth/register", payload);
}
