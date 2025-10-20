"""
Contains the core business logic (domain services) for the Invoicing domain.

These functions are pure, stateless, and decoupled from any infrastructure concerns.
They operate solely on domain models and depend on abstract ports for any
external interactions (like data persistence or API calls).
"""
import uuid
from datetime import datetime, timezone
from .models import Invoice, InvoiceCreate, InvoiceStatus
from .ports import InvoiceRepository, AnfixGateway

def create_invoice(
    invoice_data: InvoiceCreate,
    repository: InvoiceRepository,
    anfix_gateway: AnfixGateway
) -> Invoice:
    """
    Core business logic for creating a new invoice.

    This service encapsulates the rules for invoice creation, such as generating
    a unique external reference, persisting the new invoice via the repository,
    and notifying an external accounting system via the gateway.

    Args:
        invoice_data: The validated data for the new invoice.
        repository: An object that fulfills the InvoiceRepository port contract.
        anfix_gateway: An object that fulfills the AnfixGateway port contract.

    Returns:
        The newly created and persisted Invoice entity.
    """
    print("DOMAIN SERVICE: Executing 'create_invoice' logic...")

    external_ref = f"INV-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}-{str(uuid.uuid4())[:6]}"
    created_invoice = repository.create(invoice_data, external_ref=external_ref)
    created_invoice.reference = created_invoice.external_ref

    try:
        anfix_gateway.create_invoice(created_invoice)
    except Exception as e:
        print(f"Warning: Anfix call failed: {e}")

    return created_invoice


def issue_invoice(
    invoice: Invoice,
    repository: InvoiceRepository
) -> Invoice:
    """
    Core business logic for issuing an invoice after a successful payment.

    This service enforces the business rule that a paid invoice's status
    should be changed to 'ISSUED'.

    Args:
        invoice: The invoice entity to be issued.
        repository: An object that fulfills the InvoiceRepository port contract.

    Returns:
        The updated Invoice entity.
    """
    print("DOMAIN SERVICE: Executing 'issue_invoice' logic...")

    # Core Business Rule: Update status to reflect it's officially issued.
    invoice.status = InvoiceStatus.ISSUED
    
    # Delegate the update to the repository port.
    updated_invoice = repository.update(invoice)
    
    return updated_invoice