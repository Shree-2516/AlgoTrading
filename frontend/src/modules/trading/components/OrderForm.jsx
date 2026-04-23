import { useState } from "react";
import { useTradeStore } from "../../../shared/state/useTradeStore";

export default function OrderForm({ onOrderPlaced }) {
  const submitOrder = useTradeStore((state) => state.submitOrder);
  const [order, setOrder] = useState({
    symbol: "BTCUSDT",
    side: "BUY",
    quantity: 1,
    price: 100,
  });

  const [message, setMessage] = useState("");

  const handlePlaceOrder = async () => {
    try {
      const result = await submitOrder(order);

      setMessage(result.message);
      onOrderPlaced?.();
    } catch (err) {
      setMessage(err.response?.data?.message || "Order failed");
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

      <button onClick={handlePlaceOrder}>Place Order</button>

      <p>{message}</p>
    </div>
  );
}
