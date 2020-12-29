# Documentation

## Contents

1. [Dialog](./1-dialog.md)
2. [Choice](./2-choice.md)
3. [Notification](./3-notification.md)
4. [Color picker](./4-color_picker.md)
5. [Alert](./5-alert.md)
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

## FAQ

1. Why can't I specify a callback for notifications?

   Read this [answer on stackoverflow](https://stackoverflow.com/a/62248246/8677167).

2. Why chained functions and classes and not a single function?

   I had initially used regular function, and the code looked [like this](https://github.com/ninest/aquaui/blob/f4b35f05b0b5689f22e35bfe1d0af30599db7adc/as.py#L5):

   ```py
   def dialog_prompt(text, default_answer="", buttons=["Cancel", "Continue"], default_button=None, cancel_button=None, icon=None, password=False):
     ...
   ```

   As you can see, this is a little confusing. But more than that, it was difficult to test. If I wanted to get the output AppleScript, I'd have to add a flag to the function like

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

3. What does the name mean?

   This library was made for macos dialogs, and [Aqua](<https://en.m.wikipedia.org/wiki/Aqua_(user_interface)>) is the GUI.
