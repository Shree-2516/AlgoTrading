import { useState } from "react";
import axios from "axios";

export default function OrderForm({ onOrderPlaced }) {
  const [order, setOrder] = useState({
    symbol: "BTCUSDT",
    side: "BUY",
    quantity: 1,
    price: 100,
  });

  const [message, setMessage] = useState("");

  const placeOrder = async () => {
    try {
      const res = await axios.post(
        "http://localhost:8000/virtual/order",
        order
      );

      setMessage(res.data.message);
      onOrderPlaced(); // refresh positions
    } catch (err) {
      setMessage(err.response?.data?.detail || "Order failed");
    }
  };

  return (
    <div>
      <h3>Place Order</h3>

      <input
        value={order.symbol}
        onChange={(e) =>
          setOrder({ ...order, symbol: e.target.value })
        }
        placeholder="Symbol"
      />

      <select
        value={order.side}
        onChange={(e) =>
          setOrder({ ...order, side: e.target.value })
        }
      >
        <option value="BUY">BUY</option>
        <option value="SELL">SELL</option>
      </select>

      <input
        type="number"
        value={order.quantity}
        onChange={(e) =>
          setOrder({ ...order, quantity: Number(e.target.value) })
        }
        placeholder="Qty"
      />

      <input
        type="number"
        value={order.price}
        onChange={(e) =>
          setOrder({ ...order, price: Number(e.target.value) })
        }
        placeholder="Price"
      />

      <button onClick={placeOrder}>Place Order</button>

      <p>{message}</p>
    </div>
  );
}