
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.user import User

from src.activity import Activity
# from src.progressReport import ProgressReport

class ActivityManager:
    def __init__(self, user: 'User'):
        self.user = user
        self.activities: list[Activity] = []
        
    def createActivity(self, activity_id: int, activity_type: str, duration: int, calories_burned: int, date: str):
        if not isinstance(activity_id, int) or not isinstance(activity_type, str) or not isinstance(duration, int) or not isinstance(calories_burned, int) or not isinstance(date, str):
            raise ValueError("Invalid input types for activity creation.")
        
        activity = Activity(activity_id, activity_type, duration, calories_burned, date)
        # self.activities.append(activity)
        print(f"Activity created: {activity.activity_type} on {activity.date}")
        return activity

    def trackActivity(self, activity: Activity, source="manual"):
        self.activities.append(activity)
        print(f"Tracking activity: {activity.activity_type} from {source}")
        
    def getActivity(self, activity_id):
        for activity in self.activities:
            if activity.activity_id == activity_id:
                return activity
        return None

    def calculate_calories_burned(self, activity: Activity):
        calories_burned = activity.duration * 10
        print(f"Calculating calories burned for {activity.activity_type}: {calories_burned}")
        return calories_burned

    
    
    def shareActivity(self, activity):        
        print(f"Sharing activity: {activity.activity_type} - {activity.calories_burned} calories burned")
        return True
