from typing import Type
import openai
from pydantic import BaseModel
from core.classifications.domain.models import Category, ClassificationCategory
from core.classifications.domain.ports import LLMClassifier

def extract_category_choices(
    output_model: type[BaseModel], field_name: str = "category"
) -> str:
    category_field = output_model.model_fields[field_name]
    category_enum = category_field.annotation
    if hasattr(category_enum, "__members__"):
        return ", ".join(category_enum.__members__.keys())
    return str(category_enum)


class OpenAIClassifierGateway(LLMClassifier):
    """
    A concrete adapter that implements the 'CanClassify' port
    using the OpenAI API.
    """
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def classify(self, text: str, category: Type[BaseModel]) -> ClassificationCategory:
        """Uses the OpenAI API to classify the given text."""
        print("INFRASTRUCTURE (OpenAI): Classifying text...")
        categories_str = extract_category_choices(category)
        response_model=category
        messages=[
            {
                "role": "system",
                "content": f"Classify the following text into one of the following categories: {categories_str}",
            },
            {"role": "user", "content": f"Classify this text:\n\n{text}"},
        ]
        response_params = {
            "model": self.model,
            "input": messages,
            "text_format": response_model,
        }
        response = self.client.responses.parse(**response_params)
        return response.output[0].content[0].parsed