


class FitnessTracker:
    def __init__(self, tracker_id, brand, model):
        self.tracker_id = tracker_id
        self.brand = brand
        self.model = model

    def track_activity(self, activity_type, duration, calories_burned, date, source="manual"):
        if source == "automatic":
            print(f"Automatically tracking activity: {activity_type}")
        else:
            print(f"Manually tracking activity: {activity_type}")

        activity = {
            "activity_type": activity_type,
            "duration": duration,
            "calories_burned": calories_burned,
            "date": date
        }
        return activity