from aquaui import Alert, AlertType, Buttons


def test_alert():
    assert (
        Alert("Hello").with_buttons(Buttons(["One", "Two", "Three"])).of_type(AlertType.CRITICAL).applescript
        == 'display alert "Hello" buttons { "One", "Two", "Three" } as critical '
    )
