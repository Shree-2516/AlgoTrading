import { useEffect } from "react";
import OrderForm from "../components/OrderForm";
import Positions from "../components/Positions";
import { useTradeStore } from "../../../shared/state/useTradeStore";

export default function Trading() {
  const positions = useTradeStore((state) => state.positions);
  const getPositions = useTradeStore((state) => state.fetchPositions);

  useEffect(() => {
    getPositions();
  }, [getPositions]);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Trading Terminal</h2>

      <OrderForm onOrderPlaced={getPositions} />

      <hr />

      <Positions positions={positions} />
    </div>
  );
}
