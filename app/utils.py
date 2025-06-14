
import base64
import hashlib
import hmac
import json
from urllib.parse import parse_qs

BOT_TOKEN = "YOUR_BOT_TOKEN"

def validate_init_data(init_data: str) -> dict:
    decoded = parse_qs(init_data)
    data_check_string = "\n".join(
        f"{k}={v[0]}" for k, v in sorted(decoded.items()) if k != "hash"
    )
    secret = hashlib.sha256(BOT_TOKEN.encode()).digest()
    expected_hash = hmac.new(secret, data_check_string.encode(), hashlib.sha256).hexdigest()

    if decoded.get("hash", [""])[0] != expected_hash:
        raise ValueError("Invalid init data hash")

    if "user" in decoded:
        user_data = json.loads(decoded["user"][0])
        return {"user": user_data}
    else:
        raise ValueError("Missing user data")
