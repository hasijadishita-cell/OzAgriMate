from app.repositories.irrigation_repository import get_schedules_by_farm


def get_farm_irrigation_schedules(farm_id: int):
    return get_schedules_by_farm(farm_id)

from app.repositories.irrigation_repository import (
    get_schedules_by_farm,
    update_schedule,
)


def get_farm_irrigation_schedules(farm_id: int):
    return get_schedules_by_farm(farm_id)


def update_irrigation_schedule(
    farm_id: int,
    schedule_id: int,
    start_time: str,
    duration_minutes: int,
    status: str,
):
    return update_schedule(
        farm_id,
        schedule_id,
        start_time,
        duration_minutes,
        status,
    )