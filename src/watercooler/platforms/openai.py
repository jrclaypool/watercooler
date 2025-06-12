import os

import aiohttp

from watercooler.classes.platforms import ChatResponse
from watercooler.classes.tasker import SingleModeSettings
from watercooler.config.routes import OPENAI_API_URL


async def openai(prompt: str, options: SingleModeSettings):
    """
    Send a prompt to the OpenAI API and get a response.

    Args:
        prompt (str): The message to send to the model

    Returns:
        str: The model's response text
        :param prompt:
        :param options:
    """
    api_key = os.environ.get("OPENAI_API_KEY")

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    data = {
        "model": options.model,
        "messages": [{"role": "user", "content": prompt}],
        "max_completion_tokens": options.max_tokens,
        "temperature": options.temperature,
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                OPENAI_API_URL, headers=headers, json=data
            ) as response:
                response.raise_for_status()
                response_data = await response.json()
                return ChatResponse(
                    content=response_data["choices"][0]["message"]["content"],
                    platform="openai",
                    model=options.model,
                )
    except Exception as e:
        # print(f"Error communicating with OpenAI API: {e}")
        return ChatResponse(
            content="(No connection)", platform="openai", model=options.model
        )
