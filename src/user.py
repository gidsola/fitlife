
import datetime

from src.dataManager import DataManager
from src.userProfile import Profile
from src.goal import Goal
from src.emergencyContact import EmergencyContact

class User:
    """Represents a user in the FitLife application.
    Attributes:
        user_id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): Email address of the user.
        password (str): Password for the user's account.
    """
    def __init__(self, user_id: int, name: str, email: str, password: str, e_contacts: list[EmergencyContact],goals: list[Goal] = None, profile: Profile = None):
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if not isinstance(name, str) or not isinstance(email, str) or not isinstance(password, str):
            raise ValueError("Name, email, and password must be strings.")
        
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.emergency_contacts = e_contacts
        self.goals = goals
        self.profile = profile
        
    @staticmethod
    def to_dict(user: 'User') -> dict:
        """Converts User objects to dictionary representations."""
        try:
            if not isinstance(user, User):
                raise ValueError("Input must be a User object.")
            if user is None:
                raise ValueError("User cannot be None.")
        
            def serialize_goal(goal):
                if not goal:
                    return None
                d = vars(goal)
                if isinstance(d.get("start_date"), datetime.date):
                    d["start_date"] = d["start_date"].isoformat()
                if isinstance(d.get("end_date"), datetime.date):
                    d["end_date"] = d["end_date"].isoformat()
                return d
        
            def serialize_profile(profile):
                if not profile:
                    return None
                return {
                    "age": profile.age,
                    "height": profile.height,
                    "weight": profile.weight
                }

            return {
                "user_id": user.user_id,
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "goals": [serialize_goal(goal) for goal in user.goals],
                # "emergency_contact": user.emergency_contact,
                "profile": serialize_profile(user.profile)
            }
        except ValueError as e:
            print(f"\nError converting user to dict: {e}\n")
            return None
        
    @staticmethod
    def retrieveUserIfValid(user_id: int):
        """Checks if the user ID is valid, returning a user dictionary if found."""
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if user_id is None:
            raise ValueError("User ID cannot be None.")
        
        user =  DataManager.load_from_file(f"data/user_{user_id}.json")
        if user is None:
            return None
        return user
        
    
    @staticmethod
    def getUser(userid: int) -> 'User':
        """Returns a User object."""
        try:
            userDict = User.retrieveUserIfValid(userid)
            if userDict is None:
                raise ValueError(f"User with ID {userid} not found.")
            
            return User(
                userDict["user_id"],
                userDict["name"],
                userDict["email"],
                userDict["password"],
                # "emergency_contact": None,  # EmergencyContact(**user.get("emergency_contact", {})),
                [Goal(**goal) for goal in userDict["goals"]],
                Profile(**userDict["profile"])
            )
        except ValueError as e:
            print(f"\nError retrieving user: {e}\n")
            return None
        except TypeError as e:
            print(f"\nError retrieving user: {e}\n")
            return None
    
    
    @staticmethod
    def create_user(user_id, name, email, password) -> 'User':
        """Creates a new User object."""
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if not isinstance(name, str) or not isinstance(email, str) or not isinstance(password, str):
            raise ValueError("Name, email, and password must be strings.")
        if user_id is None or name is None or email is None or password is None:
            raise ValueError("User ID, name, email, and password cannot be None.")
        
        user = User(user_id, name, email, password)
        user.goals = None
        user.profile = Profile.create_profile()
        
        DataManager.save_to_file(user.to_dict(user))
        return user

    
    def update_user(self, name=None, email=None, password=None) -> None:
        """Updates the user's information."""
        if name:
            self.name = name
        if email:
            self.email = email
        if password:
            self.password = password
        print(f"User {self.user_id} updated: Name={self.name}, Email={self.email}")

    
    def save_user(self) -> None:
        """Saves the user's current information."""
        DataManager.save_to_file(self.to_dict(self), f"data/user_{self.user_id}.json")
        print(f"User {self.user_id} saved: Name={self.name}, Email={self.email}")
        
    
    def delete_user(self) -> None:
        """Deletes the user."""
        print(f"User {self.user_id} deleted: Name={self.name}, Email={self.email}")
        self = None
        # do more proper implement
    

    