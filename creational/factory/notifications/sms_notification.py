from notification import Notification

class SMSNotification(Notification):
    def send(self, message):
        """Send an SMS notification with the given message."""
        print(f"Sending SMS Notification: {message}")
