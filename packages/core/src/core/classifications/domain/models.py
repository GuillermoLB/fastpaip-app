"""
Defines the Pydantic models for the Invoicing domain.

These models represent the core data structures and "Ubiquitous Language"
for all business logic related to invoices. They act as the data contracts
for services, repositories, and external interactions within this Bounded Context.
"""
from enum import Enum
from pydantic import BaseModel

class Category(str, Enum):
    COMMERCIAL = "COMMERCIAL"
    FOLLOWING = "FOLLOWING"
    
class ClassificationCategory(BaseModel):
    category: Category

class ClassificationBase(BaseModel):
    call_id: str
    classification_category: ClassificationCategory

class ClassificationCreate(ClassificationBase):
    pass

class Classification(ClassificationBase):
    id: int