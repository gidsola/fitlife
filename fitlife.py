

from src.login import loginMenu
from src.itSecurityOfficer import showSecurityOfficerMenu

from src.emergencyContact import showEmergencyContactMenu
from src.goal import showGoalsMenu
from src.nutrition import showNutritionMenu
from src.notificationManager import showNotificationsMenu
from src.userProfile import showProfileMenu
from src.progressReport import showProgressReportMenu
from src.socialManager import showSocialMenu
from src.deviceManager import showSyncMenu
from src.fitnessTracker import showTrackingMenu


def showUserDashboard(user):
    while True:
        print("Welcome to FitLife!")
        print("\nDashboard:")
        print("1. Set/View Goals")
        print("2. Track Activity")
        print("3. Log Nutrition")
        print("4. Social Features")
        print("5. Device Sync")
        print("6. Notifications")
        print("7. View Progress Report")
        print("8. Emergency Contact")
        print("9. Profile Management")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "0":
            print("Exiting FitLife. Goodbye!")
            break
        
        menus = {
            "1": showGoalsMenu,
            "2": showTrackingMenu,
            "3": showNutritionMenu,
            "4": showSocialMenu,
            "5": showSyncMenu,
            "6": showNotificationsMenu,
            "7": showProgressReportMenu,
            "8": showEmergencyContactMenu,
            "9": showProfileMenu
        }

        if choice in menus:
            try:
                menus[choice](user)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid option. Please try again.")


def start_app():
    while True:
        user = loginMenu()
        if type(user).__name__ == "ITSecurityOfficer":
            showSecurityOfficerMenu(user)
            break
        elif type(user).__name__ == "User":
            showUserDashboard(user)
            break
        else:
            print("Invalid login. Please try again.")

if __name__ == "__main__":
    start_app()
    
    