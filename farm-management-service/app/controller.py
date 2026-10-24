from fastapi import FastAPI, HTTPException
from app import service
from app.models import FarmRequest

router = APIRouter()
#POST- Create a farm
@router.post("/farms", status_code=201)
def add_farm(request: FarmRequest):
  farms[farm_id]={
    "name": name,
    "location": location,
    "sizeHectares": sizeHectares
  }
  return{
  "farmID": farm_id,
  "message": "Farm created successfully"
  }

#PUT- Update a farm
@router.put("/farms/{farm_id}")
def update_farm(farmID: int, request: FarmRequest):
  updated= service.update_farm(
    farmID,
    request.name,
    request.location,
    request.sizeHectares)
  return {
  "farmID": farmID,
  "message": "Farm updated successfully"
  }

#DELETE- Delete a farm
def delete_farm(farmID: int):
  deleted= service.delete_farm(farm_id)
  if not deleted:
    raise HTTPException(status_code=404, detail="Farm not found")
  return {"message": "Farm deleted successfully"}


 
