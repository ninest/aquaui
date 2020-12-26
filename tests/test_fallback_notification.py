from aquaui import ApplescriptNotification as ASN


def test_fallback_notification():
    assert (
        ASN("Title").with_subtitle("Subtitle").applescript.strip()
        == 'display notification with title "Title" subtitle "Subtitle"'
    )
