"""
Defines the Pydantic models for the Invoicing domain.

These models represent the core data structures and "Ubiquitous Language"
for all business logic related to invoices. They act as the data contracts
for services, repositories, and external interactions within this Bounded Context.
"""
from datetime import datetime, timezone
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

class Category(str, Enum):
    GENERATED = "GENERATED"
    ISSUED = "ISSUED"

class ClassificationBase(BaseModel):
    call_id: str
    category: Category

class ClassificationCreate(ClassificationBase):
    pass

class Classification(ClassificationBase):
    id: int