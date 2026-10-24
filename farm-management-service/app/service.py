from app import repository

def add_farm(name, location, sizeHectares):
  return repository.add_farm(
    name, location, sizeHectares
  )

def update_farm(farm_id, name, location, sizeHectares):
  return repository.update_farm(
    farm_id, name, location, sizeHectares)

def delete_farm(farm_id):
  return repository.delete_farm(farm_id)
