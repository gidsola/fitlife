
from src.user import User
from src.itSecurityOfficer import ITSecurityOfficer

class Login:
    def __init__(self, login_id: int, session_token: str, user: 'User' = None):
        if user is None and login_id != 9999:
            print("User must be provided for non-system login_id.")
            return
        
        self.login_id = login_id
        self.session_token = session_token
        self.user = user if user else None

    def authenticate(self, user_id: int, password: str) -> 'Login | None':
        if self.login_id != 9999:
            print("Authentication can only be performed with the system login_id (9999).")
            return None
        
        sysUser = User(user_id=9999, name="sys_user", email="", password="security")
        user = sysUser.getUser(int(user_id))
        if not user:
            print(f"User with ID {user_id} not found.")
            return None
        
        print(f"Authenticating user: {user.name}")
        if user and user.password == password:
            print("Authentication successful.")
            return Login(login_id=user.user_id, session_token="some_session_token", user=user)
        else:
            print("Authentication failed.")
            return None

    def manageSession(self, user: 'User'):
        print(f"Managing session for user: {user.name}")
        
def loginMenu() -> 'User | ITSecurityOfficer | None':
    print("Welcome to FitLife!")
    print("1. User Login")
    print("2. IT Security Officer Login")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        user_id = input("User ID: ")
        password = input("Password: ")
        
        sys_login = Login(login_id=9999, session_token="")
        new_login = sys_login.authenticate(user_id=int(user_id), password=password)
        
        if new_login is not None:
            user = new_login.user
            if user is None:
                print("User not found or authentication failed.")
                return None
            
            print(f"User {user.name} logged in successfully!")
            sys_login.manageSession(user)
            return user
        else:
            print("Login failed. Please check your credentials.")
            return None

    elif choice == "2":
        officer_id = input("Officer ID: ")
        name = input("Name: ")
        security_officer = ITSecurityOfficer(officer_id=int(officer_id), name=name, contact_info="security@fitlife.com")
        print("IT Security Officer login successful!")
        return security_officer

    elif choice == "3":
        print("Exiting FitLife. Goodbye!")
        return None