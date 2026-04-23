import { useState } from "react";

export default function Navbar() {
  const [dark, setDark] = useState(false);

  const toggleTheme = () => {
    document.documentElement.classList.toggle("dark");
    setDark(!dark);
  };

  return (
    <div className="flex justify-between items-center p-4 bg-white dark:bg-gray-800 shadow">

      <h1 className="font-semibold">Dashboard</h1>

      <div className="flex items-center gap-4">

        {/* Dark Mode */}
        <button onClick={toggleTheme}>
          {dark ? "🌙" : "☀️"}
        </button>

        {/* Wallet (dummy) */}
        <div>💰 ₹10,000</div>

        {/* Account Dropdown */}
        <div className="relative group">
          <button>👤</button>

          <div className="absolute right-0 hidden group-hover:block bg-white dark:bg-gray-700 shadow p-2">
            <div className="p-2 cursor-pointer">Profile</div>
            <div className="p-2 cursor-pointer text-red-500">Logout</div>
          </div>
        </div>

      </div>
    </div>
  );
}