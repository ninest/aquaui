# Other important things

## Escaping quotes

Single quotes work fine.

```py
from aquaui import Alert

Alert("This is a 'quote'").show()
```

For double-quotes, however, you have to escape them by inserting not one, but **two** backslashes. You also have to use single-quotes for the string:

```py
Alert('This is a \\"quote\\"').show()
```

This may be changed and made simpler in the future.
