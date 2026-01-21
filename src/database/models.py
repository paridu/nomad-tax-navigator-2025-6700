from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    home_country_code = Column(String(3))  # ISO Alpha-3
    tax_residency_status = Column(JSON) # Current determined status
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class TravelEntry(Base):
    __tablename__ = "travel_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    country_code = Column(String(3), nullable=False)
    entry_date = Column(Date, nullable=False)
    exit_date = Column(Date, nullable=True) # Null means currently in country
    purpose = Column(String) # e.g., "Work", "Tourism"
    
    user = relationship("User", back_populates="travels")

User.travels = relationship("TravelEntry", back_populates="user")