import subprocess
from typing import List, Union


def quotify(string):
    """Return the string with quotes

    >>> quotify("some string")
    '"some string"'
    """

    return f'"{string}"'


def run_command(command: Union[str, List]):
    """Run a command on the terminal and return the output"""

    result = subprocess.check_output(command)
    return result.decode("utf-8")


def run_applescript(script: str, no_return: bool = False):
    """Run an applescript

    Set no_return to True to run an AppleScript that doesn't show a response, such as notifications
    """

    # Escape quotes
    # script = script.replace('"', '\\"')

    command = ["osascript", "-e"]

    # Notifications don't get an answer in applescrip
    if no_return:
        command.append(script)
    else:
        command.append(f"set answer to {script}\nreturn answer")

    return run_command(command)
