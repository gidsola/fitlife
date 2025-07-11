
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.user import User
    from src.activityManager import ActivityManager

class FitnessTracker:
    def __init__(self, user: 'User'):
        self.activity_manager = user.activity_manager

    def track_activity(self, activity_type, duration, calories_burned, date, source="manual"):
        activity = self.activity_manager.createActivity(
            activity_id=len(self.activity_manager.activities) + 1,
            activity_type=activity_type,
            duration=duration,
            calories_burned=calories_burned,
            date=date
        )
        self.activity_manager.track_activity(activity, source)
        print(f"Tracked {activity_type} activity: {duration} minutes, {calories_burned} calories burned")

    def get_activity_logs(self):
        return self.activity_manager.activities

    def sync_with_device(self, device_data):
        for activity_data in device_data:
            try:
                activity = self.activity_manager.createActivity(
                    activity_id=activity_data['activity_id'],
                    activity_type=activity_data['activity_type'],
                    duration=activity_data['duration'],
                    calories_burned=activity_data['calories_burned'],
                    date=activity_data['date']
                )
                self.activity_manager.track_activity(activity, source="device")
            except KeyError as e:
                print(f"Missing data in device sync: {e}")
        print("Synced with device successfully")

    
def showTrackingMenu(activity_manager: 'ActivityManager'):
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

                activity = activity_manager.createActivity(
                    activity_id=len(activity_manager.activities)+1, 
                    activity_type=activity_type, 
                    duration=duration, 
                    calories_burned=calories_burned, 
                    date=date
                )
                # activities.append(activity)
                activity_manager.track_activity(activity)
                print("Activity tracked.")

            elif sub == "2":
                if activity_manager.activities:
                    for a in activity_manager.activities:
                        print(f"{a.date}: {a.activity_type}, {a.duration} min, {a.calories_burned} cal")
                else:
                    print("No activities tracked.")

            input("Press Enter to continue...")