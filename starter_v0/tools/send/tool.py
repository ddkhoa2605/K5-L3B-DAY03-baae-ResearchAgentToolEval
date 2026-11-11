from __future__ import annotations

import os
import re
from typing import Any

import requests

from tools._shared import TIMEOUT, err


def _is_confirmed(confirmed: Any) -> bool:
    """Only a real True (or the string "true") counts as confirmation.

    Small models sometimes send confirmed="false"; a non-empty string is truthy in
    Python, so `if not confirmed` used to let that through and hit the network.
    """
    if isinstance(confirmed, bool):
        return confirmed
    if isinstance(confirmed, str):
        return confirmed.strip().lower() == "true"
    return False


def _redact_token(message: str) -> str:
    return re.sub(r"bot[^/\s]+/", "bot<REDACTED>/", message)


def send_telegram(text: str = "", confirmed: bool = False) -> dict[str, Any]:
    if not _is_confirmed(confirmed):
        return {
            "tool": "send_telegram",
            "status": "needs_confirmation",
            "message": "Only send after the user explicitly confirms.",
        }
    try:
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if not token or not chat_id:
            raise RuntimeError("Missing TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID env var")
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        return {"tool": "send_telegram", "status": "sent"}
    except Exception as exc:
        # requests puts the full URL (including the bot token) in HTTPError messages.
        result = err("send_telegram", exc)
        result["message"] = _redact_token(result["message"])
        return result

