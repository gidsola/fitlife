
import datetime

class Goal:
    def __init__(self, goal_id, goal_type, goal_value, frequency, start_date, end_date):
        self.goal_id = goal_id
        self.goal_type = goal_type
        self.goal_value = goal_value
        self.frequency = frequency
        self.start_date = datetime.date.fromisoformat(start_date) if isinstance(start_date, str) else start_date
        self.end_date = datetime.date.fromisoformat(end_date) if isinstance(end_date, str) else end_date

    def validate_goal(self):
        if not self.goal_type or not self.goal_value:
            print("Goal type and value must be set.")
            return False
        if self.start_date > self.end_date:
            print("Start date must be before end date.")
            return False
        return True