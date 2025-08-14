import secrets

SECRET_STORE = {"api_key": "initial-secret"}

def get_secret(name: str):
    return SECRET_STORE.get(name, None)

def rotate_secret(name: str):
    new_value = secrets.token_urlsafe(32)
    SECRET_STORE[name] = new_value
    return new_value