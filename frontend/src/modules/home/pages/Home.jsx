import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    const token = localStorage.getItem("token");
    if (token) navigate("/dashboard");
    else navigate("/login");
  };

  return (
    <>
      {/* ✅ ONLY this navbar will show on home */}
      <div className="text-center">
        {/* HERO */}
        <section className="py-24 px-6 bg-gradient-to-b from-gray-100 to-white">
          <h1 className="text-5xl font-bold mb-4">
            Build Your Trading Intelligence
          </h1>

          <p className="text-lg text-gray-600 mb-4">
            AI-powered trading insights to improve your strategy
          </p>

          <p className="text-gray-500 mb-6">
            Analyze performance, manage risk, and make smarter decisions.
          </p>

          <div className="space-x-4">
            <button
              onClick={handleGetStarted}
              className="bg-black text-white px-6 py-3 rounded-lg hover:bg-gray-800"
            >
              Get Started
            </button>

            <button className="border px-6 py-3 rounded-lg hover:bg-gray-100">
              View Demo
            </button>
          </div>
        </section>


        {/* FEATURES */}
        <section id="features" className="py-20 px-6">
          <h2 className="text-3xl font-bold mb-10">What You Can Do</h2>

          <div className="grid md:grid-cols-4 gap-6">
            <div className="p-6 border rounded-xl shadow-sm">
              <h3 className="font-semibold text-lg mb-2">📈 Strategy Backtesting</h3>
              <p className="text-gray-600">Test strategies with historical data.</p>
            </div>

            <div className="p-6 border rounded-xl shadow-sm">
              <h3 className="font-semibold text-lg mb-2">🤖 AI Suggestions</h3>
              <p className="text-gray-600">Get smart trade insights.</p>
            </div>

            <div className="p-6 border rounded-xl shadow-sm">
              <h3 className="font-semibold text-lg mb-2">📊 Analytics</h3>
              <p className="text-gray-600">Track PnL, win rate, and performance.</p>
            </div>

            <div className="p-6 border rounded-xl shadow-sm">
              <h3 className="font-semibold text-lg mb-2">📉 Risk Management</h3>
              <p className="text-gray-600">Control losses and optimize capital.</p>
            </div>
          </div>
        </section>

        {/* DASHBOARD PREVIEW */}
        <section className="py-20 bg-gray-50 px-6">
          <h2 className="text-3xl font-bold mb-6">See Your Dashboard</h2>
          <p className="text-gray-600 mb-8">
            Visualize trades, analytics, and insights in one place.
          </p>

          <div className="max-w-4xl mx-auto border rounded-xl shadow-lg p-10 bg-white">
            <p className="text-gray-400">
              [ Dashboard Preview Image / Chart Placeholder ]
            </p>
          </div>
        </section>

        {/* HOW IT WORKS */}
        <section className="py-20 px-6">
          <h2 className="text-3xl font-bold mb-8">How It Works</h2>

          <div className="grid md:grid-cols-4 gap-6 text-left max-w-5xl mx-auto">
            <div>
              <h4 className="font-semibold">1. Create Account</h4>
              <p className="text-gray-600 text-sm">Sign up in seconds</p>
            </div>

            <div>
              <h4 className="font-semibold">2. Add Data</h4>
              <p className="text-gray-600 text-sm">Import or simulate trades</p>
            </div>

            <div>
              <h4 className="font-semibold">3. Analyze</h4>
              <p className="text-gray-600 text-sm">View performance metrics</p>
            </div>

            <div>
              <h4 className="font-semibold">4. Improve</h4>
              <p className="text-gray-600 text-sm">Optimize your strategy</p>
            </div>
          </div>
        </section>

        {/* TESTIMONIALS */}
        <section className="py-20 bg-gray-100 px-6">
          <h2 className="text-3xl font-bold mb-10">What Users Say</h2>

          <div className="grid md:grid-cols-3 gap-6">
            <div className="p-6 bg-white rounded-xl shadow">
              <p>“Improved my win rate by 30%!”</p>
            </div>

            <div className="p-6 bg-white rounded-xl shadow">
              <p>“Great tool for both beginners and pros.”</p>
            </div>

            <div className="p-6 bg-white rounded-xl shadow">
              <p>“Clean UI and powerful analytics.”</p>
            </div>
          </div>
        </section>

        {/* ABOUT */}
        <section id="about" className="py-20 px-6 max-w-3xl mx-auto">
          <h2 className="text-3xl font-bold mb-4">About ALGO</h2>
          <p className="text-gray-600">
            ALGO helps traders analyze performance and make smarter decisions using data and AI.
          </p>
        </section>

        {/* FEEDBACK */}
        <section className="py-20 bg-gray-50 px-6">
          <h2 className="text-3xl font-bold mb-6">Feedback</h2>

          <form className="max-w-xl mx-auto space-y-4">
            <input type="text" placeholder="Name" className="w-full p-3 border rounded" />
            <input type="email" placeholder="Email" className="w-full p-3 border rounded" />

            <select className="w-full p-3 border rounded">
              <option>Rating ⭐</option>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>

            <textarea placeholder="Your feedback..." className="w-full p-3 border rounded" />

            <button className="bg-black text-white px-6 py-2 rounded">
              Submit
            </button>
          </form>
        </section>

        {/* CONTACT */}
        <section id="contact" className="py-20 px-6">
          <h2 className="text-3xl font-bold mb-6">Contact</h2>

          <form className="max-w-xl mx-auto space-y-4">
            <input type="text" placeholder="Name" className="w-full p-3 border rounded" />
            <input type="email" placeholder="Email" className="w-full p-3 border rounded" />
            <textarea placeholder="Message" className="w-full p-3 border rounded" />

            <button className="bg-black text-white px-6 py-2 rounded">
              Send Message
            </button>
          </form>

          <p className="mt-6 text-gray-500">
            Email: shreeyash2573@gmail.com
          </p>
        </section>

        {/* CTA */}
        <section className="py-20 bg-black text-white">
          <h2 className="text-3xl font-bold mb-4">
            Start Improving Your Trading Today
          </h2>

          <button
            onClick={handleGetStarted}
            className="bg-white text-black px-6 py-3 rounded-lg"
          >
            Sign Up Free
          </button>
        </section>

        {/* FOOTER */}
        <footer className="py-6 text-gray-500 text-sm">
          © 2026 ALGO. All rights reserved.
        </footer>

      </div>
    </>
  );
}
