#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm  import relationship
from sqlalchemy import Column, String, ForeignKey

class State(BaseModel, Base):
    """class state"""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="State", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializing state instance"""
        super().__init__(*args, **kwargs)
