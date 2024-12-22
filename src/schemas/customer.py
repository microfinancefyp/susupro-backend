
from pydantic import BaseModel
from typing import Optional
from enum import Enum



class CustomerSchema(BaseModel):
    customerID: str
    customerName: str
    customerAccountNo: str
    customerLocation: str
    customerDateOfBirth: str
    customerNextofKin: str
    customerNextofKinPhone: str
    customerPhone: str
    customerDailyRate: int
    customerRegDate: str
    agentID: str