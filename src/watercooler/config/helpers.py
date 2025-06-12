import os

from watercooler.config.routes import ENV_FILE


def load_api_keys():
    """Get the Mistral API key from environment variable or user input."""
    with open(ENV_FILE) as environment_file:
        for line in environment_file:
            os.environ[line.split("=")[0]] = line.split("=")[1].strip()
