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


def dialog(
    title: str, buttons: Union[Buttons, None] = None, icon: Union[str, Icon, None] = None, return_applescript=False
):
    """Show a dialog with an icon, text, and buttons"""

    applescript = f"display dialog {quotify(title)} "

    if buttons is not None:
        applescript += f"{buttons.applescript_fragment} "

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

        applescript += f"{applescript_fragment} "

    if return_applescript:
        return applescript

    """
    An error is thrown if the dialog gets cancelled by the escape key
    """
    try:
        return Result(run_applescript(applescript))
    except:
        return Result.escaped()


def dialog_prompt(
    title: str,
    default_text: str = "",
    buttons: Union[Buttons, None] = None,
    icon: Union[str, Icon, None] = None,
    return_applescript=False,
):
    """Show a dialog with an icon, text, input field, and buttons"""

    applescript = dialog(title, buttons, icon, return_applescript=True)  # Returns a string for sure

    applescript += 'default answer ""'  # type: ignore

    if return_applescript:
        return applescript

    # It seems that dialogs prompts cannot be canclled with the escape key
    return Result(run_applescript(applescript))
