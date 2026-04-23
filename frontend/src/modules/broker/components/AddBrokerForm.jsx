import { useState } from "react";


const initialForm = {
  broker_name: "angel",
  broker_user_id: "",
  api_key: "",
  api_secret: "",
};


export default function AddBrokerForm({ onSubmit }) {
  const [form, setForm] = useState(initialForm);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      await onSubmit(form);
      setForm(initialForm);
    } catch (err) {
      console.error(err.response?.data?.message || err.message);
      alert(err.response?.data?.message || "Failed to add broker");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-xl shadow mb-6">
      <h3 className="text-lg font-semibold mb-4">Add Broker</h3>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <select
          className="border p-2 rounded"
          value={form.broker_name}
          onChange={(e) => setForm({ ...form, broker_name: e.target.value })}
        >
          <option value="angel">Angel</option>
          <option value="dhan">Dhan</option>
        </select>

        <input
          className="border p-2 rounded"
          placeholder="Broker ID"
          value={form.broker_user_id}
          onChange={(e) => setForm({ ...form, broker_user_id: e.target.value })}
        />

        <input
          className="border p-2 rounded"
          placeholder="API Key"
          value={form.api_key}
          onChange={(e) => setForm({ ...form, api_key: e.target.value })}
        />

        <input
          className="border p-2 rounded"
          placeholder="API Secret"
          value={form.api_secret}
          onChange={(e) => setForm({ ...form, api_secret: e.target.value })}
        />
      </div>

      <button
        type="submit"
        className="mt-4 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Add Broker
      </button>
    </form>
  );
}
