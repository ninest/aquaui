# Alert

Display an alert. Similar to a dialog, but larger, and no text field.

## Parameters

- `title`: The title of the alert

## Functions

### `.with_buttons(buttons: Buttons)`

```py
from aquaui import Alert, Buttons

al = Alert("Hello").with_buttons(Buttons(["One", "Two", "Three"], default_button="One")).show()
```

If not `default_button` is specified, the last button will become the default. See the [documentation for Dialogs](https://github.com/ninest/aquaui/blob/master/docs/1-dialog.md#with_buttonsbuttons-buttons) too, as Alerts are very similar.

### `of_type(AlertType)`

The possible alert types are `AlertType.INFORMATIONAL` and `AlertType.CRITICAL`. They change the icon shown on the alert. It is _not possible_ to display a custom icon here.

```py
# AlertType has to be imported before using:
from aquaui import Alert, Buttons, AlertType

al = Alert("Hello").with_buttons(Buttons(["One", "Two",])
al.of_type(AlertType.INFORMATIONAL)
al.show()
```

### `.show()`

Show the dialog, and return a `Result`. The result as a property of `button_returned`.

```py
# AlertType has to be imported before using:
from aquaui import Alert, Buttons, AlertType

al = Alert("Hello").with_buttons(Buttons(["One", "Two",]).show()

al.button_returned  # => either "One" or "Two"
```
