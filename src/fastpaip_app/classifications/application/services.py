from typing import Any, Dict
from fastpaip_app.classifications.domain.models import ClassificationCreate
from fastpaip_app.classifications.domain.ports import ClassificationRepository, LLMClassifier
from fastpaip_app.classifications.domain.services import classify_text, create_classification
    
def can_handle_create_classification(event: Dict[str, Any]) -> bool:
    return event.get("type") == "newcall"

def create_classification_service(event: Dict[str, Any], classification_repo: ClassificationRepository, llm_classifier: LLMClassifier) -> dict:
    """
    Service function to classify data.

    This function would contain the core logic for classifying data.
    For demonstration purposes, it currently returns a placeholder response.

    Returns:
        A dictionary representing the classification result.
    """
    category = classify_text(text=event["text"], llm_classifier=llm_classifier)
    classification_create = ClassificationCreate(
        call_id="1",
        category=category
    )
    created_classification = create_classification(classification_data=classification_create, classification_repo=classification_repo)
    return created_classification