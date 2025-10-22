from typing import Dict, List, Optional
from datetime import datetime

from fastpaip_app.classifications.domain.ports import ClassificationRepository
from fastpaip_app.classifications.domain.models import Classification, ClassificationCreate


class InMemoryClassificationRepository(ClassificationRepository):
    """
    In-memory implementation of ClassificationRepository using a dictionary.
    This is useful for testing or simple applications without a database.
    """
    def __init__(self):
        # Initialize with an empty dictionary to store classifications
        # Key: classification ID, Value: Classification object
        self._classifications: Dict[int, Classification] = {}
        # Auto-increment counter for ID generation
        self._next_id: int = 1
    
    def get_by_id(self, id: int) -> Optional[Classification]:
        """Retrieve a classification by its ID."""
        return self._classifications.get(id)
    
    def create(self, data: ClassificationCreate) -> Classification:
        """Create a new classification with auto-generated ID."""
        # Create a new Classification with an auto-generated ID
        classification = Classification(
            id=self._next_id,
            call_id=data.call_id,
            category=data.category,
        )
        
        # Store in the dictionary
        self._classifications[classification.id] = classification
        
        # Increment ID counter for next creation
        self._next_id += 1
        
        return classification
    
    def update(self, classification: Classification) -> Classification:
        """Update an existing classification."""
        if classification.id not in self._classifications:
            raise ValueError(f"Classification with ID {classification.id} not found")
        
        # Store updated classification
        self._classifications[classification.id] = classification
        return classification
    
    def delete(self, id: int) -> None:
        """Delete a classification by ID."""
        if id in self._classifications:
            del self._classifications[id]
    
    def find_by_call_id(self, call_id: str) -> List[Classification]:
        """Find all classifications for a specific call ID."""
        return [
            classification 
            for classification in self._classifications.values()
            if classification.call_id == call_id
        ]

