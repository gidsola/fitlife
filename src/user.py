
import datetime

from src.dataManager import DataManager
from src.emergencyContact import EmergencyContact
from src.goal import Goal
from src.userProfile import Profile

from src.fitnessTracker import FitnessTracker
from src.activityManager import ActivityManager
from src.socialManager import SocialManager
from src.nutritionManager import NutritionManager
from src.notificationManager import NotificationManager
from src.reportManager import ReportManager

class User:
    """Represents a user in the FitLife application.
    Attributes:
        user_id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): Email address of the user.
        password (str): Password for the user's account.
    """
    def __init__(self, user_id: int, name: str, email: str, password: str, e_contacts: list[EmergencyContact] = None, goals: list[Goal] = None, profile: Profile = None):
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if not isinstance(name, str) or not isinstance(email, str) or not isinstance(password, str):
            raise ValueError("Name, email, and password must be strings.")
        
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        if user_id == 9999 and name == "sys_user" and password == "security":
            return
        
        self.activity_manager = ActivityManager(self)
        self.fitness_tracker = FitnessTracker(self)
        self.notification_manager = NotificationManager(self)
        self.nutrition_manager = NutritionManager(self)
        self.report_manager = ReportManager(self)
        self.social_manager = SocialManager(self)
        
        # isolate from non ITSecurityOfficer users?
        self.emergency_contacts = e_contacts if e_contacts is not None else []
        self.goals = goals if goals is not None else []
        self.profile = profile if profile is not None else {}
        
    
    def __to_dict__(self, user: 'User') -> dict:
        """Converts User objects to dictionary representations."""
        try:
            if not isinstance(user, User):
                raise ValueError("Input must be a User object.")
            if user is None:
                raise ValueError("User cannot be None.")
        
            def serialize_goal(goal: 'Goal'):
                if not goal:
                    return None
                d = vars(goal)
                if isinstance(d.get("start_date"), datetime.date):
                    d["start_date"] = d["start_date"].isoformat()
                if isinstance(d.get("end_date"), datetime.date):
                    d["end_date"] = d["end_date"].isoformat()
                return d
            
            def serialize_emergency_contact(contact: 'EmergencyContact'):
                if not contact:
                    return None
                return {
                    "name": contact.name,
                    "relationship": contact.relationship,
                    "phone_number": contact.phone_number
                }
        
            def serialize_profile(profile: 'Profile'):
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
                "emergency_contacts": [serialize_emergency_contact(contact) for contact in user.emergency_contacts],
                "profile": serialize_profile(user.profile)
            }
        except ValueError as e:
            print(f"\nError converting user to dict: {e}\n")
            return None
        
    def retrieveUserIfValid(self, user_id: int):
        """Checks if the user ID is valid, returning a user dictionary if found."""
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if user_id is None:
            raise ValueError("User ID cannot be None.")
        
        user =  DataManager.load_from_file(f"data/user_{user_id}.json")
        if user is None:
            return None
        return user
        
    
    def getUser(self, userid: int) -> 'User | None':
        """Returns a User object."""
        try:
            userDict = self.retrieveUserIfValid(userid)
            if userDict is None:
                raise ValueError(f"User with ID {userid} not found.")
            
            return User(
                userDict["user_id"],
                userDict["name"],
                userDict["email"],
                userDict["password"],
                [EmergencyContact(**contact) for contact in userDict["emergency_contacts"]],
                [Goal(**goal) for goal in userDict["goals"]],
                Profile(**userDict["profile"])
            )
        except ValueError as e:
            print(f"\nError retrieving user: {e}\n")
            return None
        except TypeError as e:
            print(f"\nError retrieving user: {e}\n")
            return None
    
    
    def create_user(self, user_id, name, email, password) -> 'User':
        """Creates a new User object."""
        if not self.email == "security@fitlife.com":
            raise ValueError("Only Security Officers may create new users.")
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if not isinstance(name, str) or not isinstance(email, str) or not isinstance(password, str):
            raise ValueError("Name, email, and password must be strings.")
        if user_id is None or name is None or email is None or password is None:
            raise ValueError("User ID, name, email, and password cannot be None.")
        
        user = User(user_id, name, email, password)
        user.profile = Profile.create_profile()
        user.saveUser()
        print(f"User {user.name} created successfully.")
        return user

    
    def updateUser(self, name=None, email=None, password=None) -> None:
        """Updates the user's information."""
        if name:
            self.name = name
        if email:
            self.email = email
        if password:
            self.password = password
        print(f"User {self.user_id} updated: Name={self.name}, Email={self.email}")

    
    def saveUser(self) -> None:
        """Saves the calling user's current information."""
        DataManager.save_to_file(self.__to_dict__(self), f"data/user_{self.user_id}.json")
        print(f"User {self.user_id} saved: Name={self.name}, Email={self.email}")
        
    
    def deleteUser(self) -> None:
        """Deletes the user."""
        print(f"User {self.user_id} deleted: Name={self.name}, Email={self.email}")
        self = None
        # do more proper implement
        
    
    