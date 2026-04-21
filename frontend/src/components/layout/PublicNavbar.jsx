import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <nav className="flex justify-between items-center p-4 border-b">
      <h1 className="font-bold text-xl">ALGO</h1>

      <div className="space-x-4">
        {!token ? (
          <>
            <Link to="/">Home</Link>
            <Link to="/#about">About</Link>
            <Link to="/#contact">Contact</Link>
            <Link to="/login" className="bg-black text-white px-3 py-1 rounded">
              Get Started
            </Link>
          </>
        ) : (
          <>
            <Link to="/">Home</Link>
            <Link to="/dashboard">Dashboard</Link>
            <button onClick={handleLogout} className="text-red-500">
              Logout
            </button>
          </>
        )}
      </div>
    </nav>
  );
}