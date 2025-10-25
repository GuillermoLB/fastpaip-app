"""
Defines the ports (interfaces) for the Invoicing domain.

These protocols specify the contracts that external components (like repositories
or gateways) must fulfill to be used by this domain's services. This adheres to the
Dependency Inversion Principle, a key part of clean architecture.
"""
from typing import Protocol, List

from plummy.protocols import CanClassify

from .models import Category, Classification, ClassificationCreate
from plummy.protocols import CRUDRepository


class ClassificationRepository(
    CRUDRepository[Classification, int, ClassificationCreate],
    Protocol
):
    """
    The port for classification persistence, providing full CRUD capabilities
    and custom queries.
    """
    # You inherit create, get_by_id, update, and delete from CRUDRepository.
    # You only need to define the NEW methods specific to this repository.
    
    def find_by_call_id(self, call_id: str) -> List[Classification]:
        """Finds all classifications associated with a specific call."""
        ...
        
class LLMClassifier(CanClassify[str, Category], Protocol):
    """
    A concrete adapter that implements the 'CanClassify' port
    using the OpenAI API.
    """