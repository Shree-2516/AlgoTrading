import API from "../../shared/utils/apiClient";


export function getPositions() {
  return API.get("/virtual/positions");
}


export function placeOrder(order) {
  return API.post("/virtual/order", order);
}
