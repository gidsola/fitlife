
import datetime
from src.activity import Activity
from src.activityManager import ActivityManager

class FitnessTracker:
    def __init__(self, tracker_id):
        self.tracker_id = tracker_id

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
    
def showTrackingMenu(activity_manager):
    activities = []
    while True:
            print("\nActivity Tracking Menu")    
            print("\n1. Track Activity\n2. View Activities")
            sub = input("Select: ")

            if sub == "1":
                activity_type = input("Activity type (e.g., Running): ")
                try:
                    duration = int(input("Duration (minutes): "))
                    calories_burned = int(input("Calories burned: "))
                    date = input("Date (YYYY-MM-DD): ")
                    datetime.date.fromisoformat(date)
                except ValueError:
                    print("Invalid input or date format. Please use correct types and YYYY-MM-DD for date.")
                    input("Press Enter to continue...")
                    continue

                activity = Activity(activity_id=len(activities)+1, activity_type=activity_type, duration=duration, calories_burned=calories_burned, date=date)
                activities.append(activity)
                activity_manager.track_activity(activity)
                print("Activity tracked.")

            elif sub == "2":
                if activities:
                    for a in activities:
                        print(f"{a.date}: {a.activity_type}, {a.duration} min, {a.calories_burned} cal")
                else:
                    print("No activities tracked.")

            input("Press Enter to continue...")