from aquaui import Dialog, Buttons, Icon

"""
Test out by checking the output applescript
"""


def test_title():
    assert Dialog("This is a dialog").applescript.strip() == 'display dialog "This is a dialog"'


def test_buttons():
    buttons = Buttons(["Go", "Nah"], default_button="Go", cancel_button="Nah")
    assert (
        Dialog("Title").with_buttons(buttons).applescript.strip()
        == 'display dialog "Title" buttons { "Go", "Nah" } default button "Go" cancel button "Nah"'
    )


def test_icon():
    assert Dialog("Title").with_icon(Icon.NOTE).applescript.strip() == 'display dialog "Title" with icon note'


def test_input():
    assert Dialog("Title").with_input().applescript.strip() == 'display dialog "Title" default answer ""'
    assert (
        Dialog("Title").with_input("Default Answer").applescript.strip()
        == 'display dialog "Title" default answer "Default Answer"'
    )
