from pydantic import BaseModel

class FarmRequest(BaeModel):
  name: str
  location: str
  sizeHectares: float
