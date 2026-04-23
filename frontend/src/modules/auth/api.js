import api from "../../shared/utils/apiClient";


export function login(credentials) {
  return api.post("/api/v1/auth/login", credentials);
}


export function loginWithGoogle(token) {
  return api.post("/api/v1/auth/google", { token });
}


export function registerUser(payload) {
  return api.post("/api/v1/auth/register", payload);
}
