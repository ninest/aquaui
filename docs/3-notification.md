# Notification

A native notification with a customizable title, subtitle, and informational text. In some cases, and icon and delay can also be set.\*

## Parameters

- `title`: The notification's title

Note that the notification's title does **not** change the notification's app name. The notification's app name defaults to "Python", and the only way to change it is by packaging your app with `py2app` and setting the icon.

## Functions

Similarly, these are also all chainable functions

### `.with_subtitle(subtitle: str)`

Set the subtitle of the notification (second line).

### `.with_informative_text(info_text: str)` \*

Set the informational text of the notification (third line).

### `.with_identity_image(image_path: str)` \*

Set the image on the right side of the notification. This does **not** change the "app image", which defaults to the Python Rocket. This Rocket image can only change if you package your app with `py2app` and set a custom icon.

### `.with_delay(delay: int)` \*

Set the delay in seconds between when `.send()` is called and the notification being shown.

### `.send()`

Send the notification.

\* Please see this [stackoverflow answer](https://stackoverflow.com/a/62248246/8677167). If your mac is unable to send notification from Python for an reason, aquaui will fallback to AppleScript notifications, where only the **title** and **subtitle** can be specified. The icon will be that of the AppleScript editor app.

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

In some cases, the native notification cannot be displayed, so the fallback notification will be sent instead. This fallback notification can only have the title, subtitle, and informational text. It **cannot** have an icon or delay.

- TBD
