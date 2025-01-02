import React, { useState } from "react";

function RFIDScanner() {
  const [tagId, setTagId] = useState("");
  const [message, setMessage] = useState("");

  const handleBlock = async () => {
    try {
      const response = await fetch(`/api/rfid/block`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tag_id: tagId }),
      });
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      setMessage("Error blocking tag");
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter RFID Tag ID"
        value={tagId}
        onChange={(e) => setTagId(e.target.value)}
      />
      <button onClick={handleBlock}>Block Tag</button>
      <p>{message}</p>
    </div>
  );
}

export default RFIDScanner;