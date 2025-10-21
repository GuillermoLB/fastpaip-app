"""
Contains the core business logic (domain services) for the Classification domain.

These functions are pure, stateless, and decoupled from any infrastructure concerns.
They operate solely on domain models and depend on abstract ports for any
external interactions (like data persistence or API calls).
"""
from .models import Classification, ClassificationCreate
from .ports import ClassificationRepository, LLMClassifier


def create_classification(
    classification_data: ClassificationCreate,
    classification_repo: ClassificationRepository,
    llm_classifier: LLMClassifier
) -> Classification:

    print("DOMAIN SERVICE: Executing 'create_classification' logic...")
    classification = llm_classifier.classify(classification_data)
    created_classification = classification_repo.create(classification)

    return created_classification