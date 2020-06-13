# Vacuum a specific room

rooms = []
roomString = data.get("room").lower()

if "kitchen" in roomString:
    rooms.append(19)
if "living room" in roomString:
    rooms.append(29)
if "kitchen" in roomString:
    rooms.append(19)
if any(room in roomString for room in ["nursery", "kids room"]]):
    rooms.append(19)

rooms = []
roomString = data.get("room")

room = data.get("room")
logger.info("Hello %s", name)
hass.bus.fire(name, {"wow": "from a Python script!"})


# turn_on_light.py
entity_id = data.get("entity_id")

if entity_id is not None:
    service_data = {"entity_id": entity_id, "command": "app_segment_clean", "params": [19]}
    hass.services.call("vacuum", "send_command", service_data, False)