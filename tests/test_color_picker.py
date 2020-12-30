from aquaui import ColorPicker


def test_color_picker():
    assert ColorPicker().applescript.strip() == "choose color"


def test_color_picker_default_color():
    assert ColorPicker().with_default_color([1, 2, 3]).applescript.strip() == "choose color default color { 1, 2, 3 }"
