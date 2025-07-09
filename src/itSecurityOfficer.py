
from src.user import User
# from src.dataManager import DataManager

class ITSecurityOfficer(User):
    def __init__(self, officer_id: int, name: str, contact_info: str):
        """Initializes an IT Security Officer with an officer ID, name, and contact information."""
        
        if officer_id is None or name is None or contact_info is None:
            raise ValueError("Officer ID, name, and contact information cannot be None.")
        if not isinstance(officer_id, int):
            raise ValueError("Officer ID must be an integer.")
        if not isinstance(name, str) or not isinstance(contact_info, str):
            raise ValueError("Name and contact information must be strings.")

        super().__init__(user_id=officer_id, name=name, email=contact_info, password="", profile=None, goals=None)

        self.officer_id = officer_id
        self.name = name
        self.contact_info = contact_info


    
    def enforce_security_policies(self, userid: int):
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

    def monitor_system_security(self):
        print("Monitoring system security")

    def manage_data_encryption(self, userid: int):
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

    def audit_security_compliance(self, userid: int):
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
        
        
def showSecurityOfficerMenu(security_officer: 'ITSecurityOfficer'):
        while True:
            print("IT Security Officer Menu:\n")
            print("Welcome, IT Security Officer!")
            print(f"Officer ID: {security_officer.officer_id}")
            print(f"Name: {security_officer.name}")
            print(f"Contact Info: {security_officer.contact_info}\n")
            print("Please select an option:")
            print("====================================")
            print("1. Enforce Security Policies")
            print("2. Monitor System Security")
            print("3. Manage Data Encryption")
            print("4. Audit Security Compliance")
            print("5. Logout")
            print("N. New User Creation")

            choice = input("Select an option: ")

            if choice == "1":
                user_id = input("Enter User ID to enforce security policies: ")
                if security_officer.enforce_security_policies(int(user_id)):
                    print(f"Security policies enforced successfully.")
                else:
                    print("\nError while trying to enforce security policies.")

            elif choice == "2":
                security_officer.monitor_system_security()

            elif choice == "3":
                user_id = input("Enter User ID to manage data encryption: ")
                security_officer.manage_data_encryption(int(user_id))

            elif choice == "4":
                user_id = input("Enter User ID to audit security compliance: ")
                security_officer.audit_security_compliance(int(user_id))

            elif choice == "N" or choice.lower() == "n":
                print("Creating a new user...")
                user_id = input("Enter User ID: ")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                password = input("Enter Password: ")

                try:
                    new_user = User.create_user(int(user_id), name, email, password)
                    print(f"New user created successfully: {new_user.name}")
                    # DataManager.save_to_file(new_user)  # Uncomment to save the new user
                except ValueError as e:
                    print(f"Error creating user: {e}")

            elif choice == "5":
                print("Logging out...")
                break
