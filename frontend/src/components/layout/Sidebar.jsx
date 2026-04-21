import { Link, useLocation } from "react-router-dom";

const menu = [
  { name: "Dashboard", path: "/dashboard" },
  { name: "Broker", path: "/broker" },
  { name: "News", path: "/news" },
  { name: "Historical Data", path: "/historical" },
  { name: "Strategy Templates", path: "/templates" },
  { name: "Create Strategy", path: "/create-strategy" },
  { name: "Saved Strategy", path: "/saved-strategy" },
  { name: "Backtest", path: "/backtest" },
  { name: "Reports", path: "/reports" },
  { name: "Subscription", path: "/subscription" },
  { name: "Account", path: "/account" },
];

export default function Sidebar() {
  const location = useLocation();

  return (
    <div className="w-64 bg-white dark:bg-gray-800 shadow-md">
      <h2 className="p-4 font-bold text-lg">ALGO</h2>

      {menu.map((item) => (
        <Link
          key={item.path}
          to={item.path}
          className={`block p-3 ${
            location.pathname === item.path
              ? "bg-blue-500 text-white"
              : "text-gray-700 dark:text-gray-300"
          }`}
        >
          {item.name}
        </Link>
      ))}
    </div>
  );
}