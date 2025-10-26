from core.classifications.domain.models import ClassificationCreate
from core.classifications.infrastructure.repositories import InMemoryClassificationRepository


def test_in_memory_classification_repository_get_classification_by_id(classifications_dict):
    repo = InMemoryClassificationRepository(classifications_dict)
    classification = repo.get_by_id(1)
    assert classification is not None
    assert classification.id == 1
    
def test_in_memory_classification_repository_create_classification():
    repo = InMemoryClassificationRepository()
    classification_create = ClassificationCreate(
        call_id="call_3",
        classification_category={"category": "FOLLOWING"}
    )
    new_classification = repo.create(
        data = classification_create
    )
    assert new_classification.call_id == "call_3"
    assert new_classification.classification_category.category == "FOLLOWING"
    
def test_in_memory_classification_repository_update_classification(classifications_dict):
    repo = InMemoryClassificationRepository(classifications_dict)
    classification = repo.get_by_id(1)
    classification.classification_category.category = "FOLLOWING"
    updated_classification = repo.update(classification)
    assert updated_classification.classification_category.category == "FOLLOWING"
    
def test_in_memory_classification_repository_delete_classification(classifications_dict):
    repo = InMemoryClassificationRepository(classifications_dict)
    repo.delete(1)
    classification = repo.get_by_id(1)
    assert classification is None