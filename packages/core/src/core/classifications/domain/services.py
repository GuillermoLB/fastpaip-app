"""
Contains the core business logic (domain services) for the Classification domain.

These functions are pure, stateless, and decoupled from any infrastructure concerns.
They operate solely on domain models and depend on abstract ports for any
external interactions (like data persistence or API calls).
"""
from .models import Category, Classification, ClassificationCreate, ClassificationCategory
from .ports import ClassificationRepository, LLMClassifier

def classify_text(text: str, llm_classifier: LLMClassifier) -> Category:
    """
    Classifies the given text using the provided LLM classifier.

    Args:
        text (str): The text to classify.
        llm_classifier (LLMClassifier): The LLM classifier to use.

    Returns:
        Classification: The classification result.
    """
    print("DOMAIN SERVICE: Executing 'classify_text' logic...")
    # Use a keyword argument for the response model
    classification_result = llm_classifier.classify(
        text=text, category=ClassificationCategory
    )
    return classification_result

def create_classification(
    classification_data: ClassificationCreate,
    classification_repo: ClassificationRepository,
) -> Classification:

    print("DOMAIN SERVICE: Executing 'create_classification' logic...")
    created_classification = classification_repo.create(classification_data)

    return created_classification