from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.agent import AgentCredential, AgentResponse
from ..database import get_db
from ..models.agents import Agents
from ..utility.utility import verify_password
from ..schemas.agent import AgentResponse, AgentSchema
from ..models.agents import Agents
from ..utility.utility import hashpassword

authRouter = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
    
)

@authRouter.post("/signin")
def signin(agentCredential: AgentCredential, db: Session = Depends(get_db)):
    agent = db.query(Agents).filter(Agents.agentID == agentCredential.agentID).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    if not verify_password(agentCredential.agentPassword, agent.agentPassword):
        raise HTTPException(status_code=404, detail="Incorrect password")
    
    return AgentResponse(message="success", agentName=agent.agentName)

@authRouter.post("/signup")
async def create_agent(agent: AgentSchema, db: Session=Depends(get_db)):
    hashedpassword = hashpassword(agent.agentPassword)
    new_agent = Agents(agentID =agent.agentID, agentName=agent.agentName, agentEmail=agent.agentEmail, agentPassword=hashedpassword, agentRole=agent.agentRole, agentPhone=agent.agentPhone, createdAt=agent.createdAt)
    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)
    return new_agent


