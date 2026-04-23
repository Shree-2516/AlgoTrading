import API from "../../shared/utils/apiClient";


export function getBrokers() {
  return API.get("/broker/list");
}


export function addBroker(payload) {
  return API.post("/broker/add", payload);
}


export function verifyBrokerConnection(id) {
  return API.post(`/broker/verify/${id}`);
}


export function toggleBrokerStatus(id) {
  return API.post(`/broker/toggle/${id}`);
}


export function selectActiveBroker(id) {
  return API.post(`/broker/select/${id}`);
}
