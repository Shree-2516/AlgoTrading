import { useEffect, useState } from "react";
import OrderForm from "../components/OrderForm";
import Positions from "../components/Positions";
import { getPositions as fetchPositions } from "../api";

export default function Trading() {
  const [positions, setPositions] = useState([]);

  const getPositions = async () => {
    try {
      const res = await fetchPositions();
      setPositions(res.data);
    } catch {
      console.log("Error fetching positions");
    }
  };

  useEffect(() => {
    getPositions();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Trading Terminal</h2>

      <OrderForm onOrderPlaced={getPositions} />

      <hr />

      <Positions positions={positions} />
    </div>
  );
}
