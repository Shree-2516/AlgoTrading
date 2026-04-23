import { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import { GoogleLogin } from "@react-oauth/google";
import { login, loginWithGoogle } from "../api";
import { useAuthStore } from "../../../shared/state/useAuthStore";

export default function Login() {
  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const navigate = useNavigate();
  const setToken = useAuthStore((state) => state.setToken);

  // ✅ Auto redirect if already logged in
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      navigate("/dashboard");
    }
  }, [navigate]);

  // ✅ Normal login
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await login(form);
      setToken(res.data.access_token);
      navigate("/dashboard");
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.detail || "Login failed");
    }
  };

  // ✅ Google login handler
  const handleGoogleLogin = async (credentialResponse) => {
    try {
      const res = await loginWithGoogle(credentialResponse.credential);

      setToken(res.data.access_token);
      navigate("/dashboard");

    } catch (err) {
      console.error(err);
      alert(err.response?.data?.detail || "Google login failed");
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded-lg shadow-md w-80 space-y-4"
      >
        <h2 className="text-2xl font-bold text-center">Login</h2>

        <input
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={(e) =>
            setForm({ ...form, email: e.target.value })
          }
          className="w-full p-2 border rounded"
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={(e) =>
            setForm({ ...form, password: e.target.value })
          }
          className="w-full p-2 border rounded"
          required
        />

        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
        >
          Login
        </button>

        {/* 🔥 Divider */}
        <div className="text-center text-gray-400">OR</div>

        {/* ✅ Google Login Button */}
        <div className="flex justify-center">
          <GoogleLogin
            onSuccess={handleGoogleLogin}
            onError={() => alert("Google Login Failed")}
          />
        </div>

        {/* ✅ Register Link */}
        <p className="text-sm text-center">
          New user?{" "}
          <Link to="/register" className="text-blue-500 hover:underline">
            Register
          </Link>
        </p>
      </form>
    </div>
  );
}
