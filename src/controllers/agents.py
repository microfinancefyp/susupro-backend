
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models.agents import Agents
from ..models.customer import Customer
from sqlalchemy import text
from ..database import get_db


agentRouter = APIRouter(
    prefix="/api/agents",
    tags=["agents"],
    responses={404: {"description": "Not found"}},
)

@agentRouter.get("/")
def get_all_agents(db: Session=Depends(get_db)):
    agents = db.query(Agents).all()
    return {"agents": agents}

@agentRouter.get("/{agent_id}")
def get_agent(agent_id: str, db: Session=Depends(get_db)):
    agent = db.query(Agents).filter(Agents.userID == agent_id).first()
    return {"agent": agent}

@agentRouter.get("/{agent_id}/customers")
def get_agent_customers(agent_id: str, db: Session=Depends(get_db)):
    customers = db.query(Customer).filter(Customer.agentID == agent_id).all()
    return {"customers": customers}

@agentRouter.delete("/{agent_id}")
def delete_agent(agent_id: str, db: Session=Depends(get_db)):
    db.query(Agents).filter(Agents.agentID == agent_id).delete()
    db.commit()
    return {"message": "Agent deleted successfully"}