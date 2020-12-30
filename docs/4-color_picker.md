# Color picker

WIP!

```py
from aquaui import ColorPicker

color = ColorPicker().show()
```

## Functions

### `.with_default_color(color: List[int])`

Note: the color is NOT in the RGB 255, 255, 255 format.

```py
from aquaui import ColorPicker

c = ColorPicker().with_default_color([0, 0, 0]).show()
print(c)
```

### `.show()`

Show the color picker. If the color picker is cancelled, `None` is returned. If a color is picked, the color as a list of integers is returned
