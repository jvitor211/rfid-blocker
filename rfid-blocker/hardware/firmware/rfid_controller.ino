#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10

MFRC522 rfid(SS_PIN, RST_PIN);

void setup() {
    Serial.begin(9600);
    SPI.begin();
    rfid.PCD_Init();
    Serial.println("RFID Scanner Initialized");
}

void loop() {
    if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
        return;

    String tagID = "";
    for (byte i = 0; i < rfid.uid.size; i++) {
        tagID += String(rfid.uid.uidByte[i], HEX);
    }
    Serial.println("Detected Tag: " + tagID);

    if (tagID == "blocked_tag_id") {
        Serial.println("Tag Blocked");
    }
    delay(1000);
}