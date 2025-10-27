from typing import Optional
from unittest.mock import MagicMock
from core.classifications.domain.ports import ClassificationRepository
import pytest

from core.classifications.domain.models import Category, Classification, ClassificationCategory, ClassificationCreate

# ==============================================================================
# 1. Mock Classes for Unit Tests
# ==============================================================================

class MockClassificationRepository(ClassificationRepository):
    """A fake repository that simulates database behavior for unit tests."""
    
    def get_by_id(self, id) -> Optional[Classification]:
        return Classification(
            call_id="1",
            category=Category.COMMERCIAL,
            id=id
        )
    
    def create(self, invoice_data: ClassificationCreate, external_ref: str) -> Classification:
        """Simulates creating an invoice and returning the full entity."""
        print("MOCK REPO: 'create' called.")
        
        return Classification(
            call_id="1",
            category=Category.COMMERCIAL,
            id=id
        )
        
    def update(self, classification: Classification) -> Classification:
        """Simulates updating an invoice in the database."""
        print("MOCK REPO: 'update' called.")
        return Classification(
            call_id="1",
            category=Category.COMMERCIAL,
            id=id
        )
    
    def delete(self, id: int) -> None:
        """Simulates deleting an invoice from the database."""
        print("MOCK REPO: 'delete' called.")
        pass
    
    def find_by_call_id(self, call_id) -> list[Classification]:
        return [
            Classification(
                call_id="1",
                category=Category.COMMERCIAL,
                id=id
            )
        ]
    

class MockOpenAIClassifierGateway:
    """A fake OpenAI gateway that simulates classification behavior for unit tests."""
    
    def classify(self, data: str) -> Category:
        """Simulates classifying text and returning a category."""
        print("MOCK GATEWAY: 'classify' called.")
        return Category.COMMERCIAL

# ==============================================================================
# 2. Pytest Fixtures
# ==============================================================================

@pytest.fixture(name="classification_repo")
def _classification_repo_fixture() -> MockClassificationRepository:
    """Provides a mock invoice repository for invoicing unit tests."""
    return MockClassificationRepository()

@pytest.fixture(name="anfix_gateway")
def _openai_classifier_gateway_fixture() -> MockOpenAIClassifierGateway:
    """Provides a mock Anfix gateway for invoicing unit tests."""
    return MockOpenAIClassifierGateway()

@pytest.fixture(name="classifications_dict", scope="function")
def _classifications_dict() -> dict[int, Classification]:
    """
    Provides a mock classifications dictionary for testing the
    InMemoryClassificationRepository.
    """
    return {
        1: Classification(
            id=1,
            call_id="call_1",
            classification_category=ClassificationCategory(category=Category.COMMERCIAL),
        ),
        2: Classification(
            id=2,
            call_id="call_2",
            classification_category=ClassificationCategory(category=Category.COMMERCIAL),
        ),
    }

@pytest.fixture()
def mock_pipeline_fixture(mocker) -> MagicMock:
    """
    A fixture that mocks the entire 'pipeline_start' object from the main module.

    This uses pytest-mock's 'mocker' to patch the object at its source,
    returning the mock. Tests can then inject this fixture to make assertions
    about how the pipeline was called, isolating the test from the pipeline's
    actual implementation.
    """
    return mocker.patch("fastpaip_app.application.main.pipeline_start")

@pytest.fixture
def mock_processor() -> MagicMock:
    """
    Provides a mock 'Processable' component.
    (Simulates a FunctionalProcessor in a real scenario).
    """
    return MagicMock()

@pytest.fixture
def mock_handler() -> MagicMock:
    """
    Provides a generic mock 'Handler' for chaining.
    (Simulates another StepHandler instance in a real scenario).
    """
    return MagicMock()