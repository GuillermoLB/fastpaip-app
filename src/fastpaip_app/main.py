from typing import Any, Dict


def lambda_handler(event: Dict[str, Any], context: Any) -> Any:
    if "pipeline_start" not in globals():
        raise RuntimeError("Pipeline not initialized. Ensure that the application is properly set up.")