import asyncio.tasks

from watercooler.classes.tasker import SingleModeSettings
from watercooler.config.models import (
    DEFAULT_MISTRAL_MODEL,
    SUPPORTED_MODEL_NAMES,
    ANTHROPIC_MODEL_NAMES,
    OPENAI_MODEL_NAMES,
    MISTRAL_MODEL_NAMES,
)
from watercooler.platforms.anthropic import anthropic
from watercooler.platforms.mistral import mistral
from watercooler.platforms.openai import openai


def single_mode(prompt: str, settings: SingleModeSettings):
    tasks = []
    model = settings.model
    platform = "mistral"

    if model in ANTHROPIC_MODEL_NAMES:
        platform = "anthropic"
    elif model in OPENAI_MODEL_NAMES:
        platform = "openai"
    elif model in MISTRAL_MODEL_NAMES:
        platform = "mistral"

    if platform == "mistral":
        tasks.append(asyncio.tasks.create_task(mistral(prompt, settings)))
    elif platform == "openai":
        tasks.append(asyncio.tasks.create_task(openai(prompt, settings)))
    elif platform == "anthropic":
        tasks.append(asyncio.tasks.create_task(anthropic(prompt, settings)))
    else:
        tasks.append(asyncio.tasks.create_task(mistral(prompt, settings)))
    return tasks


def single_mode_settings(args) -> SingleModeSettings:
    # Verify model
    llm: str | None = None
    if args.llm:
        if args.llm not in SUPPORTED_MODEL_NAMES:
            print(f"Model {args.llm} is not supported.")
            raise TypeError
        llm = args.llm
    else:
        llm = DEFAULT_MISTRAL_MODEL

    # Verify temperature
    temperature: float = 0.7
    if args.temperature < 0 or args.temperature > 1:
        print("Temperature must be between 0 and 1.")
        raise TypeError
    else:
        temperature = args.temperature

    # Verify max tokens
    max_tokens: int = 500
    if args.max_tokens < 100:
        print("Max tokens must be at least 1.")
        raise TypeError
    else:
        max_tokens = args.max_tokens

    return SingleModeSettings(max_tokens=max_tokens, temperature=temperature, model=llm)
