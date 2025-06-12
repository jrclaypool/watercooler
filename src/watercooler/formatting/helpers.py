from watercooler.classes.formatting import Colors


def style_text(text, color=None, bold=False):
    """
    Apply styling to text with specified color and/or bold formatting.

    Args:
        text (str): The text to style
        color (str, optional): Color to apply from Colors class
        bold (bool, optional): Whether to make text bold

    Returns:
        str: Styled text
    """
    styled = ""
    if color:
        styled += color
    if bold:
        styled += "\033[1m"  # Bold ANSI code

    styled += text + Colors.RESET
    return styled


def get_platform_color(platform: str):
    if platform == "anthropic":
        return Colors.PURPLE
    elif platform == "openai":
        return Colors.RED
    elif platform == "mistral":
        return Colors.BLUE
    else:
        return Colors.RED
