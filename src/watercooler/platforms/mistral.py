import os

import aiohttp

from watercooler.classes.platforms import ChatResponse
from watercooler.classes.tasker import SingleModeSettings
from watercooler.config.routes import MISTRAL_API_URL


async def mistral(prompt: str, options: SingleModeSettings) -> ChatResponse:
    """

    :param prompt:
    :param options:
    :return:
    """
    api_key = os.environ.get("MISTRAL_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = {
        "model": options.model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": options.max_tokens,
        "temperature": options.temperature,
    }

    # try:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                MISTRAL_API_URL, headers=headers, json=data
            ) as response:
                response.raise_for_status()
                response_data = await response.json()
                return ChatResponse(
                    content=response_data["choices"][0]["message"]["content"],
                    platform="mistral",
                    model=options.model,
                )
    except Exception as e:
        # print(f"Error communicating with Mistral API: {e}")
        return ChatResponse(
            content="(No connection)", platform="mistral", model=options.model
        )
