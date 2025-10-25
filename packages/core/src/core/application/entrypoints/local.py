"""
Main application entry point and Composition Root.

This script instantiates all necessary components (repositories, handlers, etc.)
and assembles them into the final, unified Chain of Responsibility pipeline.
It also defines the `lambda_handler`, which is the entry point for AWS Lambda.
"""
from functools import partial
from typing import Any, Dict

# 1. Import plummy components
from plummy.handlers import StepHandler, Handler
from plummy.adapters import FunctionalProcessor

# 2. Import configuration and concrete infrastructure
from core.classifications.infrastructure.gateways import OpenAIClassifierGateway
from core.classifications.infrastructure.repositories import InMemoryClassificationRepository
from core.config.settings import settings

# 3. Import handler builders from each domain's application layer
from core.classifications.application.services import create_classification_service

# 4. Import cross-domain application services


# ==============================================================================
# --- Composition Root: Instantiate all dependencies ---
# ==============================================================================

# In a real application, the db_session would be created and managed here,
# often using a dependency injection container or a session factory.
# For this example, we'll use 'None' as a placeholder.
db_session = None

# Instantiate all concrete adapters
classification_repo = InMemoryClassificationRepository()
openai_classifier_gateway = OpenAIClassifierGateway(api_key=settings.openai_api.api_key)
# ==============================================================================
# --- Build all handler instances ---
# ==============================================================================

def can_handle_create_classification(event: Dict[str, Any]) -> bool:
    return event.get("type") == "newcall"

create_classification_func = partial(
    create_classification_service,
    classification_repo=classification_repo,
    llm_classifier=openai_classifier_gateway
    )

create_classification_processor = FunctionalProcessor(
    can_handle=can_handle_create_classification,
    process=create_classification_func
)

create_classification_handler=StepHandler(
    processor=create_classification_processor
)

# ==============================================================================
# --- Assemble the final, unified pipeline ---
# ==============================================================================

pipeline_start: Handler = create_classification_handler


# ==============================================================================
# --- Entry Point ---
# ==============================================================================

def app() -> None:
    
    event = {
        "type": "newcall",
        "text": "Customer called to inquire about pricing for bulk orders."
    }

    print(f"Received event: {event}")
    
    # Run the pipeline with the incoming event data
    result = pipeline_start.handle(event)
    
    # print(f"Pipeline result: {result}")
    
    # Return the result (important for synchronous invocations like API Gateway)
    return result