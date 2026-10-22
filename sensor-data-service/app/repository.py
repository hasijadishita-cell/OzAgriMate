from datetime import datetime, timedelta
now = datetime.now().astimezone()

# # Every sensor in OzAgriMate and which farm it belongs to
sensors = {
    1: {"sensorId": 1, "farmId": 1},
    2: {"sensorId": 2, "farmId": 1},
    3: {"sensorId": 3, "farmId": 1},
}

# Every reading saved from all sensors
readings = [
    {
        "readingId": 2498,
        "sensorId": 1,
        "farmId": 1,
        "readingType": "temperature",
        "value": 34.2,
        "unit": "°C",
        "recordedAt": now - timedelta(minutes=5),
    },
    {
        "readingId": 2499,
        "sensorId": 2,
        "farmId": 1,
        "readingType": "soilMoisture",
        "value": 18.5,
        "unit": "%",
        "recordedAt": now - timedelta(minutes=3),
    },
    {
        "readingId": 2500,
        "sensorId": 3,
        "farmId": 1,
        "readingType": "soilMoisture",
        "value": 22.0,
        "unit": "%",
        "recordedAt": now - timedelta(hours=30),
    },
]

# Find one sensor by its ID
def get_sensor(sensor_id: int):
    return sensors.get(sensor_id)

# Find all sensors on a farm
def get_sensors_by_farm(farm_id: int):
    return [
        sensor
        for sensor in sensors.values()
        if sensor["farmId"] == farm_id
    ]

# Give a new reading the next ID and save it
def save_reading(reading: dict):
    last_reading = readings[-1]
    new_id = last_reading["readingId"] + 1
    reading["readingId"] = new_id
    readings.append(reading)
    return reading

# Find a sensor's latest reading
def get_latest_reading(sensor_id: int):
    latest = None

    for reading in readings:
        if reading["sensorId"] == sensor_id:
            if latest is None or reading["recordedAt"] > latest["recordedAt"]:
                latest = reading

    return latest