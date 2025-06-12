import os

import aiohttp

from watercooler.classes.platforms import ChatResponse
from watercooler.classes.tasker import SingleModeSettings
from watercooler.config.routes import ANTHROPIC_API_URL


async def anthropic(prompt, options: SingleModeSettings) -> ChatResponse:
    """
    Send a prompt to the Anthropic Claude API and get a response.

    Args:
        prompt (str): The message to send to the model

    Returns:
        str: The model's response text
        :param prompt:
        :param options:
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }

    data = {
        "model": options.model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": options.max_tokens,
        "temperature": options.temperature,
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                ANTHROPIC_API_URL, headers=headers, json=data
            ) as response:
                response.raise_for_status()
            response_data = await response.json()
            return ChatResponse(
                content=response_data["content"][0]["text"],
                platform="anthropic",
                model=options.model,
            )
    except Exception as e:
        # print(f"Error communicating with Anthropic API: {e}")
        return ChatResponse(
            content="(No connection)", platform="anthropic", model=options.model
        )
