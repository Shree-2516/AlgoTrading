import API from "../../shared/utils/apiClient";


export function login(credentials) {
  return API.post("/api/v1/auth/login", credentials);
}


export function loginWithGoogle(token) {
  return API.post("/api/v1/auth/google", { token });
}


export function registerUser(payload) {
  return API.post("/api/v1/auth/register", payload);
}
