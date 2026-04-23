import requests

from app.core.logger import get_logger


logger = get_logger(__name__)


def verify_angel(api_key: str, api_secret: str, client_id: str):
    try:
        from SmartApi import SmartConnect

        client = SmartConnect(api_key=api_key)
        data = client.generateSession(client_id, api_secret)
        return bool(data.get("status"))
    except Exception as exc:
        logger.exception("Angel verification failed: %s", exc)
        return False


def verify_dhan(api_key: str):
    try:
        response = requests.get(
            "https://api.dhan.co/v2/profile",
            headers={"access-token": api_key},
            timeout=10,
        )
        return response.status_code == 200
    except Exception as exc:
        logger.exception("Dhan verification failed: %s", exc)
        return False
