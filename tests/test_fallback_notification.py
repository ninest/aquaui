from aquaui import ApplescriptNotification as ASN


def test_fallback_notification():
    assert (
        ASN("Text").with_title("Title").with_subtitle("Subtitle").applescript.strip()
        == 'display notification "Text" with title "Title" subtitle "Subtitle"'
    )
