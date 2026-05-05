import uuid
from datetime import datetime, timedelta

reset_tokens = {}

def generate_reset_token(admin_id):
    token = str(uuid.uuid4())
    reset_tokens[token] = {
        "admin_id": admin_id,
        "expires": datetime.utcnow() + timedelta(hours=1)
    }
    return token

def validate_reset_token(token):
    data = reset_tokens.get(token)

    if not data:
        return None

    if datetime.utcnow() > data["expires"]:
        return None

    return data["admin_id"]
