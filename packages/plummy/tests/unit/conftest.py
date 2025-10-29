from unittest.mock import MagicMock
import pytest

# ==============================================================================
# 1. Mock Classes for Unit Tests
# ==============================================================================



# ==============================================================================
# 2. Pytest Fixtures
# ==============================================================================


@pytest.fixture(name="pipeline")
def _pipeline_fixture(mocker) -> MagicMock:
    """
    A fixture that mocks the entire 'pipeline_start' object from the main module.

    This uses pytest-mock's 'mocker' to patch the object at its source,
    returning the mock. Tests can then inject this fixture to make assertions
    about how the pipeline was called, isolating the test from the pipeline's
    actual implementation.
    """
    return mocker.patch("plummy.main.pipeline_start")

@pytest.fixture(name="processor")
def _processor_fixture() -> MagicMock:
    """
    Provides a mock 'Processable' component.
    (Simulates a FunctionalProcessor in a real scenario).
    """
    return MagicMock()

@pytest.fixture(name="handler")
def _handler_fixture() -> MagicMock:
    """
    Provides a generic mock 'Handler' for chaining.
    (Simulates another StepHandler instance in a real scenario).
    """
    return MagicMock()