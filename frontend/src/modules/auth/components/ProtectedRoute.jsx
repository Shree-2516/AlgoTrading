import { Navigate, Outlet } from "react-router-dom";
import { useAuthStore } from "../../../shared/state/useAuthStore";

export default function ProtectedRoute() {
  const token = useAuthStore((state) => state.token);

  if (!token) {
    return <Navigate to="/login" />;
  }

  return <Outlet />; // ✅ FIXED
}
