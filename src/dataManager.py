import json
import os
# import datetime

# from src.user import User
# from src.goal import Goal
# from src.emergencyContact import EmergencyContact
# from src.userProfile import Profile

class DataManager:
    """A class to manage data storage and retrieval for the FitLife application."""
    
    @staticmethod
    def save_to_file(user: dict, filename=None) -> None:
        if not filename:
            filename = f"data/user_{user["user_id"]}.json"
        if not isinstance(user, dict):
            raise ValueError("User data must be a dictionary.")
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            json.dump(user, f, indent=4)

    @staticmethod
    def load_from_file(filename: os.path) -> dict | None:
        if not os.path.exists(filename):
            return None
        
        with open(filename, "r") as f:
            data: dict = json.load(f)
            # user = User(data["user_id"], data["name"], data["email"], data["password"])
            
            # if data.get("goal"):
            #     g = data["goal"]
            #     user.goal = Goal(g["goal_id"], g["goal_type"], g["goal_value"], g["frequency"], g["start_date"], g["end_date"])
            
            # if data.get("emergency_contact"):
            #     c = data["emergency_contact"]
            #     user.emergency_contact = EmergencyContact(c["contact_id"], c["name"], c["phone_number"], c["relationship"])
            
            # if data.get("profile"):
            #     p = data["profile"]
            #     user.profile = Profile(p["profile_id"], p["age"], p["height"], p["weight"])
            
            return data
