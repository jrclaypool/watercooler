from dataclasses import dataclass
from typing import Optional


@dataclass
class SingleModeSettings:
    # TODO: Add `seed`, 'json'
    model: str
    temperature: float
    max_tokens: int
    seed: Optional[int] = None
    json: bool = False


@dataclass
class MultiModeSettings:
    # TODO: Allow for providing a model list to run all such models
    mistral_model_settings: SingleModeSettings
    openai_model_settings: SingleModeSettings
    anthropic_model_settings: SingleModeSettings
