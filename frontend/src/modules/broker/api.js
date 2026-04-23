import API from "../../shared/utils/apiClient";


export function getBrokers() {
  return API.get("/api/v1/broker/list");
}


export function addBroker(payload) {
  return API.post("/api/v1/broker/add", payload);
}


export function verifyBrokerConnection(id) {
  return API.post(`/api/v1/broker/verify/${id}`);
}


export function toggleBrokerStatus(id) {
  return API.post(`/api/v1/broker/toggle/${id}`);
}


export function selectActiveBroker(id) {
  return API.post(`/api/v1/broker/select/${id}`);
}
