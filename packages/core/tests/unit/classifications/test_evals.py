from core.classifications.domain.models import Category, ClassificationCategory
from core.classifications.infrastructure.gateways import OpenAIClassifierGateway

from core.config.settings import settings


def test_commercial_categorization():
    classifier = OpenAIClassifierGateway(api_key=settings.openai_api.api_key)
    classification_category = classifier.classify(
        text="Do you want a new car?",
        category=ClassificationCategory
    )
    assert classification_category.category == Category.COMMERCIAL
    
    
def test_following_categorization():
    classifier = OpenAIClassifierGateway(api_key=settings.openai_api.api_key)
    classification_category = classifier.classify(
        text="I want to follow-up on my previous inquiry.",
        category=ClassificationCategory
    )
    assert classification_category.category == Category.FOLLOWING