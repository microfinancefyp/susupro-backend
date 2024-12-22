
from pydantic import BaseModel

class AdminSchema(BaseModel):
    adminID: str
    adminName: str
    adminEmail: str
    adminPhone: str
    adminPassword: str
    
class ReturnSchema(BaseModel):
    message: str
    adminID: str
    adminName: str
    adminEmail: str
    adminPhone: str