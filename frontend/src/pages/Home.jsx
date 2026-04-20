import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    const token = localStorage.getItem("token");

    if (token) {
      navigate("/dashboard");   // already logged in
    } else {
      navigate("/login");       // not logged in
    }
  };

  return (
    <div className="text-center mt-20 space-y-16">

      {/* HERO */}
      <section>
        <h1 className="text-4xl font-bold mb-3">
          Build Your Trading Intelligence
        </h1>

        <p className="text-gray-600 mb-5">
          Analyze, Learn, Improve your strategy
        </p>

        <button
          onClick={handleGetStarted}
          className="bg-black text-white px-6 py-2 rounded hover:bg-gray-800"
        >
          Get Started
        </button>
      </section>

      {/* ABOUT */}
      <section id="about">
        <h2 className="text-2xl font-bold mb-2">How it works</h2>
        <p>1. Register → 2. Login → 3. Dashboard</p>
      </section>

      {/* CONTACT */}
      <section id="contact">
        <h2 className="text-2xl font-bold mb-2">Contact</h2>
        <p>Email: shreeyash2573@gmail.com</p>
      </section>

    </div>
  );
}