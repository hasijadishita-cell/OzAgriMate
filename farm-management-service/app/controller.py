from fastapi import APIRouter, HTTPException
from app import service
from app.models import FarmRequest

router = APIRouter()
#POST- Create a farm
@router.post("/farms", status_code=201)
def add_farm(request: FarmRequest):
  farm_id = service.add_farm(
    request.name,
    request.location,
    request.sizeHectares
  )
  return{
  "farmID": farm_id,
  "message": "Farm created successfully"
  }

#PUT- Update a farm
@router.put("/farms/{farm_id}")
def update_farm(farm_id: int, request: FarmRequest):
  updated= service.update_farm(
    farm_id,
    request.name,
    request.location,
    request.sizeHectares)
  if updated:
    return {
  "farm_id": farm_id,
  "message": "Farm updated successfully"
  }
  else:
    raise HTTPException(
      status_code=404,
      detail= "Farm not found"
    )

#DELETE- Delete a farm
@router.delete("/farms/{farm_id}")
def delete_farm(farm_id: int):
  deleted= service.delete_farm(farm_id)
  if not deleted:
    raise HTTPException(status_code=404, detail="Farm not found")
  return {"message": "Farm deleted successfully"}


 



 
