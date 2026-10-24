from pydantic import BaseModel

class FarmRequest(BaseModel):
  name: str
  location: str
  sizeHectares: float
