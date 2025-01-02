from fastapi import FastAPI
from app.api.endpoints import rfid

app = FastAPI(title="RFID Blocker API", version="1.0")

app.include_router(rfid.router, prefix="/api/rfid", tags=["RFID"])

@app.get("/")
def root():
    return {"message": "Welcome to the RFID Blocker API"}