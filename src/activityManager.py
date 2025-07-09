

class ActivityManager:
    def __init__(self, activity_manager_id):
        self.activity_manager_id = activity_manager_id
        self.activities = []

    # def track_activity(self, activity, source="manual"):
    #     self.activities.append(activity)
    #     print(f"Tracking activity: {activity.activity_type} from {source}")

    def calculate_calories_burned(self, activity):
        calories_burned = activity.duration * 10  # Example calculation
        print(f"Calculating calories burned for {activity.activity_type}: {calories_burned}")
        return calories_burned
