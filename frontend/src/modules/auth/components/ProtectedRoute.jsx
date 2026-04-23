import { jwtDecode } from "jwt-decode";
import { Navigate, Outlet, useLocation } from "react-router-dom";
import { useAuthStore } from "../../../shared/state/useAuthStore";

export default function ProtectedRoute() {
  const token = useAuthStore((state) => state.token);
  const logout = useAuthStore((state) => state.logout);
  const location = useLocation();

  if (!token) {
    return <Navigate to="/login" replace state={{ from: location }} />;
  }

  try {
    const decoded = jwtDecode(token);
    const expiresAt = decoded.exp ? decoded.exp * 1000 : null;

    if (expiresAt && expiresAt <= Date.now()) {
      logout();
      return <Navigate to="/login" replace state={{ from: location }} />;
    }
  } catch {
    logout();
    return <Navigate to="/login" replace state={{ from: location }} />;
  }

  return <Outlet />;
}
