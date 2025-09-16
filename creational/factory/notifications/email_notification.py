from notification import Notification

class EmailNotification(Notification):
    def send(self, message):
        """Send an email notification with the given message."""
        print(f"Sending Email Notification: {message}")
