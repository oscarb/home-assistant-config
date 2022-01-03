# Vacuum a specific room

roomConfig = {
    16: ["hallway"],
    17: ["bedroom"],
    18: ["entrance"],
    19: ["kitchen"],
    20: ["nursery", "kids room"],
    22: ["living room"],
    23: ["office"] 
}

entity_id = data.get("entity_id")
area = data.get("area").lower()

roomsToClean = []

for roomNumber, roomNames in roomConfig.items():
    for name in roomNames:
        if name in area: 
            roomsToClean.append(int(roomNumber))
            continue

if entity_id is not None and len(roomsToClean) > 0: 
    service_data = {"entity_id": entity_id, "command": "app_segment_clean", "params": roomsToClean}
    hass.services.call("vacuum", "send_command", service_data, False)
