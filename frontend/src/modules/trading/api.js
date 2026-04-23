import api from "../../shared/utils/apiClient";


export function getPositions() {
  return api.get("/api/v1/virtual/positions");
}


export function placeOrder(order) {
  return api.post("/api/v1/virtual/order", order);
}
