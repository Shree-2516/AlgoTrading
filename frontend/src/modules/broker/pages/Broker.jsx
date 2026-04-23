import AddBrokerForm from "../components/AddBrokerForm";
import BrokerCard from "../components/BrokerCard";
import { useBrokers } from "../hooks";


export default function Broker() {
  const {
    brokers,
    loading,
    createBroker,
    verifyBroker,
    toggleBroker,
    selectBroker,
  } = useBrokers();

  const handleVerify = async (id) => {
    try {
      const result = await verifyBroker(id);
      alert(result.connected ? "Connected" : "Failed");
    } catch (err) {
      console.error(err.response?.data || err.message);
    }
  };

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h2 className="text-2xl font-semibold mb-6">Broker Management</h2>

      <AddBrokerForm onSubmit={createBroker} />

      <h3 className="text-lg font-semibold mb-4">My Brokers</h3>

      {loading && <p className="text-sm text-gray-500">Loading brokers...</p>}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {brokers.map((broker) => (
          <BrokerCard
            key={broker.id}
            broker={broker}
            onVerify={handleVerify}
            onToggle={toggleBroker}
            onSelect={selectBroker}
          />
        ))}
      </div>
    </div>
  );
}
