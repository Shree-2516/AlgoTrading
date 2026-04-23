import { BrowserRouter, Route, Routes } from "react-router-dom";

import ProtectedRoute from "../modules/auth/components/ProtectedRoute";
import Login from "../modules/auth/pages/Login";
import Register from "../modules/auth/pages/Register";
import Backtest from "../modules/backtest/pages/Backtest";
import Broker from "../modules/broker/pages/Broker";
import Dashboard from "../modules/dashboard/pages/Dashboard";
import Home from "../modules/home/pages/Home";
import News from "../modules/news/pages/News";
import Account from "../modules/account/pages/Account";
import Profile from "../modules/account/pages/Profile";
import Reports from "../modules/reports/pages/Reports";
import HistoricalData from "../modules/reports/pages/HistoricalData";
import CreateStrategy from "../modules/strategy/pages/CreateStrategy";
import SavedStrategy from "../modules/strategy/pages/SavedStrategy";
import StrategyTemplates from "../modules/strategy/pages/StrategyTemplates";
import Subscription from "../modules/subscription/pages/Subscription";
import Trading from "../modules/trading/pages/Trading";
import Layout from "../shared/components/Layout";
import PublicNavbar from "../shared/components/PublicNavbar";


export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
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

        <Route element={<ProtectedRoute />}>
          <Route element={<Layout />}>
            <Route path="/dashboard" element={<Dashboard />} />
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
