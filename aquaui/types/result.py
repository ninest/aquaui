from typing import Union


class Result:
    def __init__(self, string_result: Union[str, None], cancelled=False) -> None:
        self.button_returned: str = ""
        self.text_returned: str = ""
        self.cancelled = cancelled

        # Set attributes based on output
        if string_result is not None:
            for data in string_result.split(","):
                data = data.strip()

                key, value = data.split(":")
                key = key.replace(" ", "_")

                # setattr(self, key, value)
                if key == "button_returned":
                    self.button_returned = value
                elif key == "text_returned":
                    self.text_returned = value

    @staticmethod
    def escaped():
        """Used when dialog is cancelled with escape key"""

        return Result(None, cancelled=True)
