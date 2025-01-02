def block_tag(tag_id: str):
    print(f"Blocking RFID tag {tag_id}")
    return True

def get_status(tag_id: str):
    return {"tag_id": tag_id, "status": "blocked"}