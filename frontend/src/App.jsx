import { BrowserRouter, Routes, Route } from "react-router-dom";

// Layout & Protection
import Layout from "./components/layout/Layout";
import ProtectedRoute from "./components/auth/ProtectedRoute";

// Public Pages
import PublicNavbar from "./components/layout/PublicNavbar";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";

// Private Pages
import Dashboard from "./pages/Dashboard";
import Broker from "./pages/Broker";
import News from "./pages/News";
import HistoricalData from "./pages/HistoricalData";
import StrategyTemplates from "./pages/StrategyTemplates";
import CreateStrategy from "./pages/CreateStrategy";
import SavedStrategy from "./pages/SavedStrategy";
import Backtest from "./pages/Backtest";
import Reports from "./pages/Reports";
import Subscription from "./pages/Subscription";
import Account from "./pages/Account";
import Profile from "./pages/Profile";

// ✅ NEW IMPORT
import Trading from "./pages/Trading";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* 🌐 PUBLIC ROUTES */}
        <Route
          path="/"
          element={
            <>
              <PublicNavbar />
              <Home />
            </>
          }
        />

        <Route
          path="/login"
          element={
            <>
              <PublicNavbar />
              <Login />
            </>
          }
        />

        <Route
          path="/register"
          element={
            <>
              <PublicNavbar />
              <Register />
            </>
          }
        />

        {/* 🔒 PROTECTED ROUTES */}
        <Route element={<ProtectedRoute />}>
          <Route element={<Layout />}>

            <Route path="/dashboard" element={<Dashboard />} />

            {/* ✅ NEW TRADING PAGE */}
            <Route path="/trading" element={<Trading />} />

            <Route path="/broker" element={<Broker />} />
            <Route path="/news" element={<News />} />
            <Route path="/historical" element={<HistoricalData />} />
            <Route path="/templates" element={<StrategyTemplates />} />
            <Route path="/create-strategy" element={<CreateStrategy />} />
            <Route path="/saved-strategy" element={<SavedStrategy />} />
            <Route path="/backtest" element={<Backtest />} />
            <Route path="/reports" element={<Reports />} />
            <Route path="/subscription" element={<Subscription />} />
            <Route path="/account" element={<Account />} />
            <Route path="/profile" element={<Profile />} />

          </Route>
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;