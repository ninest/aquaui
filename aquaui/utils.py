import subprocess


def quotify(string):
    """Return the string with quotes

    >>> quotify("some string")
    '"some string"'
    """

    return f'"{string}"'


def run_command(command: str):
    result = subprocess.check_output(command, shell=True)
    return result.decode("utf-8")


def run_applescript(script: str):
    command = f"""
        osascript -e '\
            set answer to {script}
            return answer
        '
    """
    return run_command(command)
