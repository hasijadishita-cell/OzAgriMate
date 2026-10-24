farms={}

def add_farm(name, location, sizeHectares):
  farm_id=max(farms, default=0)+1
  farms[farm_id]={
    "name": name,
    "location": location,
    "sizeHectares": sizeHectares
  }
  return farm_id

def update_farm(farmID, name, locatio, sizeHectares):
  if farmID not in farms:
    return False
  farms[farmID]={
  "name": name,
  "location": location,
  "sizeHectares": sizeHectares
  }
  return True
  
def delete_farm(farmID):
  if farmID not in farms:
    return False
  del farms[farmID]
  return True
