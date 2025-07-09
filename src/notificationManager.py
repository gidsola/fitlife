
from src.notification import Notification

class NotificationManager:
    def __init__(self, notification_manager_id):
        self.notification_manager_id = notification_manager_id

    def send_notification(self, notification):
        print(f"Sending notification: {notification.message}")

    def customize_notification_preferences(self):
        print("Customizing notification preferences")


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