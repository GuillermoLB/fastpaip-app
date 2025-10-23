

from fastpaip_app.classifications.infrastructure.repositories import InMemoryClassificationRepository


def test_in_memory_classification_repository_get_classification_by_id(classifications_dict):
    repo = InMemoryClassificationRepository(classifications_dict)
    classification = repo.get_by_id(1)
    assert classification is not None
    assert classification.id == 1