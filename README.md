<h1 align="center">
  <!-- <img src=assets/logo.svg width=95> -->
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

- [Documentation](#Documentation)
- [Examples](#Examples)
- Discussions

## Features

- [x] Display dialogs
  - [x] Dialog prompts
  - [x] Icon support
- [ ] Alerts
- [x] Choice dialogs
- [ ] Notifications
  - [x] Customize title, subtitle, and informational text
  - [x] Customize icon
  - [x] Schedulable
  - [ ] Callbacks (button pressed, reply text) – [relevant stackoverflow answer](https://stackoverflow.com/a/62248246/8677167)

## Documentation

<details>
  
  <summary>
    View Table of Contents
  </summary>
  
  
  - [Documentation](#documentation)
  - [Basic usage](#basic-usage)
  - [Dialog](#dialog)
    - [Parameters](#parameters)
    - [Functions](#functions)
      - [`.show()`](#show)
      - [`.with_buttons(buttons: Buttons)`](#with_buttonsbuttons-buttons)
      - [`.with_input(default_answer: str or None)`](#with_inputdefault_answer-str-or-none)
  - [Choice](#choice)
    - [Parameters](#parameters-1)
    - [Functions](#functions-1)
      - [`.with_choices(choices: List[str])`](#with_choiceschoices-liststr)
      - [`.default_choice(choice: str)`](#default_choicechoice-str)
      - [`.show()`](#show-1)
  - [Notification](#notification)
    - [Parameters](#parameters-2)
    - [Functions](#functions-2)
      - [`.with_subtitle(subtitle: str)`](#with_subtitlesubtitle-str)
      - [`.with_informative_text(info_text: str)`](#with_informative_textinfo_text-str)
      - [`.with_identity_image(image_path: str)` \*](#with_identity_imageimage_path-str-)
      - [`.with_delay(delay: int)` \*](#with_delaydelay-int-)
      - [`.send()`](#send)
    - [Fallback](#fallback)
  - [Color picker](#color-picker)
  - [Alert](#alert)
- [Examples](#examples)
  
  
</details>

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
from aquaui import Dialog

the_dialog = Dialog("This is the dialog title")
the_dialog.show()
```

#### Parameters

- `title`: the text shown in the dialog

#### Functions

These are chainable functions to use on a `Dialog` object. See the [examples](#Examples) too.

##### `.show()`

Display the dialog and return a result (see `.with_buttons` and `.with_input`).

```py
from aquaui import Dialog

the_dialog = Dialog("This is the dialog title")
the_dialog.show()
```

Note that the above code is the same as

```py
from aquaui import Dialog

the_dialog = Dialog("This is the dialog title").show()
```

##### `.with_buttons(buttons: Buttons)`

A list of buttons along with the default and cancel button can be specified.

```py
from aquaui import Dialog, Buttons

buttons = Buttons(["Enter", "Exit"])
```

The default button is highlighted:

```py
buttons = Buttons(["Enter", "Exit"], default_button="Enter")
```

Setting `default_button` and `cancel_button` is optional. Note that if a button is specified, its string needs to be in the list.

This code will **throw an error**:

```py
buttons = Buttons(["Enter", "Exit"], default_button="Go")
# => Exception: Default Button not in buttons list

buttons_2 = Buttons(["Enter", "Exit"], default_button="Enter", cancel_button="No")
# => Exception: Cancel Button not in buttons list
```

Once the buttons have been defined, pass them into the dialog with the `.with_buttons` chainable function:

```py
from aquaui import Dialog

buttons = Buttons(["Enter", "Exit"])
the_dialog = Dialog("This is the dialog title").with_buttons(buttons)
```

Finally, display the dialog with `.show()`:

```py
from aquaui import Dialog

buttons = Buttons(["Enter", "Exit"])
the_dialog = Dialog("This is the dialog title").with_buttons(buttons).show()
```

Note that the above code is the same as

```py
from aquaui import Dialog

buttons = Buttons(["Enter", "Exit"])
the_dialog = Dialog("This is the dialog title")
the_dialog.with_buttons(buttons)
the_dialog.show()
```

The `.show()` function will return a `Result` object which contains the `button_returned` (and `text_returned` if it's a dialog with an input – see `.with_input`)

```py
from aquaui import Dialog

buttons = Buttons(["Enter", "Exit"])
the_dialog = Dialog("This is the dialog title")
the_dialog.with_buttons(buttons)
result = the_dialog.show()

print(result.button_returned) # => a string of the button pressed
# Either "Enter" or "Exit"
```

##### `.with_input(default_answer: str or None)`

Specified that the dialog should have a text box:

```py
from aquaui import Dialog

buttons = Buttons(["Enter", "Exit"])
the_dialog = Dialog("This is the dialog title")
the_dialog.with_buttons(buttons)
the_dialog.with_input()

result = the_dialog.show()

result.button_returned  # => string of button pressed
result.text_returned  # => text entered in input
```

A default value can be provided:

```py
...

the_dialog.with_input("default text in textbox")

...
```

### Choice

```py
from aquaui import Choice

the_choice = Choice("Choose below").with_choices(["One", "Two", "Three"]).show()

print(the_choice)  # => Choice selected ("One", "Two", or "Three"), or false if none selected
```

Display a dialog with a list of choices to choose from.

#### Parameters

- `title`: The title of the choice selection dialog

#### Functions

These are chainable functions to use on a `Choice` object. See the [examples](#Examples) too.

##### `.with_choices(choices: List[str])`

A list of choices for the dialog.

```py
from aquaui import Choice

the_choice = Choice("Choose below")
the_choice.with_choices(["One", "Two", "Three"])
the_choice.show()
```

##### `.default_choice(choice: str)`

The default choice.

```py
from aquaui import Choice

the_choice = Choice("Choose below")
the_choice.with_choices(["One", "Two", "Three"])
the_choice.default_choice("One")
the_choice.show()
```

The default choice has to be in the list passed in to `.with_choices`, otherwise an error is thrown.

##### `.show()`

Shows the choice dialog and returns the text selected, or `""` (empty string) if nothing was selected.

```py
from aquaui import Choice

the_choice = Choice("Choose below").with_choices(["One", "Two", "Three"]).default_choice("One").show()

if the_choice:
  print(f"{the_choice} was selected")
else:
  print("Nothing was selected")
```

<details>
<summary>
How to check if a string is empty?
</summary>

```py
my_string = ""
if my_string:
  # string not empty
else:
  # string empty :(
```

</details>

### Notification

A native notification with a customizable title, subtitle, and informational text. In some cases, and icon and delay can also be set.\*

#### Parameters

- `title`: The notification's title

#### Functions

Similarly, these are also all chainable functions

##### `.with_subtitle(subtitle: str)`

Set the subtitle of the notification (second line).

##### `.with_informative_text(info_text: str)`

Set the informational text of the notification (third line).

##### `.with_identity_image(image_path: str)` \*

Set the image on the right side of the notification.

##### `.with_delay(delay: int)` \*

Set the delay in seconds between when `.send()` is called and the notification being shown.

##### `.send()`

Send the notification.

\* Please see this [stackoverflow answer](https://stackoverflow.com/a/62248246/8677167).

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

```py
from aquaui import Notification

notification = Notification("Your pizza is here!").with_delay(15).send()
# 15 seconds delay
```

#### Fallback

In some cases, the native notification cannot be displayed, so the fallback notification will be sent instead. This fallback notification can only have the title, subtitle, and informational text. It cannot have an icon or delay.

- TBD

### Color picker

- TBD

### Alert

- TBD

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

## License

MIT
