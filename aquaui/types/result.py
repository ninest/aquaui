class Result:
    def __init__(self, string_result) -> None:
        self.button = None
        self.text = None

        """Go through results and set attributes accordingly"""

        for data in string_result.split(","):
            data = data.strip()

            key, value = data.split(":")
            key = key.replace(" ", "_")

            if key == "button_returned":
                self.button = value
            elif key == "text_returned":
                self.text = value
            else:
                setattr(self, key, value)
