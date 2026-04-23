import API from "../../shared/utils/apiClient";


export function getPositions() {
  return API.get("/api/v1/virtual/positions");
}


export function placeOrder(order) {
  return API.post("/api/v1/virtual/order", order);
}
