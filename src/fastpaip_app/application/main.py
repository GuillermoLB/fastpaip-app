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
from fastpaip_app.config.settings import settings
from fastpaip_app.classifications.infrastructure.repositories import SQLClassificationRepository
from fastpaip_app.infrastructure.gateways import OpenAIGateway

# 3. Import handler builders from each domain's application layer
from fastpaip_app.classifications.application.classification_service import classify_text

# 4. Import cross-domain application services


# ==============================================================================
# --- Composition Root: Instantiate all dependencies ---
# ==============================================================================

# In a real application, the db_session would be created and managed here,
# often using a dependency injection container or a session factory.
# For this example, we'll use 'None' as a placeholder.
db_session = None

# Instantiate all concrete adapters
classification_repo = SQLClassificationRepository(db_session=db_session)
anfix_gateway = OpenAIGateway(
    api_key=settings.openai_api.api_key
)

# ==============================================================================
# --- Build all handler instances ---
# ==============================================================================

process_classification_func = partial(
    process_classification
    )

# Build the domain-specific handlers
sqs_invoice_handler = build_classification_handler(
    repository=classification_repo,
    sqs_parser=parse_sqs_event
)
api_invoice_handler = build_api_gateway_invoice_handler(repository=invoice_repo)
api_client_handler = build_api_gateway_client_handler(repository=client_repo)

# Build the cross-domain (ACL) handler
get_client_invoices_service_func = partial(
    get_client_invoices_service,
    client_repo=client_repo,
    invoice_repo=invoice_repo
)
get_client_invoices_processor = FunctionalProcessor(
    can_handle=can_handle_get_client_invoices,
    process=get_client_invoices_service_func
)
get_client_invoices_handler = StepHandler(processor=get_client_invoices_processor)

# ==============================================================================
# --- Assemble the final, unified pipeline ---
# ==============================================================================

pipeline_start: Handler = sqs_invoice_handler
sqs_invoice_handler.set_next(api_invoice_handler)
api_invoice_handler.set_next(api_client_handler)
api_client_handler.set_next(get_client_invoices_handler)


# ==============================================================================
# --- AWS Lambda Entry Point ---
# ==============================================================================

def lambda_handler(event: Dict[str, Any], context: object) -> Dict[str, Any]:
    """
    Main entry point for the Lambda function.

    It receives an event from a trigger (like SQS or API Gateway) and
    passes it to the start of the Chain of Responsibility pipeline.

    Args:
        event: The event data from the AWS service.
        context: The Lambda runtime context object.

    Returns:
        The result of the pipeline execution.
    """
    print(f"Received event: {event}")
    
    # Run the pipeline with the incoming event data
    result = pipeline_start.handle(event)
    
    print(f"Pipeline result: {result}")
    
    # Return the result (important for synchronous invocations like API Gateway)
    return result