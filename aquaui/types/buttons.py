from typing import List, Union
from ..utils import quotify


class Buttons:
    """Provide the buttons, default button, and cancel button for dialogs and alerts"""

    def __init__(
        self,
        buttons: List[str] = [],
        default_button: Union[str, None] = None,
        cancel_button: Union[str, None] = None,
    ) -> None:
        # Maximum 3 buttons
        if len(buttons) > 3:
            raise Exception("There can be a maximum of 3 buttons only")

        if (default_button is not None) and (default_button not in buttons):
            raise Exception("Default Button not in buttons list")

        if (cancel_button is not None) and (cancel_button not in buttons):
            raise Exception("Cancel Button not in buttons list")

        self.buttons = buttons
        self.default_button = default_button
        self.cancel_button = cancel_button

    @property
    def string(self) -> str:
        """Get a string of all buttons"""
        return ", ".join(map(quotify, self.buttons))

    @property
    def applescript_fragment(self) -> str:
        """Generate the applescript fragment for the button"""

        script_fragment = f"buttons {{ {self.string} }} "

        if self.default_button is not None:
            script_fragment += f"default button {quotify(self.default_button)} "
        if self.cancel_button is not None:
            script_fragment += f"cancel button {quotify(self.cancel_button)} "

        return script_fragment
