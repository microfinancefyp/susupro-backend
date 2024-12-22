from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base
from sqlalchemy.orm import relationship
from ..models.agents import Agents

class Transaction(Base):
    __tablename__ = "transactions"

    transactionID = Column(String(10), primary_key=True, index=True)
    transactionType = Column(String(10), index=True)
    transactionAmount = Column(Integer, index=True)
    transactionDate = Column(String(20), index=True)
    agentID = Column(String(10), ForeignKey("agents.agentID"), index=True)
    customerID = Column(String(10), ForeignKey("customers.customerID"), index=True)
    accountID = Column(String(10), ForeignKey("accounts.accountID"), index=True)
    
    agents = relationship("Agents", back_populates="transactions")
    accounts = relationship(
        "Account",
        back_populates="transactions",
        foreign_keys="Transaction.accountID"  # Specify the FK to Account
    )