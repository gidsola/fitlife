
from src.user import User

class ITSecurityOfficer(User):
    def __init__(self, officer_id: int, name: str, contact_info: str):
        """Initializes an IT Security Officer User object with an officer ID, name, and contact information."""
        
        if officer_id is None or name is None or contact_info is None:
            raise ValueError("Officer ID, name, and contact information cannot be None.")
        if not isinstance(officer_id, int):
            raise ValueError("Officer ID must be an integer.")
        if not isinstance(name, str) or not isinstance(contact_info, str):
            raise ValueError("Name and contact information must be strings.")

        super().__init__(user_id=officer_id, name=name, email=contact_info, password="")

        self.officer_id = officer_id
        self.name = name
        self.contact_info = contact_info


    
    def enforceSecurityPolicies(self, userid: int):
        try:
            if not isinstance(userid, int):
                raise ValueError("User ID must be an integer.")
            if userid is None:
                raise ValueError("User ID cannot be None.")

            user = User.getUser(userid)
            if user is None:
                raise ValueError(f"User with ID {userid} not found.")

            print(f"\nEnforcing security policies for user: {user.name}")
            return True

        except ValueError as e:
            print(f"\nError enforcing security policies: {e}\n")
            return False

    def monitorSystemSecurity(self):
        print("Monitoring system security")

    def manageDataEncryption(self, userid: int):
        try:
            if not isinstance(userid, int):
                raise ValueError("User ID must be an integer.")
            if userid is None:
                raise ValueError("User ID cannot be None.")

            user = User.getUser(userid)
            if user is None:
                raise ValueError(f"User with ID {userid} not found.")

            print(f"Managing data encryption for user: {user.name}")
            return True

        except ValueError as e:
            print(f"\nError managing data encryption: {e}\n")
            return False

    def auditSecurityCompliance(self, userid: int):
        try:
            if not isinstance(userid, int):
                raise ValueError("User ID must be an integer.")
            if userid is None:
                raise ValueError("User ID cannot be None.")

            user = User.getUser(userid)
            if user is None:
                raise ValueError(f"User with ID {userid} not found.")

            print(f"Auditing security compliance for user: {user.name}")
            return True

        except ValueError as e:
            print(f"\nError auditing security compliance: {e}\n")
            return False
