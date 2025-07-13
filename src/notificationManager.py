
from src.notification import Notification

class NotificationManager:
    def __init__(self, user):
        self.user = user
        self.notifications = []

    def createNotification(self, title, message, date):
        """Add a notification to the manager's list of notifications."""
        
        notification = Notification(
            notification_id=len(self.notifications) + 1,
            notification_type=title,
            message=message,
            date=date
        )
        self.notifications.append(notification)

    
    def sendNotification(self, notification: Notification):
        """Create and send a notification for the user."""
        print(f"Notification sent: {notification.notification_type} - {notification.message} on {notification.date}")
        

    def getNotifications(self):
        """Retrieve all notifications for the user."""
        return self.notifications
    

    def sendAllNotifications(self):
        """Send all notifications."""
        for notification in self.notifications:
            self.send_notification(notification)

    def customize_notification_preferences(self):
        """Customize how notifications are sent or handled."""
        print("Customizing notification preferences.")
