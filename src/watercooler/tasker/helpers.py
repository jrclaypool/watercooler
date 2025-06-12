import asyncio

from watercooler.classes.tasker import SingleModeSettings
from watercooler.config.models import (
    ANTHROPIC_MODELS,
    OPENAI_MODELS,
    MISTRAL_MODELS,
    Model,
)
from watercooler.platforms.anthropic import anthropic
from watercooler.platforms.mistral import mistral
from watercooler.platforms.openai import openai


def get_task_by_model(prompt: str, model: Model):
    platform = None
    settings = SingleModeSettings(model=model.name, max_tokens=500, temperature=0.7)
    if model in ANTHROPIC_MODELS:
        platform = "anthropic"
    elif model in OPENAI_MODELS:
        platform = "openai"
    elif model in MISTRAL_MODELS:
        platform = "mistral"

    if platform == "mistral":
        return asyncio.tasks.create_task(mistral(prompt, settings))
    elif platform == "openai":
        return asyncio.tasks.create_task(openai(prompt, settings))
    elif platform == "anthropic":
        return asyncio.tasks.create_task(anthropic(prompt, settings))
    else:
        raise Exception
