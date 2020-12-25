from typing import List, Union
from .utils import quotify, run_applescript


class Choice:
    def __init__(self, title: str) -> None:
        self.title = title
        self.applescript = "choose from list "

    def with_choices(self, choices: List[str] = []):
        self.choices = choices
        string_choices = "{%s}" % ", ".join(map(quotify, self.choices))
        self.applescript += f"{string_choices} "

        # Set title before showing: first choices need to be defined
        if self.title is not None:
            self.applescript += f"with prompt {quotify(self.title)} "

        return self

    def default_choice(self, default_choice: Union[str, None] = None):
        if default_choice is not None:
            if default_choice not in self.choices:
                raise Exception("The default_choice must be in choices")
            self.applescript += f"default items {{ {quotify(default_choice)} }} "

        return self

    def show(self) -> str:
        result = run_applescript(self.applescript).strip()
        if result == "false":
            result = ""
        return result
