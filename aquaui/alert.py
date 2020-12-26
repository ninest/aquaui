from enum import Enum, unique
from typing import Union
from aquaui.utils import quotify, run_applescript
from .types.buttons import Buttons
from .types.result import Result


@unique
class AlertType(Enum):
    INFORMATIONAL = "informational"
    CRITICAL = "critical"

    """
    WARNING = "warning"
    Warning seems to be the same as informational on Big Sur
    """


class Alert:
    """
    Returns an object of type Result, which as a button_returned property.
    """

    def __init__(self, title: str) -> None:
        self.applescript = f"display alert {quotify(title)} "

    def with_buttons(self, buttons: Union[Buttons, None] = None):
        """
        If a default button is not specified, the last button is the list will become the default.

        If buttons is None, default buttons are displayed
        """

        if buttons is not None:
            self.applescript += f"{buttons.applescript_fragment}"

        return self

    def of_type(self, alert_type: AlertType = AlertType.INFORMATIONAL):
        """Different alert types use different icons"""

        self.applescript += f"as {alert_type.value} "
        return self

    def show(self) -> Result:
        try:
            return Result(run_applescript(self.applescript))
        except:
            return Result.escaped()
