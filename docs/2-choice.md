# Choice

```py
from aquaui import Choice

the_choice = Choice("Choose below").with_choices(["One", "Two", "Three"]).show()

print(the_choice)  # => Choice selected ("One", "Two", or "Three"), or false if none selected
```

Display a dialog with a list of choices to choose from.

## Parameters

- `title`: The title of the choice selection dialog

## Functions

These are chainable functions to use on a `Choice` object. See the [examples](https://github.com/ninest/aquaui#examples) too.

### `.with_choices(choices: List[str])`

A list of choices for the dialog.

```py
from aquaui import Choice

the_choice = Choice("Choose below")
the_choice.with_choices(["One", "Two", "Three"])
the_choice.show()
```

### `.default_choice(choice: str)`

The default choice.

```py
from aquaui import Choice

the_choice = Choice("Choose below")
the_choice.with_choices(["One", "Two", "Three"])
the_choice.default_choice("One")
the_choice.show()
```

The default choice has to be in the list passed in to `.with_choices`, otherwise an error is thrown.

### `.show()`

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
