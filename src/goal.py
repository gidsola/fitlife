
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
    
    
    
def goalMenu(user):
    while True:
        print("1. Set Goal")
        print("2. View Goal")
        print("X. Exit")
        sub = input("Select: ")

        if sub == "1":
            goal_type = input("Goal type (e.g., Steps): ")
            goal_value = int(input("Goal value (e.g., 10000): "))
            frequency = input("Frequency (e.g., Daily): ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")

            try:
                datetime.date.fromisoformat(start_date)
                datetime.date.fromisoformat(end_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                input("Press Enter to continue...")
                continue

            goal = Goal(
                goal_id=int(len(user.goals)) + 1,
                goal_name="User Goal", # ask user
                goal_type=goal_type,
                goal_value=goal_value,
                frequency=frequency,
                start_date=start_date,
                end_date=end_date
            )
            if goal.validate_goal():
                goal.set_goal(user, goal)
            else:
                print("Invalid goal.")

            input("Press Enter to continue...")

        elif sub == "2":
            if len(user.goals) > 0:
                for goal in user.goals:
                    print(goal)
            else:
                print("No goal set.")

            input("Press Enter to continue...")
                
        elif sub == "X" or sub.lower() == "x":
            print("Exiting goal menu.")
            break
                
   