from notification_creator import NotificationCreator
from email_notification import EmailNotification

class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        """Create an EmailNotification instance."""
        return EmailNotification()
