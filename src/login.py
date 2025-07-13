
from src.user import User

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
