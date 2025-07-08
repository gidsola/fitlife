

class NotificationManager:
    def __init__(self, notification_manager_id):
        self.notification_manager_id = notification_manager_id

    def send_notification(self, notification):
        print(f"Sending notification: {notification.message}")

    def customize_notification_preferences(self):
        print("Customizing notification preferences")
