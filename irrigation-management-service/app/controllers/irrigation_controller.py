from fastapi import APIRouter, HTTPException

from app.services.irrigation_service import get_farm_irrigation_schedules


router = APIRouter()


@router.get("/farms/{farm_id}/irrigation/schedules")
def get_irrigation_schedules(farm_id: int):
    schedules = get_farm_irrigation_schedules(farm_id)

    if not schedules:
        raise HTTPException(
            status_code=404,
            detail="No irrigation schedules found for this farm",
        )

    return {
        "farmId": farm_id,
        "schedules": schedules,
    }