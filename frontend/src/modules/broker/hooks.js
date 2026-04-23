import { useCallback, useEffect, useState } from "react";

import {
  addBroker,
  getBrokers,
  selectActiveBroker,
  toggleBrokerStatus,
  verifyBrokerConnection,
} from "./api";


export function useBrokers() {
  const [brokers, setBrokers] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchBrokers = useCallback(async () => {
    setLoading(true);
    try {
      const res = await getBrokers();
      setBrokers(res.data);
    } catch (err) {
      console.error("Fetch error:", err.response?.data || err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchBrokers();
  }, [fetchBrokers]);

  const createBroker = async (payload) => {
    await addBroker(payload);
    await fetchBrokers();
  };

  const verifyBroker = async (id) => {
    const res = await verifyBrokerConnection(id);
    await fetchBrokers();
    return res.data;
  };

  const toggleBroker = async (id) => {
    await toggleBrokerStatus(id);
    await fetchBrokers();
  };

  const selectBroker = async (id) => {
    await selectActiveBroker(id);
    await fetchBrokers();
  };

  return {
    brokers,
    loading,
    createBroker,
    verifyBroker,
    toggleBroker,
    selectBroker,
  };
}
