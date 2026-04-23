import { useEffect } from "react";

import { useBrokerStore } from "../../shared/state/useBrokerStore";

export function useBrokers() {
  const brokers = useBrokerStore((state) => state.brokers);
  const loading = useBrokerStore((state) => state.loading);
  const fetchBrokers = useBrokerStore((state) => state.fetchBrokers);
  const createBroker = useBrokerStore((state) => state.createBroker);
  const verifyBroker = useBrokerStore((state) => state.verifyBroker);
  const toggleBroker = useBrokerStore((state) => state.toggleBroker);
  const selectBroker = useBrokerStore((state) => state.selectBroker);

  useEffect(() => {
    fetchBrokers();
  }, [fetchBrokers]);

  return {
    brokers,
    loading,
    createBroker,
    verifyBroker,
    toggleBroker,
    selectBroker,
  };
}
