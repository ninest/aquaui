from typing import List, Union
from ..utils import quotify


class Buttons:
    """Provider the buttons, default button, and cancel button for dialogs and alerts"""

    def __init__(
        self,
        buttons: List[str] = [],
        default_button: Union[str, None] = None,
        cancel_button: Union[str, None] = None,
    ) -> None:
        if (default_button is not None) and (default_button not in buttons):
            raise Exception("Default Button not in buttons list")

        if (cancel_button is not None) and (cancel_button not in buttons):
            raise Exception("Cancel Button not in buttons list")

        self.buttons = buttons
        self.default_button = default_button
        self.cancel_button = cancel_button

    @property
    def string(self):
        """Get a string of all buttons"""
        return ", ".join(map(quotify, self.buttons))
