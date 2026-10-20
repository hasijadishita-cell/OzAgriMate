from app.repositories.irrigation_repository import get_schedules_by_farm


def get_farm_irrigation_schedules(farm_id: int):
    return get_schedules_by_farm(farm_id)