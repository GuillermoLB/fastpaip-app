from typing import Dict, List, Optional

from core.classifications.domain.ports import ClassificationRepository
from core.classifications.domain.models import Classification, ClassificationCreate


class InMemoryClassificationRepository(ClassificationRepository):
    """
    In-memory implementation of ClassificationRepository using a dictionary.
    This is useful for testing or simple applications without a database.
    """
    def __init__(self, classifications_dict: Optional[Dict[int, Classification]] = {}):
        # Initialize with an empty dictionary to store classifications
        # Key: classification ID, Value: Classification object
        self._classifications: Dict[int, Classification] = classifications_dict
        # Auto-increment counter for ID generation
        self._next_id: int = 1
    
    def get_by_id(self, id: int) -> Optional[Classification]:
        """Retrieve a classification by its ID."""
        classification = self._classifications.get(id)
        if classification is None:
            raise ValueError(f"Classification with ID {id} not found")
        return classification
    
    def create(self, data: ClassificationCreate) -> Classification:
        """Create a new classification with auto-generated ID."""
        # Create a new Classification with an auto-generated ID
        classification = Classification(
            id=self._next_id,
            call_id=data.call_id,
            classification_category=data.classification_category,
        )
        
        # Store in the dictionary
        self._classifications[classification.id] = classification
        
        # Increment ID counter for next creation
        self._next_id += 1
        
        return classification
    
    def update(self, classification: Classification) -> Classification:
        """Update an existing classification."""
        existing_classification = self.get_by_id(classification.id)  # Ensure it exists
        
        # Store updated classification
        existing_classification = classification
        return existing_classification
    
    def delete(self, id: int) -> None:
        """Delete a classification by ID."""
        del self._classifications[id]
    
    def find_by_call_id(self, call_id: str) -> List[Classification]:
        """Find all classifications for a specific call ID."""
        classifications = [
            classification 
            for classification in self._classifications.values()
            if classification.call_id == call_id
        ]
    
        if classifications == []:
            raise ValueError(f"No classifications found for call ID {call_id}")
        return classifications

