from dataclasses import dataclass


@dataclass
class ChatResponse:
    content: str
    platform: str
    model: str
