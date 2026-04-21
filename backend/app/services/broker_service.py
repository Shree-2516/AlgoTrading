from SmartApi import SmartConnect
import requests


# =========================
# ANGEL ONE
# =========================
def verify_angel(api_key: str, api_secret: str, client_id: str):
    try:
        obj = SmartConnect(api_key=api_key)

        data = obj.generateSession(
            client_id,
            api_secret
        )

        if data.get("status"):
            return True
        return False

    except Exception as e:
        print("Angel error:", e)
        return False


# =========================
# DHAN
# =========================
def verify_dhan(api_key: str):
    try:
        url = "https://api.dhan.co/v2/profile"

        headers = {
            "access-token": api_key
        }

        res = requests.get(url, headers=headers)

        if res.status_code == 200:
            return True
        return False

    except Exception as e:
        print("Dhan error:", e)
        return False