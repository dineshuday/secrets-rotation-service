from fastapi import FastAPI, HTTPException
from src.secrets_utils import get_secret, rotate_secret

app = FastAPI()

@app.get("/get-secret/{name}")
def api_get_secret(name: str):
    secret = get_secret(name)
    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")
    return {"secret": secret}

@app.post("/rotate-secret/{name}")
def api_rotate_secret(name: str):
    new_secret = rotate_secret(name)
    return {"status": "rotated", "new_secret": new_secret}