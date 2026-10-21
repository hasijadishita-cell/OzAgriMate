from fastapi import FastAPI, HTTPException

app=FastAPI()
farms={}

@app.post("/farms", status_code=201)
def add_farm(name: str, location: str, sizeHectares: float):
  farm_id=max(farms, default=0)+1
  
  farms[farm_id]={
    "name": name,
    "location": location,
    "sizeHectares": sizeHectares
  }
  return{
  "farmID": farm_id,
  "message": "Farm created successfully"
  }

@app.put("/farms/{farmID}")
def update_farm(farmID: int, name: str, location: str, sizeHectares: float):
  if farmID not in farms:
    raise HTTPException(status_code=404, detail="Farm not found")
  farms[farmID]={
  "name": name,
  "location": location,
  "sizeHectares": sizeHectares
  }
  return {
  "farmID": farmID,
  "message": "Farm updated successfully"
  }

@app.delete("/farms/{farmID}")
def delete_farm(farmID: int):
  if farmID not in farms:
    raise HTTPException(status_code=404, detail="Farm not found")
  del farms[farmID]
  return {"message": "Farm deleted successfully"}
