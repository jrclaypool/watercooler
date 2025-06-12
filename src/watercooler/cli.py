# mistral_cli.py
import argparse
import asyncio
import sys

from watercooler.classes.formatting import Colors
from watercooler.classes.platforms import ChatResponse
from watercooler.classes.tasker import SingleModeSettings
from watercooler.config.helpers import load_api_keys
from watercooler.config.models import (
    MISTRAL_MODELS,
    OPENAI_MODELS,
    ANTHROPIC_MODELS,
    MODELS_CONFIG,
    ANTHROPIC_MODEL_NAMES,
    MISTRAL_MODEL_NAMES,
    OPENAI_MODEL_NAMES,
    SUPPORTED_MODEL_NAMES,
)
from watercooler.formatting.helpers import style_text
from watercooler.history.database import read_history, clear_history, write_history
from watercooler.platforms.print_response import print_response
from watercooler.tasker.feed_mode import feed_mode
from watercooler.tasker.single_mode import single_mode, single_mode_settings


async def main():
    parser = argparse.ArgumentParser(
        prog="watercooler",
        description="A place for LLMs to talk",
        epilog="Created by Jonathan Claypool",
    )

    parser.add_argument(
        "prompt", nargs="?", type=str, help="The prompt to provide to the LLMs"
    )
    # Chat Settings
    parser.add_argument(
        "--clear-history",
        action="store_true",
        help="Equivalent to --history except creates a fresh history file",
    )
    parser.add_argument(
        "--history",
        action="store_true",
        help="Use the chat history. Equivalent to using both --save-chat and --load-chat",
    )
    parser.add_argument(
        "--save-chat",
        action="store_true",
        help="Save the chat history (default: false)",
    )
    parser.add_argument(
        "--load-chat",
        action="store_true",
        help="Load the chat history (default: false)",
    )
    # Model Selection Settings
    parser.add_argument(
        "--llm",
        type=str,
        help=f"Specify a single model to use. Supported models: {SUPPORTED_MODEL_NAMES} ",
    )
    parser.add_argument(
        "--anthropic",
        action="store_true",
        help=f"Use all the configured Anthropic models. Configured models: {ANTHROPIC_MODEL_NAMES}",
    )
    parser.add_argument(
        "--mistral",
        action="store_true",
        help=f"Use all the configured Mistral models. Configured models: {MISTRAL_MODEL_NAMES}",
    )
    parser.add_argument(
        "--openai",
        action="store_true",
        help=f"Use all the configured OpenAI models. Configured models: {OPENAI_MODEL_NAMES}",
    )
    parser.add_argument(
        "--reasoning",
        action="store_true",
        help=f"Use all the configured reasoning models. Configured models: {list(map(lambda x: x.name, MODELS_CONFIG['reasoning']))}",
    )
    parser.add_argument(
        "--general",
        action="store_true",
        help=f"Use all the configured general models. Configured models: {list(map(lambda x: x.name, MODELS_CONFIG["general"]))}",
    )
    parser.add_argument(
        "--mini",
        action="store_true",
        help=f"Use all the configured mini models. Configured models: {list(map(lambda x: x.name, MODELS_CONFIG['mini']))}",
    )
    parser.add_argument(
        "-t",
        type=float,
        default=0.7,
        help="Temperature setting (0-1, default: 0.7)",
    )
    parser.add_argument(
        "--max-tokens",
        "-m",
        type=int,
        default=500,
        help="Maximum tokens per LLM response (default: 500)",
    )

    # Visual Settings
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Display extra information in the responses",
    )

    args = parser.parse_args()

    # Verify prompt
    if not args.prompt:
        parser.print_help()
        sys.exit(1)

    # Verify history
    if args.history or args.clear_history:
        args.save_chat = True
        args.load_chat = True
    if args.clear_history:
        clear_history()

    prompt = args.prompt
    if args.load_chat:
        history = read_history()
        if len(history) > 1:
            prompt = prompt + f"\n\nHere is the conversation so far:\n{history}"

    # Choose mode
    if args.llm:
        # (OPTION 1) Single model only
        settings: SingleModeSettings = single_mode_settings(args)  # Extract settings
        tasks = single_mode(prompt, settings)  # One response
    elif args.mini:
        tasks = feed_mode(prompt, MODELS_CONFIG["mini"])
    elif args.mini:
        tasks = feed_mode(prompt, MODELS_CONFIG["mini"])
    elif args.openai:
        tasks = feed_mode(prompt, MODELS_CONFIG["openai"])
    elif args.anthropic:
        tasks = feed_mode(prompt, MODELS_CONFIG["anthropic"])
    elif args.mistral:
        tasks = feed_mode(prompt, MODELS_CONFIG["mistral"])
    elif args.reasoning:
        tasks = feed_mode(prompt, MODELS_CONFIG["reasoning"])
    elif args.general:
        tasks = feed_mode(prompt, MODELS_CONFIG["general"])
    else:
        # (OPTION 2) Multiple model responses
        tasks = feed_mode(
            prompt, [OPENAI_MODELS[0], ANTHROPIC_MODELS[0], MISTRAL_MODELS[0]]
        )  # One response per platform

    # Print your prompt
    you_string = f"\n{style_text("You:", color=Colors.GREEN)} {args.prompt}\n-----"
    if args.save_chat:
        write_history(you_string)
    print(you_string)

    # Print the responses
    for completed_task in asyncio.as_completed(tasks):
        result: ChatResponse = await completed_task
        if (
            result.content != "(No connection)"
        ):  # TODO: Flag to remove blank connections
            print_response(
                result, args.verbose, args.save_chat
            )  # Save response to database


def run_main():
    """Entry point for the CLI
    Creates a synchronous wrapper around the async main function.
    """
    load_api_keys()
    return asyncio.run(main())


if __name__ == "__main__":
    run_main()
