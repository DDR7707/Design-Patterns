from email_notification_creator import EmailNotificationCreator
from sms_notification_creator import SMSNotificationCreator

class NotificationServiceDemo:
    @staticmethod
    def run():
        """Run the notification service demo."""
        # Create notification creators
        email_creator = EmailNotificationCreator()
        sms_creator = SMSNotificationCreator()

        # Create notifications
        email_notification = email_creator.create_notification()
        sms_notification = sms_creator.create_notification()

        # Send notifications
        email_notification.send("Hello via Email!")
        sms_notification.send("Hello via SMS!")


if __name__ == "__main__":
    # Example usage
    NotificationServiceDemo.run()
