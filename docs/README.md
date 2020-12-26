# Documentation

## Contents

1. [Dialog](https://github.com/ninest/aquaui/blob/master/docs/1-dialog.md)
2. [Choice](https://github.com/ninest/aquaui/blob/master/docs/2-choice.md)
3. [Notification](https://github.com/ninest/aquaui/blob/master/docs/3-notification.md)
4. [Color picker](https://github.com/ninest/aquaui/blob/master/docs/4-color_picker.md)
5. [Alert](https://github.com/ninest/aquaui/blob/master/docs/5-alert.md)
6. [Examples](https://github.com/ninest/aquaui#Examples)

## Installation

```bash
pip3 install aquaui
```

## Basic usage

Show a dialog with two buttons **Go** and **No**:

```py
from aquaui import Dialog, Buttons, Icon

buttons = Buttons(["Go", "No"], default_button="Go", cancel_button="No")
result = Dialog("Hello!").with_buttons(buttons).with_icon(Icon.CAUTION).show()

print(result)
```

## Examples

View examples on the [README](https://github.com/ninest/aquaui#Examples) or in the `examples/` directory.
