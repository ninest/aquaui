<h1 align="center">
  <!-- <img src=assets/logo.svg width=95> -->
  <br>
  aquaui
</h1>

<p align="center">
Display native dialogs, alerts, notifications, color pickers, and more with Python
</p>

<p align="center">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/ninest/flixpy/PyTest?style=flat-square">
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

- [Documentation](#Documentation)
- [Examples](#Examples)
- Discussions

## Features

- [x] Display dialogs
  - [x] Dialog prompts
  - [ ] Icon support
- [ ] Alerts
- [ ] Choice dialogs
- [ ] Notifications
  - [ ] Customize title, subtitle, and informational text
  - [ ] Customize icon
  - [ ] Schedulable
  - [ ] Callbacks (button pressed, reply text) – [relevant](https://stackoverflow.com/a/62248246/8677167)

## Documentation

### Installation

```bash
pip install aquaui

# or
pip3 install aquaui
```

### Basic usage

Show a dialog with two buttons **Go** and **No**:

```py
from aquaui import Dialog, Buttons, Icon

buttons = Buttons(["Go", "No"], default_button="Go", cancel_button="No")
result = Dialog("Hello!").with_buttons(buttons).with_icon(Icon.CAUTION).show()

print(result)
```

### Dialog

```py
from aquaui import dialog
```

### Dialog prompt

```py
from aquaui import dialog_prompt
```

### Choice

### Notification

### Color picker

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

## License

MIT
