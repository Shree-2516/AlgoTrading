import { createRoot } from 'react-dom/client'
import { GoogleOAuthProvider } from "@react-oauth/google"

import App from './App.jsx'
import './index.css'

const googleClientId = import.meta.env.VITE_GOOGLE_CLIENT_ID

if (!googleClientId) {
  throw new Error("Missing VITE_GOOGLE_CLIENT_ID. Check frontend/.env and restart the Vite dev server.")
}

console.info(
  "Google OAuth client loaded:",
  `${googleClientId.slice(0, 8)}...${googleClientId.slice(-8)}`,
)

createRoot(document.getElementById('root')).render(
  <GoogleOAuthProvider clientId={googleClientId}>
    <App />
  </GoogleOAuthProvider>
)
