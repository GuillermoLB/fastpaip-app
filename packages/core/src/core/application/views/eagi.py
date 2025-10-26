from functools import partial

from core.classifications.application.services import create_classification_service
from core.classifications.infrastructure.gateways import OpenAIClassifierGateway
from core.classifications.infrastructure.repositories import InMemoryClassificationRepository
from core.config import settings
from plummy.adapters import FunctionalProcessor
from plummy.handlers import Handler, StepHandler

# –-------------------------------------------------------------------------------
# --- Composition Root: Instantiate all dependencies ---
# –-------------------------------------------------------------------------------

classification_repo = InMemoryClassificationRepository()
openai_classifier_gateway = OpenAIClassifierGateway(api_key=settings.openai_api.api_key)

# –-------------------------------------------------------------------------------
# --- Define validators ---
# –-------------------------------------------------------------------------------

def can_handle_newcall_event(event):
    """
    Determine if the given event is a Newcall event that can be handled.

    Args:
        event (dict): The event data.

    Returns:
        bool: True if the event is a Newcall event, False otherwise.
    """
    return event.get("source") == "newcall"

# –-------------------------------------------------------------------------------
# --- Build services ---
# –-------------------------------------------------------------------------------

create_classification_func = partial(
    create_classification_service,
    classification_repo=classification_repo,
    llm_classifier=openai_classifier_gateway
    )

# –-------------------------------------------------------------------------------
# --- Make it "Processable" ---
# –-------------------------------------------------------------------------------

create_classification_processor = FunctionalProcessor(
    can_handle=can_handle_newcall_event,
    process=create_classification_func
)

# –-------------------------------------------------------------------------------
# --- Make it "Processable" ---
# –-------------------------------------------------------------------------------

create_classification_handler=StepHandler(
    processor=create_classification_processor
)

pipeline_start: Handler = create_classification_handler