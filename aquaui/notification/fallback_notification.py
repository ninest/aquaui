from typing import Union
from ..utils import quotify, run_applescript


class ApplescriptNotification:
    def __init__(self, title: Union[str, None] = None) -> None:

        self.applescript = "display notification "

        if title is not None:
            self.applescript += f"with title {quotify(title)} "

    def with_subtitle(self, subtitle: Union[str, None]):
        if subtitle is not None:
            self.applescript += f"subtitle {quotify(subtitle)} "

        return self

    def send(self):
        return run_applescript(self.applescript, no_return=True)
