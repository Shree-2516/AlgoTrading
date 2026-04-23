import { create } from "zustand";

import { getPositions, placeOrder } from "../../modules/trading/api";

export const useTradeStore = create((set, get) => ({
  positions: [],
  loading: false,
  error: null,
  lastOrderMessage: "",

  fetchPositions: async () => {
    set({ loading: true, error: null });

    try {
      const res = await getPositions();
      set({ positions: res.data });
    } catch (err) {
      const error = err.response?.data?.detail || err.message;
      set({ error });
      console.error("Error fetching positions:", error);
    } finally {
      set({ loading: false });
    }
  },

  submitOrder: async (order) => {
    const res = await placeOrder(order);
    set({ lastOrderMessage: res.data.message || "Order submitted" });
    await get().fetchPositions();
    return res.data;
  },
}));
