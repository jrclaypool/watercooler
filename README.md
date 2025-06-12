# watercooler

<img width=720 src="docs/watercooler.jpg">

A place for LLMs to talk

## Global Python Install

```shell
# From repo root dir, install watercooler package
pip install -e .
```

#### Venv Install

```shell
# From repo root dir, make a virtual env
python -m venv .venv
# Install watercooler package
pip install -e .
```

## Config

```
src/config/models - all the models available in the CLI
src/config/routes - API endpoints and internal file paths
```

## Command Line

The goal of `watercooler` is to provide a robust command-line interface for talking to LLMs.  
We strive to provide intuitive and comprehensive flags and script parameters.  
Focus on easy-of-typing and ease-of-scripting over all else.

### Options

```
usage: watercooler [-h] [--clear-history] [--history] [--save-chat] [--load-chat]
                   [--llm LLM] [--anthropic] [--mistral] [--openai] [--reasoning]
                   [--general] [--mini] [-t T] [--max-tokens MAX_TOKENS] [-v]
                   [prompt]

A place for LLMs to talk

positional arguments:
  prompt                The prompt to provide to the LLMs

options:
  -h, --help            show this help message and exit
  --clear-history       Equivalent to --history except creates a fresh history file.
  --history             Use the chat history. Equivalent to using both --save-chat and --load-chat
  --save-chat           Save the chat history (default: false)
  --load-chat           Load the chat history (default: false)
  --llm LLM             Specify a single model to use. Supported models: ['mistral-large-
                        latest', 'mistral-medium-latest', 'mistral-small-latest',
                        'claude-3-opus-latest', 'claude-3-5-sonnet-latest',
                        'claude-3-5-haiku-latest', 'gpt-4o', 'gpt-4.1', 'gpt-4o-mini']
  --anthropic           Use all the configured Anthropic models. Configured models:
                        ['claude-3-opus-latest', 'claude-3-5-sonnet-latest',
                        'claude-3-5-haiku-latest']
  --mistral             Use all the configured Mistral models. Configured models:
                        ['mistral-large-latest', 'mistral-medium-latest', 'mistral-small-
                        latest']
  --openai              Use all the configured OpenAI models. Configured models:
                        ['gpt-4o', 'gpt-4.1', 'gpt-4o-mini']
  --reasoning           Use all the configured reasoning models. Configured models: []
  --general             Use all the configured general models. Configured models:
                        ['mistral-large-latest', 'mistral-medium-latest', 'claude-3-opus-
                        latest', 'claude-3-5-sonnet-latest', 'claude-3-5-haiku-latest',
                        'gpt-4o']
  --mini                Use all the configured mini models. Configured models: ['mistral-
                        small-latest', 'gpt-4o-mini']
  -t T                  Temperature setting (0-1, default: 0.7)
  --max-tokens MAX_TOKENS, -m MAX_TOKENS
                        Maximum tokens per LLM response (default: 500)
  -v, --verbose         Display extra information in the responses (default: false)
```

## Options Plan
```
--anthropic = Run all the configured Anthropic models
--clear-history = Equivalent to --history except wipes the current history to a blank file.
-d, --debug = Flag to execute debug code
--debate (future) = Request the LLMs to debate a topic
-h, --help
--history = Saves and loads the chat history to the database. Equivalent to --save --load (default: false).
-j, --json = Request that the LLMs respond in JSON
-l, --long-print = Display extra information in the responses (default: false)
--llm = Specify a single model to use. Supported models:
--llms = Specify multiple models to use. Supported models:
-m, --max_tokens = Maximum tokens per LLM response (default: 500)
--mini = Run all the configured mini models
--mistral = Run all the configured Mistral models
-o, --options = JSON option string
--openai = Run all the configured OpenAI models
--reasoning = Run all the configured reasoning models
--save-chat = Save responses to the database (default: false)
--seed = Provide a seed (I think this nullifies temperature)
-t, --temperature = Temperature setting (0-1, default: 0.7)
--load-chat = Load the chat history from the database (default: false)
-v, --verbose = Show the maximum amount of info in the chat
```