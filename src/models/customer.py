from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    customerID = Column(String(10), primary_key=True, unique=True, index=True)
    customerName = Column(String(100), index=True)
    customerAccountNo = Column(String(100), unique=True, index=True)
    agentID = Column(String(10), ForeignKey("agents.agentID"), index=True)
    customerLocation = Column(String(100))
    customerAccountType = Column(String(20))
    customerDateOfBirth = Column(String(20))
    customerNextofKin = Column(String(100))
    customerNextofKinPhone = Column(String(10))
    customerPhone = Column(String(10))
    customerDailyRate = Column(Integer)
    customerRegDate = Column(String(100))
    
    accounts = relationship("Account", back_populates="customer")