from fastapi import APIRouter

router = APIRouter()

@router.post("/block")
def block_rfid(tag_id: str):
    return {"message": f"RFID tag {tag_id} blocked successfully"}

@router.get("/status/{tag_id}")
def get_rfid_status(tag_id: str):
    return {"tag_id": tag_id, "status": "blocked"}