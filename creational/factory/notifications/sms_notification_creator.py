from notification_creator import NotificationCreator
from sms_notification import SMSNotification

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        """Create an SMSNotification instance."""
        return SMSNotification()
