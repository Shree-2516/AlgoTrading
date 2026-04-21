import { useEffect, useState } from "react";
import OrderForm from "../components/OrderForm";
import Positions from "../components/Positions";
import axios from "axios";

export default function Trading() {
  const [positions, setPositions] = useState([]);

  const getPositions = async () => {
    try {
      const res = await axios.get("http://localhost:8000/virtual/positions");
      setPositions(res.data);
    } catch (err) {
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