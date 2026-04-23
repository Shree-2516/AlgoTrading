import { create } from "zustand";

import {
  addBroker,
  getBrokers,
  selectActiveBroker,
  toggleBrokerStatus,
  verifyBrokerConnection,
} from "../../modules/broker/api";

export const useBrokerStore = create((set, get) => ({
  brokers: [],
  loading: false,
  error: null,

  fetchBrokers: async () => {
    set({ loading: true, error: null });

    try {
      const res = await getBrokers();
      set({ brokers: res.data.data });
    } catch (err) {
      const error = err.response?.data?.message || err.message;
      set({ error });
      console.error("Fetch error:", err.response?.data || err.message);
    } finally {
      set({ loading: false });
    }
  },

  createBroker: async (payload) => {
    await addBroker(payload);
    await get().fetchBrokers();
  },

  verifyBroker: async (id) => {
    const res = await verifyBrokerConnection(id);
    await get().fetchBrokers();
    return res.data.data;
  },

  toggleBroker: async (id) => {
    await toggleBrokerStatus(id);
    await get().fetchBrokers();
  },

  selectBroker: async (id) => {
    await selectActiveBroker(id);
    await get().fetchBrokers();
  },
}));
