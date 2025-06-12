from watercooler.classes.platforms import ChatResponse
from watercooler.formatting.helpers import style_text, get_platform_color
from watercooler.history.database import write_history


# TODO: Add runtime / usage info
def print_response(response: ChatResponse, verbose: bool = False, save: bool = False):
    model = response.model
    platform = response.platform
    content = response.content
    color = get_platform_color(platform)
    if verbose:
        print_string = (
            f"{style_text(f"{platform.upper()} ({model})", color=color)}: {content}\n"
        )
    else:
        print_string = f"{style_text(f"{platform.upper()}", color=color)}: {content}\n"
    if save:
        write_history(print_string)
    print(print_string)
