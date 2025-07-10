from src.activity import Activity
from src.progressReport import ProgressReport

class ActivityManager:
    def __init__(self, activity_manager_id):
        self.activity_manager_id = activity_manager_id
        self.activities = []

    def track_activity(self, activity: Activity, source="manual"):
        self.activities.append(activity)
        print(f"Tracking activity: {activity.activity_type} from {source}")

    def calculate_calories_burned(self, activity: Activity):
        calories_burned = activity.duration * 10
        print(f"Calculating calories burned for {activity.activity_type}: {calories_burned}")
        return calories_burned

    def generate_progress_report(self, report_id, report_date):
        report = ProgressReport(report_id, report_date)
        data = [activity.calories_burned for activity in self.activities]
        report.generate_visual_representation(data)
        return report
