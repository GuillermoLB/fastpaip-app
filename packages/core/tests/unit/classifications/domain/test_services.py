from core.classifications.domain.services import classify_text
from core.classifications.domain.models import ClassificationCategory, ClassificationCreate
from core.classifications.domain.services import create_classification

def test_classify_text_calls_llm_classifier(llm_classifier):
    """
    Tests the 'classify_text' domain service function.
    Ensures it correctly calls LLMClassifier
    """
    input_text = "Sample text"
    classify_text(text=input_text, llm_classifier=llm_classifier)
    
    llm_classifier.classify.assert_called_once_with(
        text=input_text,
        category=ClassificationCategory
    )

def test_create_classification_calls_repository(classification_repo, mocker):
    """
    Tests the 'create_classification' domain service function.
    Ensures it correctly calls ClassificationRepository.
    """
    classification_create = ClassificationCreate(
                                call_id="123",
                                classification_category=ClassificationCategory(category="COMMERCIAL")
                            )
    

    create_classification(
        classification_data=classification_create,
        classification_repo=classification_repo
    )
    
    classification_repo.create.assert_called_once_with(classification_create)