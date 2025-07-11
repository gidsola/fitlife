
from src.notification import Notification

class NotificationManager:
    def __init__(self, user):
        self.user = user
        self.notification_manager_id = 1
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

    
    def sendNotification(self, notification: Notification):   # notification_type, message, date
        """Create and send a notification for the user."""
        print(f"Notification sent: {notification.notification_type} - {notification.message} on {notification.date}")
        

    def getNotifications(self):
        """Retrieve all notifications for the user."""
        return self.notification_manager.notifications
    

    def sendAllNotifications(self):
        """Send all notifications."""
        for notification in self.notifications:
            self.send_notification(notification)

    def customize_notification_preferences(self):
        """Customize how notifications are sent or handled."""
        print("Customizing notification preferences.")


def showNotificationsMenu():
            notifications = []

            while True:
                print("\nNotification Preferences Menu")
                print("1. Send Notification")
                print("2. View Notifications")
                print("3. Customize Notification Preferences")
                print("4. Exit")
                sub = input("Select: ")

                if sub == "1":
                    notification_type = input("Notification type: ")
                    message = input("Message: ")
                    date = input("Date (YYYY-MM-DD): ")
                    notification = Notification(
                        notification_id=len(notifications) + 1,
                        notification_type=notification_type,
                        message=message,
                        date=date
                    )
                    notifications.append(notification)
                    print("Notification sent.")

                elif sub == "2":
                    if notifications:
                        for n in notifications:
                            print(f"{n.date}: {n.notification_type} - {n.message}")
                    else:
                        print("No notifications.")

                elif sub == "3":
                    nm = NotificationManager(notification_manager_id=1)
                    nm.customize_notification_preferences()

                elif sub == "4":
                    break

                else:
                    print("Invalid option.")

                input("Press Enter to continue...")