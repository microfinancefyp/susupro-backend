
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Agents(Base):
    __tablename__ = "agents"

    agentID = Column(String(10), primary_key=True, index=True)
    agentName = Column(String(100), unique=False, index=True)
    agentEmail = Column(String(100), unique=True, index=True)
    agentPassword = Column(String(100))
    agentRole = Column(String(10))
    agentPhone = Column(String(10))
    createdAt = Column(String(10))
    
    transactions = relationship("Transaction", back_populates="agents")
    

class AgentCredential(Base):
    __tablename__ = "credentials"

    agentID = Column(String(10), primary_key=True, index=True)
    agentName = Column(String(100), unique=True, index=True)
    agentPassword = Column(String(100))