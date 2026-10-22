# Sends the new reading to the "sensor-readings" topic for other services
def publish_reading_event(reading: dict):
    event = {
        "eventType": "SensorReadingRecorded",
        "readingId": reading["readingId"],
        "sensorId": reading["sensorId"],
        "farmId": reading["farmId"],
        "readingType": reading["readingType"],
        "value": reading["value"],
        "unit": reading["unit"],
        "recordedAt": reading["recordedAt"].isoformat(),
    }

    # Print statement acts as publishing the event
    print(f"[Event published to 'sensor-readings'] {event}")
    return event