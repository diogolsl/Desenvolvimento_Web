from sqlalchemy.sql import func
from sqlalchemy import Enum
from .extensions import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(
        Enum("customer", "agent", name="user_role"), nullable=False, default="customer")
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())

    customer_tickets = db.relationship(
        "Ticket",
        foreign_keys="Ticket.customer_id",
        back_populates="customer",
        lazy=True
    )