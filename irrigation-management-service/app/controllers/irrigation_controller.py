from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.irrigation_service import (
    get_farm_irrigation_schedules,
    update_irrigation_schedule,
)


class IrrigationScheduleUpdate(BaseModel):
    startTime: str
    durationMinutes: int
    status: str


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


@router.put("/farms/{farm_id}/irrigation/schedules/{schedule_id}")
def update_schedule(
    farm_id: int,
    schedule_id: int,
    request: IrrigationScheduleUpdate,
):
    updated_schedule = update_irrigation_schedule(
        farm_id,
        schedule_id,
        request.startTime,
        request.durationMinutes,
        request.status,
    )

    if updated_schedule is None:
        raise HTTPException(
            status_code=404,
            detail="Irrigation schedule not found",
        )

    return {
        **updated_schedule,
        "message": "Irrigation schedule updated successfully",
    }