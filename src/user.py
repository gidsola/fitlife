


from src.dataManager import DataManager
# from src.itSecurityOfficer import ITSecurityOfficer
from src.userProfile import Profile
# from src.goal import Goal
# from src.emergencyContact import EmergencyContact


class User:
    """Represents a user in the FitLife application.
    Attributes:
        user_id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): Email address of the user.
        password (str): Password for the user's account.
    """
    def __init__(self, user_id: int, name: str, email: str, password: str, profile: Profile = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        
        # self.goal = None
        # self.emergency_contact = None
        self.profile = profile

    # def set_goal(self, goal):
    #     self.goal = goal
    #     print(f"Goal set for user {self.name}: {goal.goal_type} - {goal.goal_value}")

    # def view_progress_report(self, report):
    #     print(f"Progress Report for {self.name} on {report.report_date}: Report ID {report.report_id}")

    # def set_emergency_contact(self, contact):
    #     self.emergency_contact = contact
    #     print(f"Emergency contact set for user {self.name}: {contact.name} ({contact.relationship})")

    # def set_profile(self, profile):
    #     self.profile = profile
    #     print(f"Profile updated for user {self.name}.")
        
    @staticmethod
    def getUser(userid: int) -> 'User':
        """Returns a User object."""
        try:
            user = User.validateUserId(userid)
            if user is None:
                raise ValueError(f"User with ID {userid} not found.")
            return User(**user)
        
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
        profile = Profile.create_profile()
        user.profile = profile
        
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
        
    
    def delete_user(self) -> None:
        print(f"User {self.user_id} deleted: Name={self.name}, Email={self.email}")
        self.user_id = None
        self.name = None
        self.email = None
        self.password = None
        # self.goal = None
        # self.emergency_contact = None
        self.profile = None
    

    @staticmethod
    def to_dict(user: 'User') -> dict:
        # def serialize_goal(goal):
        #     if not goal:
        #         return None
        #     d: dict[str, any] = vars(goal)
            
        #     if isinstance(d.get("start_date"), datetime.date):
        #         d["start_date"] = d["start_date"].isoformat()
            
        #     if isinstance(d.get("end_date"), datetime.date):
        #         d["end_date"] = d["end_date"].isoformat()
        #     return d

        def serialize(obj):
            return vars(obj) if obj else None

        return {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "password": user.password,
            # reconsider these
            # "goal": serialize_goal(user.goal),
            # "emergency_contact": serialize(user.emergency_contact),
            "profile": serialize(user.profile)
        }
        
    @staticmethod
    def validateUserId(user_id: int):
        """Checks if the user ID is valid, returning a user dictionary if found."""
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if user_id is None:
            raise ValueError("User ID cannot be None.")
        
        user =  DataManager.load_from_file(f"data/user_{user_id}.json")
        if user is None:
            return None
        return user
    

    def __str__(self) -> str:
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"
    
    def __repr__(self) -> str:
        return f"User({self.user_id}, {self.name}, {self.email})"
    
    def __eq__(self, other):
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False
    
    def __hash__(self) -> int:
        return hash(self.user_id)
    

    
    
    
    
    

    