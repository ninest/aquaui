from typing import Union
import os
import objc
import Foundation

# This import is required for NSImage
import AppKit  # noqa: 5401

from .fallback_notification import ApplescriptNotification

NSUserNotification = objc.lookUpClass("NSUserNotification")  # type: ignore
NSUserNotificationCenter = objc.lookUpClass("NSUserNotificationCenter")  # type: ignore
NSUrl = objc.lookUpClass("NSURL")  # type: ignore
NSImage = objc.lookUpClass("NSImage")  # type: ignore


class Notification:
    """Show a notification with a title, subtitle, info text, image, delay, and sound"""

    def __init__(self, title: Union[str, None] = None) -> None:
        """
        title is the large text at the top of the notification, not required
        """

        self.notification = NSUserNotification.alloc().init()

        if title is not None:
            self.notification.setTitle_(title)
            self.title = title

    def with_subtitle(self, subtitle: str):
        """
        subtitle is in the second line
        """

        self.notification.setSubtitle_(subtitle)
        self.subtitle = subtitle
        return self

    def with_informative_text(self, informative_text: str):
        """
        info text is the third (last) line
        """

        self.notification.setInformativeText_(informative_text)
        return self

    def _create_image(self, image_path: str):
        """Create an image for identity of content image"""

        path = f"file:{os.getcwd()}/{image_path}"
        url = NSUrl.alloc().initWithString_(path)
        image = NSImage.alloc().initWithContentsOfURL_(url)

        return image

    def with_identity_image(self, identity_image_path: Union[str, None] = None):
        """Image on the right side of the notification"""

        if identity_image_path is not None:
            image = self._create_image(identity_image_path)
            self.notification.set_identityImage_(image)

        return self

    def _with_content_image(self, content_image_path: Union[str, None] = None):
        """Image on the left side of the notification, but does not seem to be working on Big Sur"""

        if content_image_path is not None:
            image = self._create_image(content_image_path)
            self.notification.setContentImage_(image)

        return self

    def with_delay(self, delay: int = 0):
        """The delay in second between .send() and the notification being shown"""

        self.notification.setDeliveryDate_(
            Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date())  # type: ignore
        )
        return self

    def send(self) -> Union[None, str]:
        try:
            NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(self.notification)
        except:
            return ApplescriptNotification(self.title).with_subtitle(self.subtitle).send()
