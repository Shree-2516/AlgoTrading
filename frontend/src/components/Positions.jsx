export default function Positions({ positions }) {
  return (
    <div>
      <h3>Positions</h3>

      {positions.length === 0 ? (
        <p>No positions</p>
      ) : (
        positions.map((p, index) => (
          <div key={index}>
            <strong>{p.symbol}</strong> | Qty: {p.quantity} | Avg: {p.avg_price}
          </div>
        ))
      )}
    </div>
  );
}