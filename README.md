<h1 align="center">
  <img src="https://raw.githubusercontent.com/ninest/aquaui/master/assets/icon.svg" width=155>
  <br>
  aquaui
</h1>

<p align="center">
Display native dialogs, alerts, notifications, color pickers, and more with Python
</p>

<p align="center">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/ninest/aquaui/Run%20tests?style=flat-square">

  <a href="https://pypi.org/project/aquaui/">
    <img src="https://img.shields.io/pypi/v/aquaui?color=blue&style=flat-square" alt="Version" />
  </a>
  <a href="https://pypi.org/project/aquaui/">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/aquaui?color=red&style=flat-square" />
  </a>

  <img src="https://img.shields.io/github/license/ninest/aquaui?style=flat-square" alt="MIT" />

  <a href="https://www.buymeacoffee.com/ninest">
    <img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-orange.svg?style=flat-square" alt="Buy Me A Coffee">
  </a>
</p>

**💥 This library is still a work in progress.**

## Useful links

- [Documentation](https://github.com/ninest/aquaui/tree/master/docs)
- [Examples](https://github.com/ninest/aquaui#examples)
- [Discussions](https://github.com/ninest/aquaui/discussions)

## Features

- [x] Display dialogs
  - [x] Dialog prompts
  - [x] Icon support
- [x] Alerts
- [x] Choice dialogs
- [ ] Notifications
  - [x] Customize title, subtitle, and informational text
  - [x] Customize icon
  - [x] Schedulable
  - [ ] Callbacks (button pressed, reply text) – [relevant stackoverflow answer](https://stackoverflow.com/a/62248246/8677167)
  - [ ] Fallback (AppleScript) notifications
- [ ] Color picker
- [ ] File/folder picker

## Documentation

[Documentation index and getting started](https://github.com/ninest/aquaui/tree/master/docs)

1. [Dialog](https://github.com/ninest/aquaui/blob/master/assets/1-dialog.md)
2. [Choice](https://github.com/ninest/aquaui/blob/master/assets/2-choice.md)
3. [Notification](https://github.com/ninest/aquaui/blob/master/assets/3-notification.md)
4. [Color picker](https://github.com/ninest/aquaui/blob/master/assets/4-color_picker.md)
5. [Alert](https://github.com/ninest/aquaui/blob/master/assets/5-alert.md)
6. [Examples](https://github.com/ninest/aquaui#examples)

## Examples

See the `examples/` directory. Feel free to make a pull request to add more examples.

**Show a dialog with the buttons "Go" (default) and "No" (to cancel) with the caution icon:**

```py
from aquaui import Dialog, Buttons, Icon

buttons = Buttons(["Go", "No"], default_button="Go", cancel_button="No")
result = Dialog("Hello!").with_buttons(buttons).with_icon(Icon.CAUTION).show()
```

**Execute functions based on the button clicked:**

```py
from aquaui import Dialog, Buttons

button_one = "One"
button_two = "Two"
buttons = Buttons([button_one, button_two])

result = Dialog("Press a button").with_buttons(buttons).show()

if result.button_returned == button_one:
  print("Button One was pressed")
elif result.button_returned == button_two:
  print("Button Two was pressed")
```

**Display a choice dialog with the options "Netflix" and "Prime Video"**

```py
from aquaui import Choice

provider = Choice("Choose the streaming platform").with_choices(["Netflix", "Prime Video"]).show()
print(provider)
```

If this example interests you, check out my other library [Flixpy](https://github.com/ninest/flixpy).

**Display a notification:**

```py
from aquaui import Notification

notification = (
    Notification("Hello!")
    .with_subtitle("This is the subtitle!")
    .with_informative_text("Isn't this informative?")
    .with_identity_image("assets/folder.png")  # the image on the right of the notification
    .send()
)
```

**Schedule a notification:**

```py
from aquaui import Notification

notification = Notification("Your pizza is here!").with_delay(15).send()
# 15 seconds delay
```

## Build setup

Clone or fork the repository, then run

```bash
poetry shell

poetry install
pre-commit install
```

Make changes, then run tests with

```bash
pytest tests
```

Ensure that all tests pass.

<details>
<summary>
Recommended editor settings
</summary>

```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.insertSpaces": true,
    "editor.detectIndentation": false,
    "editor.tabSize": 4
  },
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.pylintEnabled": false,
  "python.pythonPath": "/Users/yourusername/.../aquaui-UIHDsdfS-py3.7"
}
```

</details>

## License

MIT
