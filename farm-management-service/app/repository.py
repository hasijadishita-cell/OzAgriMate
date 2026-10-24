farms={}

def add_farm(name, location, sizeHectares):
  farm_id=max(farms, default=0)+1
  farms[farm_id]={
    "name": name,
    "location": location,
    "sizeHectares": sizeHectares
  }
  return farm_id

def update_farm(farm_id, name, location, sizeHectares):
  if farm_id not in farms:
    return False
  farms[farm_id]={
  "name": name,
  "location": location,
  "sizeHectares": sizeHectares
  }
  return True
  
def delete_farm(farm_id):
  if farm_id not in farms:
    return False
  del farms[farm_id]
  return True
