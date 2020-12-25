from .types.buttons import Buttons
from .types.result import Result
from .utils import quotify, run_applescript


def dialog(title: str, buttons: Buttons):
    """Show a dialog with an icon, text, and buttons"""

    applescript = f"display dialog {quotify(title)} {buttons.applescript_fragment}"
    return Result(run_applescript(applescript))


def dialog_prompt():
    """Show a dialog with an icon, text, input field, and buttons"""
    pass
