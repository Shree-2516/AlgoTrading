import { useEffect, useState } from "react";
import axios from "axios";
import { Play, Square, Trash2, CheckCircle } from "lucide-react";

export default function Broker() {
  const [brokers, setBrokers] = useState([]);
  const [form, setForm] = useState({
    broker_name: "angel",
    broker_user_id: "",
    api_key: "",
    api_secret: "",
  });

  // =========================
  // FETCH BROKERS
  // =========================
  const fetchBrokers = async () => {
    try {
      const res = await axios.get("http://localhost:8000/broker/list");
      setBrokers(res.data);
    } catch (err) {
      console.error("Fetch error:", err.response?.data);
    }
  };

  useEffect(() => {
    fetchBrokers();
  }, []);

  // =========================
  // ADD BROKER
  // =========================
  const addBroker = async () => {
    try {
      await axios.post("http://localhost:8000/broker/add", form);
      fetchBrokers();

      // reset form
      setForm({
        broker_name: "angel",
        broker_user_id: "",
        api_key: "",
        api_secret: "",
      });

    } catch (err) {
      console.error(err.response?.data);
      alert(err.response?.data?.detail || "Failed to add broker");
    }
  };

  // =========================
  // VERIFY
  // =========================
  const verifyBroker = async (id) => {
    try {
      const res = await axios.post(
        `http://localhost:8000/broker/verify/${id}`
      );

      alert(res.data.connected ? "Connected ✅" : "Failed ❌");

      fetchBrokers();
    } catch (err) {
      console.error(err.response?.data);
    }
  };

  // =========================
  // TOGGLE
  // =========================
  const toggleBroker = async (id) => {
    try {
      await axios.post(`http://localhost:8000/broker/toggle/${id}`);
      fetchBrokers();
    } catch (err) {
      console.error(err.response?.data);
    }
  };

  // =========================
  // ⭐ SELECT ACTIVE BROKER
  // =========================
  const selectBroker = async (id) => {
    try {
      await axios.post(`http://localhost:8000/broker/select/${id}`);
      fetchBrokers();
    } catch (err) {
      console.error(err.response?.data);
    }
  };

  return (
    <div className="p-6 bg-gray-50 min-h-screen">

      {/* HEADER */}
      <h2 className="text-2xl font-semibold mb-6">Broker Management</h2>

      {/* ================= ADD BROKER ================= */}
      <div className="bg-white p-6 rounded-xl shadow mb-6">
        <h3 className="text-lg font-semibold mb-4">Add Broker</h3>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <select
            className="border p-2 rounded"
            value={form.broker_name}
            onChange={(e) =>
              setForm({ ...form, broker_name: e.target.value })
            }
          >
            <option value="angel">Angel</option>
            <option value="dhan">Dhan</option>
          </select>

          <input
            className="border p-2 rounded"
            placeholder="Broker ID"
            value={form.broker_user_id}
            onChange={(e) =>
              setForm({ ...form, broker_user_id: e.target.value })
            }
          />

          <input
            className="border p-2 rounded"
            placeholder="API Key"
            value={form.api_key}
            onChange={(e) =>
              setForm({ ...form, api_key: e.target.value })
            }
          />

          <input
            className="border p-2 rounded"
            placeholder="API Secret"
            value={form.api_secret}
            onChange={(e) =>
              setForm({ ...form, api_secret: e.target.value })
            }
          />
        </div>

        <button
          onClick={addBroker}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Add Broker
        </button>
      </div>

      {/* ================= BROKER LIST ================= */}
      <h3 className="text-lg font-semibold mb-4">My Brokers</h3>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {brokers.map((b) => (
          <div
            key={b.id}
            className={`bg-white p-5 rounded-xl shadow flex flex-col gap-3 
              ${b.is_selected ? "border-2 border-green-500" : ""}
            `}
          >
            <div className="flex justify-between items-center">
              <h4 className="font-bold uppercase">{b.broker_name}</h4>

              {b.is_connected ? (
                <span className="text-green-600 text-sm flex items-center gap-1">
                  <CheckCircle size={16} /> Connected
                </span>
              ) : (
                <span className="text-red-500 text-sm">Not Connected</span>
              )}
            </div>

            <div className="text-sm">
              Status:{" "}
              <span className={b.is_active ? "text-green-600" : "text-gray-500"}>
                {b.is_active ? "Running" : "Stopped"}
              </span>
            </div>

            {/* ACTIONS */}
            <div className="flex flex-wrap gap-2 mt-2">

              <button
                onClick={() => verifyBroker(b.id)}
                className="text-blue-600 text-sm"
              >
                Verify
              </button>

              <button
                onClick={() => toggleBroker(b.id)}
                className="flex items-center gap-1 text-sm bg-gray-100 px-2 py-1 rounded"
                disabled={!b.is_connected}
              >
                {b.is_active ? <Square size={14} /> : <Play size={14} />}
                {b.is_active ? "Stop" : "Start"}
              </button>

              {/* ⭐ SELECT BUTTON */}
              <button
                onClick={() => selectBroker(b.id)}
                className={`px-2 py-1 text-sm rounded ${
                  b.is_selected
                    ? "bg-green-600 text-white"
                    : "bg-gray-200"
                }`}
              >
                {b.is_selected ? "Active" : "Set Active"}
              </button>

              <button className="text-red-600 text-sm flex items-center gap-1">
                <Trash2 size={14} /> Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}