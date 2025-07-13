
from src.menus import loginMenu, showSecurityOfficerMenu, showUserDashboard

def start_app():
    while True:
        user = loginMenu()
        if user is None:
            print("Login failed. Please try again.")
            continue
        if type(user).__name__ == "ITSecurityOfficer":
            showSecurityOfficerMenu(user)
            break
        elif type(user).__name__ == "User":
            showUserDashboard(user)
            break
        else:
            print("Unknown user type. Please try again.")
            continue

if __name__ == "__main__":
    start_app()
