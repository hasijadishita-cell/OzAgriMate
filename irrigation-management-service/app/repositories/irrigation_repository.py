irrigation_schedules = [
    {
        "scheduleId": 301,
        "farmId": 1,
        "startTime": "06:00",
        "durationMinutes": 30,
        "status": "active",
    },
    {
        "scheduleId": 302,
        "farmId": 1,
        "startTime": "18:00",
        "durationMinutes": 20,
        "status": "active",
    },
    {
        "scheduleId": 401,
        "farmId": 2,
        "startTime": "07:00",
        "durationMinutes": 25,
        "status": "inactive",
    },
]


def get_schedules_by_farm(farm_id: int):
    return [
        schedule
        for schedule in irrigation_schedules
        if schedule["farmId"] == farm_id
    ]

def update_schedule(
    farm_id: int,
    schedule_id: int,
    start_time: str,
    duration_minutes: int,
    status: str,
):
    for schedule in irrigation_schedules:
        if (
            schedule["farmId"] == farm_id
            and schedule["scheduleId"] == schedule_id
        ):
            schedule["startTime"] = start_time
            schedule["durationMinutes"] = duration_minutes
            schedule["status"] = status

            return schedule

    return None