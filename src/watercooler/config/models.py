# Model lists
from dataclasses import dataclass


# TODO: Add breakout by minis and reasoning models


@dataclass
class Model:
    name: str
    type: str

    # Display the name when printed
    def __repr__(self):
        return self.name


MISTRAL_MODELS: list[Model] = [
    Model("mistral-large-latest", "general"),
    Model("mistral-medium-latest", "general"),
    Model("mistral-small-latest", "mini"),
]
MISTRAL_MODEL_NAMES: list[str] = list(map(lambda x: x.name, MISTRAL_MODELS))
ANTHROPIC_MODELS: list[Model] = [
    Model("claude-3-opus-latest", "general"),
    Model("claude-3-5-sonnet-latest", "general"),
    Model("claude-3-5-haiku-latest", "general"),
]
ANTHROPIC_MODEL_NAMES: list[str] = list(map(lambda x: x.name, ANTHROPIC_MODELS))
OPENAI_MODELS: list[Model] = [
    Model("gpt-4o", "general"),
    Model("gpt-4.1", "genera"),
    Model("gpt-4o-mini", "mini"),
]
OPENAI_MODEL_NAMES: list[str] = list(map(lambda x: x.name, OPENAI_MODELS))

# All models supported by the API
SUPPORTED_MODELS: list[Model] = MISTRAL_MODELS + ANTHROPIC_MODELS + OPENAI_MODELS
SUPPORTED_MODEL_NAMES: list[str] = list(map(lambda x: x.name, SUPPORTED_MODELS))

MODELS_CONFIG = {
    "mistral": MISTRAL_MODELS,
    "anthropic": ANTHROPIC_MODELS,
    "openai": OPENAI_MODELS,
    "all": MISTRAL_MODELS + ANTHROPIC_MODELS + OPENAI_MODELS,
    "general": filter(lambda x: x.type == "general", SUPPORTED_MODELS),
    "reasoning": filter(lambda x: x.type == "reasoning", SUPPORTED_MODELS),
    "mini": filter(lambda x: x.type == "mini", SUPPORTED_MODELS),
}

# Model defaults
DEFAULT_MISTRAL_MODEL = MISTRAL_MODELS[1]
DEFAULT_ANTHROPIC_MODEL = ANTHROPIC_MODELS[2]
DEFAULT_OPENAI_MODEL = OPENAI_MODELS[1]
