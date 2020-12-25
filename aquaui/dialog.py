from typing import Union
from enum import Enum, unique
from .types.buttons import Buttons
from .types.result import Result
from .utils import quotify, run_applescript


@unique
class Icon(Enum):
    NOTE = "note"
    CAUTION = "caution"
    STOP = "stop"


def dialog(title: str, buttons: Buttons, icon: Union[str, Icon, None] = None):
    """Show a dialog with an icon, text, and buttons"""

    applescript = f"display dialog {quotify(title)} {buttons.applescript_fragment} "

    applescript_fragment: str
    if icon is not None:
        # relative path
        if isinstance(icon, str):

            # TODO: also support absolute file paths
            # pwd = run_command("pwd")
            # icon_path = f"{pwd}/{icon}"
            # icon_path = os.path.join(pwd, icon)

            icon_path = icon
            applescript_fragment = f"with icon POSIX file {quotify(icon_path)}"

        # applescript built in icon
        elif isinstance(icon, Icon):
            applescript_fragment = f"with icon {icon.value}"

        else:
            raise Exception("Incorrect datatype for property icon")

        applescript += applescript_fragment

    return Result(run_applescript(applescript))


def dialog_prompt():
    """Show a dialog with an icon, text, input field, and buttons"""
    pass
