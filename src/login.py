
from src.user import User
from src.itSecurityOfficer import ITSecurityOfficer

class Login:
    def __init__(self, login_id, session_token):
        self.login_id = login_id
        self.session_token = session_token

    def authenticate(self, user: User):
        print(f"Authenticating user: {user.name}")
        return True

    def manageSession(self, user: User):
        print(f"Managing session for user: {user.name}")
        
    def loginMenu() -> User | ITSecurityOfficer | None:
        print("Welcome to FitLife!")
        print("1. User Login")
        print("2. IT Security Officer Login")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            user_id = input("User ID: ")
            password = input("Password: ")

            user = User.getUser(int(user_id))
            if not user:
                print(f"User with ID {user_id} not found.")
                return None
            
            print(f"Attempting to login with user ID: {user_id}")

            if user and str(user.user_id) == user_id:
                login = Login(login_id=1, session_token="abc123xyz")
                
                if login.authenticate(user):
                    print("Login successful!")
                    return user
            else:
                print("Invalid user ID or password. Please try again.")
                return None

        elif choice == "2":
            officer_id = input("Officer ID: ")
            name = input("Name: ")
            security_officer = ITSecurityOfficer(officer_id=int(officer_id), name=name, contact_info="security@example.com")
            print("IT Security Officer login successful!")
            print(f"security_officer type: {type(security_officer)}")
            return security_officer

        elif choice == "3":
            print("Exiting FitLife. Goodbye!")
            return None