import subprocess


def quotify(string):
    """Return the string with quotes

    >>> quotify("some string")
    '"some string"'
    """

    return f'"{string}"'


def run_command(command: str):
    """Run a command on the terminal and return the output"""

    result = subprocess.check_output(command, shell=True)
    return result.decode("utf-8")


def run_applescript(script: str, no_return: bool = False):
    """Run an applescript

    Set no_return to True to run an AppleScript that doesn't show a response, such as notifications
    """

    # escape quotes
    script = script.replace('"', '\\"')

    command = f"""
        osascript -e "\
            set answer to {script}
            return answer
        "
    """

    print(command)

    # Notifications don't get an "answer"
    if no_return:
        command = f"""
            osascript -e "\
                {script}
            "
        """

    return run_command(command)
