from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    accounts = relationship("Account", back_populates="owner")
    sent_transactions = relationship("Transaction", foreign_keys="Transaction.from_user_id", back_populates="sender")
    received_transactions = relationship("Transaction", foreign_keys="Transaction.to_user_id", back_populates="receiver")

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String(20), unique=True, index=True, nullable=False)
    balance = Column(Float, default=0.0, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    owner = relationship("User", back_populates="accounts")

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    from_account_number = Column(String(20), nullable=False)
    to_account_number = Column(String(20), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(Text)
    transaction_type = Column(String(20), default="transfer")
    status = Column(String(20), default="completed")
    from_user_id = Column(Integer, ForeignKey("users.id"))
    to_user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    sender = relationship("User", foreign_keys=[from_user_id], back_populates="sent_transactions")
    receiver = relationship("User", foreign_keys=[to_user_id], back_populates="received_transactions")