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

- [Useful links](#useful-links)
- [Features](#features)
- [Documentation](#documentation)
- [Examples](#examples)
- [FAQ](#faq)
- [License](#license)

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

[Documentation index and getting started](https://github.com/ninest/aquaui/tree/master/docs)

1. [Dialog](https://github.com/ninest/aquaui/blob/master/assets/1-dialog.md)
2. [Choice](https://github.com/ninest/aquaui/blob/master/assets/2-choice.md)
3. [Notification](https://github.com/ninest/aquaui/blob/master/assets/3-notification.md)
3. [Color picker](https://github.com/ninest/aquaui/blob/master/assets/4-color_picker.md)
4. [Alert](https://github.com/ninest/aquaui/blob/master/assets/5-alert.md)
5. [Examples](#Examples)

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

## FAQ

<details>
<summary>
View FAQ
</summary>

1. Why chained functions and classes and not a single function?

   I had initially used regular function, and the code looked [like this](https://github.com/ninest/aquaui/blob/f4b35f05b0b5689f22e35bfe1d0af30599db7adc/as.py#L5):

   ```py
   def dialog_prompt(text, default_answer="", buttons=["Cancel", "Continue"], default_button=None, cancel_button=None, icon=None, password=False):
     ...
   ```

   As you can see, this is a little confusing. But more than that, it was difficult to text. If I wanted to get the output AppleScript, I'd have to add a flag to the function like

   ```py
   def dialog_prompt(......, return_applescript=False):
     ...
     if return_applescript:
       return as
    ...
   ```

   This, to an extent is also fine, but there's an issue with _type safety_. I wanted to add types to all functions to make it easier to code faster. So for the above function, adding types will look something like this:

   ```py
   def dialog_prompt(..., return_applescript=False) -> Union[Result, None]:
     ...

    response = dialog_prompt(...)
    answer = response.text_returned.strip()
   ```

   This looks fine, right? Althought it runs fine, your code editor will fight with you. You know that the function returns a `Result` object, but your editor does not. It thinkgs it is possibly `None`, so you have to do something like this **all the time**:

   ```py
   ...

   response = dialog_prompt(...)
   answer = response.text_returned.strip()

   if response is not None:
     answer = response.text_returned.strip()
   ```

   With chained functions, it's easy to do something like

   ```py
   response = Dialog(..).with_input().show()

   # for testing purposes
   output_applescript = Dialog(..).with_input().applescript
   ```

2. What does the name mean?

   This library was made for macos dialogs, and [Aqua](<https://en.m.wikipedia.org/wiki/Aqua_(user_interface)>) is the GUI.

</details>

## License

MIT
