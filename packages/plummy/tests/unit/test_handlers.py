"""Unit tests for the Handler classes in the shared framework."""
from plummy.handlers import StepHandler

def test_step_handler_processes_when_can_handle_is_true(
    processor, handler
):
    """
    Tests that StepHandler calls its processor and the next handler
    when can_handle() returns True.
    """
    # 1. Arrange
    processor.can_handle.return_value = True
    test_data = {"key": "value"}

    # Create the handler instance we are testing
    first_handler = StepHandler(processor=processor)
    first_handler.set_next(handler)

    # 2. Act
    first_handler.handle(test_data)

    # 3. Assert
    # Verify the processor was called as expected
    processor.can_handle.assert_called_once_with(test_data)
    processor.process.assert_called_once_with(test_data)
    
    # Verify the chain continued
    handler.handle.assert_called_once()


def test_step_handler_skips_when_can_handle_is_false(
    processor, handler
):
    """
    Tests that StepHandler skips its processor but still calls the next handler
    when can_handle() returns False.
    """
    # 1. Arrange
    processor.can_handle.return_value = False
    test_data = {"key": "value"}

    first_handler = StepHandler(processor=processor)
    first_handler.set_next(handler)

    # 2. Act
    first_handler.handle(test_data)

    # 3. Assert
    # Verify the processor's 'can_handle' was checked, but 'process' was not called
    processor.can_handle.assert_called_once_with(test_data)
    processor.process.assert_not_called()

    # Verify the chain still continued
    handler.handle.assert_called_once_with(test_data)
    

def test_step_handler_at_end_of_chain(processor):
    """
    Tests that a StepHandler correctly processes data and returns the result
    when it is the last handler in the chain (i.e., no next_handler is set).
    """
    # 1. Arrange
    test_data = {"status": "new"}
    processed_data = {"status": "processed"}

    # Configure the mock processor to accept the data and return a specific result
    processor.can_handle.return_value = True
    processor.process.return_value = processed_data

    # Create the handler instance, but DO NOT set a next handler
    handler = StepHandler(processor=processor)

    # 2. Act
    result = handler.handle(test_data)

    # 3. Assert
    # Verify that the processor's methods were called correctly
    processor.can_handle.assert_called_once_with(test_data)
    processor.process.assert_called_once_with(test_data)

    # Verify that the final result is the data returned by our processor
    assert result == processed_data