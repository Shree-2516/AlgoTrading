import { CheckCircle, Play, Square, Trash2 } from "lucide-react";


export default function BrokerCard({
  broker,
  onVerify,
  onToggle,
  onSelect,
}) {
  return (
    <div
      className={`bg-white p-5 rounded-xl shadow flex flex-col gap-3 ${
        broker.is_selected ? "border-2 border-green-500" : ""
      }`}
    >
      <div className="flex justify-between items-center">
        <h4 className="font-bold uppercase">{broker.broker_name}</h4>

        {broker.is_connected ? (
          <span className="text-green-600 text-sm flex items-center gap-1">
            <CheckCircle size={16} /> Connected
          </span>
        ) : (
          <span className="text-red-500 text-sm">Not Connected</span>
        )}
      </div>

      <div className="text-sm">
        Status:{" "}
        <span className={broker.is_active ? "text-green-600" : "text-gray-500"}>
          {broker.is_active ? "Running" : "Stopped"}
        </span>
      </div>

      <div className="flex flex-wrap gap-2 mt-2">
        <button onClick={() => onVerify(broker.id)} className="text-blue-600 text-sm">
          Verify
        </button>

        <button
          onClick={() => onToggle(broker.id)}
          className="flex items-center gap-1 text-sm bg-gray-100 px-2 py-1 rounded"
          disabled={!broker.is_connected}
        >
          {broker.is_active ? <Square size={14} /> : <Play size={14} />}
          {broker.is_active ? "Stop" : "Start"}
        </button>

        <button
          onClick={() => onSelect(broker.id)}
          className={`px-2 py-1 text-sm rounded ${
            broker.is_selected ? "bg-green-600 text-white" : "bg-gray-200"
          }`}
        >
          {broker.is_selected ? "Active" : "Set Active"}
        </button>

        <button className="text-red-600 text-sm flex items-center gap-1">
          <Trash2 size={14} /> Delete
        </button>
      </div>
    </div>
  );
}
