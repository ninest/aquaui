import pytest
from aquaui.types.buttons import Buttons


@pytest.fixture
def buttons():
    enter_button = "Enter"
    cancel_button = "Cancel"
    more_button = "More"

    return Buttons(
        [cancel_button, more_button, enter_button],
        default_button=enter_button,
        cancel_button=cancel_button,
    )


def test_buttons_string(buttons: Buttons):
    assert buttons.string == '"Cancel", "More", "Enter"'


def test_buttons_error():
    """
    Should through an error as the default/cancel button are not in the
    buttons list
    """

    with pytest.raises(Exception):
        Buttons(["One"], default_button="OOOOO")

    with pytest.raises(Exception):
        Buttons(["One"], cancel_button="OOOOO")
