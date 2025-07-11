
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
        
        self.emergency_contacts = e_contacts
        self.goals = goals
        self.profile = profile
        
        self.activity_manager = ActivityManager(self)
        self.social_manager = SocialManager(self)
        self.nutrition_manager = NutritionManager(self)
        self.notification_manager = NotificationManager(self)
        self.fitness_tracker = FitnessTracker(self.activity_manager)
    
    def __to_dict(user: 'User') -> dict:
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
            
            def serialize_emergency_contact(contact):
                if not contact:
                    return None
                return {
                    "name": contact.name,
                    "relationship": contact.relationship,
                    "phone_number": contact.phone_number
                }
        
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
                "emergency_contact": [serialize_emergency_contact(contact) for contact in user.emergency_contacts],
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
                [EmergencyContact(**contact) for contact in userDict.get("emergency_contacts", [])],
                [Goal(**goal) for goal in userDict["goals"]],
                Profile(**userDict["profile"])
            )
        except ValueError as e:
            print(f"\nError retrieving user: {e}\n")
            return None
        except TypeError as e:
            print(f"\nError retrieving user: {e}\n")
            return None
    
    
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
        
        DataManager.save_to_file(user.__to_dict(user)) # change to a saveuser implement
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
        """Saves the user's current information."""
        DataManager.save_to_file(self.__to_dict(self), f"data/user_{self.user_id}.json")
        print(f"User {self.user_id} saved: Name={self.name}, Email={self.email}")
        
    
    def deleteUser(self) -> None:
        """Deletes the user."""
        print(f"User {self.user_id} deleted: Name={self.name}, Email={self.email}")
        self = None
        # do more proper implement
        
        
    def share_activity(self, activity):
        self.social_manager.shareActivity(activity)


    def share_progress_report(self, report):
        self.social_manager.share_progress_report(report)
        

    def log_nutrition(self, nutrition):
        self.nutrition_manager.log_nutrition(nutrition)


    def share_nutrition_logs(self):
        nutrition_logs = self.nutrition_manager.getNutritionItems()
        for log in nutrition_logs:
            self.social_manager.getNutritionInfo(log)

    def createNotification(self, title, message, date):
        """Sends a notification to the user."""
        self.notification_manager.createNotification(title, message, date)
        print(f"Notification sent: {title} - {message} on {date}")
    