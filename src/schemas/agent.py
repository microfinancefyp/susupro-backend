
from pydantic import BaseModel
from typing import Optional

class AgentSchema(BaseModel):
    agentID: str
    agentName: str
    agentEmail: str
    agentPassword: str
    agentRole: str
    agentPhone: str
    createdAt: str
    
class AgentCredential(BaseModel):
    agentID: str
    agentName: Optional[str] = None
    agentPassword: str
    
class AgentResponse(BaseModel):
    message: str
    agentName: str