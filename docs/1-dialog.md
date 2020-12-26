# Dialog

```py
from aquaui import Dialog

the_dialog = Dialog("This is the dialog title")
the_dialog.show()
```

## Parameters

- `title`: the text shown in the dialog

## Functions

These are chainable functions to use on a `Dialog` object. See the [examples](#Examples) too.

### `.show()`

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

### `.with_buttons(buttons: Buttons)`

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

### `.with_input(default_answer: str or None)`

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
