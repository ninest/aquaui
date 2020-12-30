from aquaui.utils import run_applescript
from typing import List, Union


class ColorPicker:
    def __init__(self) -> None:
        self.applescript = "choose color "

    def with_default_color(self, color: List[int]):
        if color is not None:
            color_list = ", ".join(str(val) for val in color)
            self.applescript += f"default color {{ {color_list} }} "

        return self

    def show(self) -> Union[List[int], None]:
        try:
            result = run_applescript(self.applescript)
            color_array = list(map(int, result.replace("\n", "").split(", ")))
            return color_array
        except:
            # If cancelled using escape key
            return None
