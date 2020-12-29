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


class Dialog:
    def __init__(self, text: str) -> None:
        """Start generation of applescript for dialog"""

        self.applescript = f"display dialog {quotify(text)} "

    def with_title(self, title: str):
        self.applescript += f"with title {quotify(title)} "
        return self

    def with_buttons(self, buttons: Union[Buttons, None] = None):
        """If buttons is None, default buttons are displayed"""

        if buttons is not None:
            self.applescript += f"{buttons.applescript_fragment} "

        return self

    def with_icon(self, icon: Union[str, Icon] = None):
        """Use custom icons or built-in icons"""

        applescript_fragment: str
        if icon is not None:
            if isinstance(icon, str):
                # TODO: also support absolute file paths
                icon_path = icon
                applescript_fragment = f"with icon POSIX file {quotify(icon_path)}"

            # applescript built in icon
            elif isinstance(icon, Icon):
                applescript_fragment = f"with icon {icon.value}"

            else:
                raise Exception("Incorrect datatype for property icon")

            self.applescript += f"{applescript_fragment} "

        return self

    def with_input(self, default_response: str = ""):
        """Specify default answer"""

        self.applescript += f"default answer {quotify(default_response)} "
        return self

    def show(self):
        try:
            return Result(run_applescript(self.applescript))
        except:
            # On some cases, the dislog can be dismissed with the escape key,
            # and an error is thrown
            return Result.escaped()
