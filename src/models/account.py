from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from enum import Enum


class AccountType(str, Enum):
    SAVINGS = "Savings"
    SUSU = "Susu"
    BUSINESS = "Business"


class Account(Base):
    __tablename__ = "accounts"

    accountID = Column(String(10), primary_key=True, index=True)
    customerID = Column(String(10), ForeignKey("customers.customerID"))
    accountType = Column(String(10))
    accountBalance = Column(Integer)
    accountDateOpened = Column(String(20))
    accountStatus = Column(String(10))
    transactionID = Column(String(10), ForeignKey("transactions.transactionID"))
    
    customer = relationship("Customer", back_populates="accounts")
    transactions = relationship(
        "Transaction",
        back_populates="accounts",
        foreign_keys="Transaction.accountID"  
    )