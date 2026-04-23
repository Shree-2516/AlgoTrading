import api from "../../shared/utils/apiClient";


export function getBrokers() {
  return api.get("/api/v1/broker/list");
}


export function addBroker(payload) {
  return api.post("/api/v1/broker/add", payload);
}


export function verifyBrokerConnection(id) {
  return api.post(`/api/v1/broker/verify/${id}`);
}


export function toggleBrokerStatus(id) {
  return api.post(`/api/v1/broker/toggle/${id}`);
}


export function selectActiveBroker(id) {
  return api.post(`/api/v1/broker/select/${id}`);
}
