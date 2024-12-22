
from ..database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Admin(Base):
    __tablename__ = "admins"

    adminID = Column(String(10), primary_key=True, unique=True, index=True)
    adminName = Column(String(100), index=True)
    adminEmail = Column(String(100), unique=True, index=True)
    adminPhone = Column(String(10), unique=True, index=True)
    adminPassword = Column(String(100))