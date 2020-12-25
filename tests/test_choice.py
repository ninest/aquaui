import pytest
from aquaui import Choice


def test_choice():
    assert (
        Choice("Choice Title").with_choices(["One", "Two"]).applescript.strip()
        == 'choose from list {"One", "Two"} with prompt "Choice Title"'
    )


def test_choice_default():
    assert (
        Choice("Title").with_choices(["A", "B"]).default_choice("B").applescript.strip()
        == 'choose from list {"A", "B"} with prompt "Title" default items { "B" }'
    )


def test_choice_error():
    with pytest.raises(Exception):
        # Error because default choice not in choices
        Choice("Title").with_choices(["A", "B"]).default_choice("C")
