
import datetime

class Goal:
    def __init__(self, goal_id, goal_name, goal_type, goal_value, frequency, start_date, end_date):
        self.goal_id = goal_id
        self.goal_name = goal_name
        self.goal_type = goal_type
        self.goal_value = goal_value
        self.frequency = frequency
        self.start_date = datetime.date.fromisoformat(start_date) if isinstance(start_date, str) else start_date
        self.end_date = datetime.date.fromisoformat(end_date) if isinstance(end_date, str) else end_date
     
    def __str__(self):
        start_date_str = self.start_date.isoformat() if hasattr(self.start_date, "isoformat") else str(self.start_date)
        end_date_str = self.end_date.isoformat() if hasattr(self.end_date, "isoformat") else str(self.end_date)
        return (
            f"\n"
            f"{'='*40}\n"
            f"        Goal Details\n"
            f"{'='*40}\n"
            f"ID         : {self.goal_id}\n"
            f"Name       : {self.goal_name}\n"
            f"Type       : {self.goal_type}\n"
            f"Value      : {self.goal_value}\n"
            f"Frequency  : {self.frequency}\n"
            f"Start Date : {start_date_str}\n"
            f"End Date   : {end_date_str}\n"
            f"{'='*40}\n"
        )
           

    def validate_goal(self):
        if not self.goal_type or not self.goal_value:
            print("Goal type and value must be set.")
            return False
        if self.start_date > self.end_date:
            print("Start date must be before end date.")
            return False
        return True
    
    
    def set_goal(self, user, goal):
        goal = Goal(goal_id=goal.goal_id, goal_name = goal.goal_name, goal_type=goal.goal_type, goal_value=goal.goal_value, frequency=goal.frequency, start_date=goal.start_date, end_date=goal.end_date)
        user.goals.append(goal)
        user.save_user()
        print(f"Goal set for user {user.name}: {goal.goal_type} - {goal.goal_value}")
