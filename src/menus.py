
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.user import User
    from src.activityManager import ActivityManager

# from src.challenge import Challenge
from src.deviceManager import DeviceManager
from src.emergencyContact import EmergencyContact
from src.fitnessTracker import FitnessTracker
from src.friend import Friend
from src.goal import Goal
from src.itSecurityOfficer import ITSecurityOfficer
from src.leaderboard import Leaderboard
from src.login import Login
from src.notification import Notification
from src.notificationManager import NotificationManager
from src.nutrition import Nutrition
from src.userProfile import Profile
from src.report import Report
from src.smartwatch import Smartwatch

def loginMenu() -> 'User | ITSecurityOfficer | None':
    print("Welcome to FitLife!")
    print("1. User Login")
    print("2. IT Security Officer Login")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        user_id = input("User ID: ")
        password = input("Password: ")
        return Login.userLogin(user_id=user_id, password=password)

    elif choice == "2":
        officer_id = input("Officer ID: ")
        name = input("Name: ")
        security_officer = ITSecurityOfficer(officer_id=int(officer_id), name=name, contact_info="security@fitlife.com")
        print("IT Security Officer login successful!")
        return security_officer

    elif choice == "3":
        print("Exiting FitLife. Goodbye!")
        return None
    
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
            if security_officer.enforceSecurityPolicies(int(user_id)):
                print(f"Security policies enforced successfully.")
            else:
                print("\nError while trying to enforce security policies.")

        elif choice == "2":
            security_officer.monitorSystemSecurity()

        elif choice == "3":
            user_id = input("Enter User ID to manage data encryption: ")
            security_officer.manageDataEncryption(int(user_id))

        elif choice == "4":
            user_id = input("Enter User ID to audit security compliance: ")
            security_officer.auditSecurityCompliance(int(user_id))

        elif choice == "N" or choice.lower() == "n":
            print("Creating a new user...")
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")

            try:
                new_user = security_officer.create_user(int(user_id), name, email, password)
                print(f"New user created successfully: {new_user.name}")
            except ValueError as e:
                print(f"Error creating user: {e}")

        elif choice == "5":
            print("Logging out...")
            break

def showUserDashboard(user: 'User | ITSecurityOfficer'):
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

def showGoalsMenu(user: 'User'):
    while True:
        print("1. Set Goal")
        print("2. View Goal")
        print("X. Exit")
        sub = input("Select: ")

        if sub == "1":
            goal_name = input("Goal name: ")
            if not goal_name:
                print("Goal name cannot be empty.")
                input("Press Enter to continue...")
                continue
            goal_type = input("Goal type (e.g., Steps): ")
            goal_value = int(input("Goal value (e.g., 10000): "))
            frequency = input("Frequency (e.g., Daily): ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")

            try:
                datetime.date.fromisoformat(start_date)
                datetime.date.fromisoformat(end_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                input("Press Enter to continue...")
                continue

            goal = Goal(
                goal_id=int(len(user.goals)) + 1,
                goal_name=goal_name,
                goal_type=goal_type,
                goal_value=goal_value,
                frequency=frequency,
                start_date=start_date,
                end_date=end_date
            )
            if goal.validate_goal():
                goal.set_goal(user, goal)
            else:
                print("Invalid goal.")

            input("Press Enter to continue...")

        elif sub == "2":
            if len(user.goals) > 0:
                for goal in user.goals:
                    print(goal)
                    input("Press Enter to view next goal...")
            else:
                print("No goals set yet.")
                input("Press Enter to continue...")
                
        elif sub == "X" or sub.lower() == "x":
            print("Exiting goal menu.")
            break

def showTrackingMenu(activity_manager: 'ActivityManager'):
    while True:
            print("\nActivity Tracking Menu")    
            print("\n1. Track Activity\n2. View Activities")
            sub = input("Select: ")

            if sub == "1":
                activity_type = input("Activity type (e.g., Running): ")
                try:
                    duration = int(input("Duration (minutes): "))
                    calories_burned = int(input("Calories burned: "))
                    date = input("Date (YYYY-MM-DD): ")
                    datetime.date.fromisoformat(date)
                except ValueError:
                    print("Invalid input or date format. Please use correct types and YYYY-MM-DD for date.")
                    input("Press Enter to continue...")
                    continue

                activity = activity_manager.createActivity(
                    activity_id=len(activity_manager.activities)+1, 
                    activity_type=activity_type, 
                    duration=duration, 
                    calories_burned=calories_burned, 
                    date=date
                )
                # activities.append(activity)
                activity_manager.trackActivity(activity)
                print("Activity tracked.")

            elif sub == "2":
                if activity_manager.activities:
                    for a in activity_manager.activities:
                        print(f"{a.date}: {a.activity_type}, {a.duration} min, {a.calories_burned} cal")
                else:
                    print("No activities tracked.")

            input("Press Enter to continue...")

def showNutritionMenu():
    nutritions = []
    while True:
        print("\nNutrition Tracking Menu")
        print("1. Log Nutrition")
        print("2. View Nutrition Log")
        print("0. Back to Main Menu")
        sub = input("Select: ")

        if sub == "1":
            food_item = input("Food item: ")
            quantity = input("Quantity: ")
            calories = int(input("Calories: "))
            nutritional_values = input("Nutritional values (e.g., Protein, Carbs, Fats): ")
            
            nutrition = Nutrition(nutrition_id=len(nutritions)+1, food_item=food_item, quantity=quantity, calories=calories, nutritional_values=nutritional_values)
            nutritions.append(nutrition)
            print("Nutrition logged.")

        elif sub == "2":
            if nutritions:
                for n in nutritions:
                    print(f"{n.nutrition_id}: {n.food_item}, {n.quantity}, {n.calories} cal, {n.nutritional_values}")
            else:
                print("No nutrition logged.")
                
        elif sub == "0":
            break
            
        else:
            print("Invalid option. Please try again.")
        
        input("Press Enter to continue...")
        
def showSocialMenu(user):
    while True:
        print("\nSocial Features Menu")
        print("1. Friends Management")
        print("2. Challenges")
        print("3. Leaderboards")
        print("0. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "0":
            break

        elif choice == "1":
            showFriendsMenu(user)

        elif choice == "2":
            showChallengesMenu(user)

        elif choice == "3":
            showLeaderboardsMenu(user)

        else:
            print("Invalid option. Please try again.")

        input("Press Enter to continue...")

def showFriendsMenu(user):
    friends = []
    while True:
        print("\nFriends Management Menu")
        print("1. Add Friend")
        print("2. View Friends")
        print("0. Back to Social Features Menu")

        choice = input("Select an option: ")

        if choice == "0":
            break

        elif choice == "1":
            friend_name = input("Friend name: ")
            friend = Friend(friend_id=len(friends)+1, friend_name=friend_name)
            friends.append(friend)
            print("Friend added.")

        elif choice == "2":
            if friends:
                for f in friends:
                    print(f"{f.friend_id}: {f.friend_name}")
            else:
                print("No friends added.")

        else:
            print("Invalid option. Please try again.")

        input("Press Enter to continue...")

def showChallengesMenu(user: 'User'):
    while True:
        print("\nChallenges Menu")
        print("1. Join Challenge")
        print("2. View Challenges")
        print("0. Back to Social Features Menu")
        choice = input("Select an option: ")
        if choice == "0":
            break

        elif choice == "1":
            challenge_name = input("Challenge name: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            user.social_manager.joinChallenge(challenge_name, start_date, end_date)

        elif choice == "2":
            user.social_manager.viewChallenges()
        else:
            print("Invalid option. Please try again.")
        input("Press Enter to continue...")
               
def showLeaderboardsMenu(user):
    leaderboards = []
    while True:
        print("\nLeaderboards Menu")
        print("1. Compete on Leaderboard")
        print("2. View Leaderboards")
        print("0. Back to Social Features Menu")

        choice = input("Select an option: ")

        if choice == "0":
            break

        elif choice == "1":
            metric = input("Leaderboard metric (e.g., Steps, Calories): ")
            leaderboard = Leaderboard(leaderboard_id=len(leaderboards)+1, metric=metric)
            leaderboards.append(leaderboard)
            print(f"Competing on leaderboard with metric: {leaderboard.metric}")

        elif choice == "2":
            if leaderboards:
                for lb in leaderboards:
                    print(f"{lb.leaderboard_id}: {lb.metric}")
            else:
                print("No leaderboards available.")

        else:
            print("Invalid option. Please try again.")

        input("Press Enter to continue...")

def showSyncMenu():
    while True:
            print("\n1. Sync Fitness Tracker\n2. Sync Smartwatch")
            sub = input("Select: ")

            if sub == "1":
                brand = input("Tracker brand: ")
                model = input("Tracker model: ")
                tracker = FitnessTracker(tracker_id=1)
                DeviceManager.sync_with_fitness_tracker(tracker)
                print(f"Synced with fitness tracker: {tracker.brand} {tracker.model}")

            elif sub == "2":
                brand = input("Smartwatch brand: ")
                model = input("Smartwatch model: ")
                watch = Smartwatch(watch_id=1, brand=brand, model=model)
                DeviceManager.sync_with_smartwatch(watch)
                print(f"Synced with smartwatch: {watch.brand} {watch.model}")

            input("Press Enter to continue...")

def showNotificationsMenu():
    notifications = []
    while True:
        print("\nNotification Preferences Menu")
        print("1. Send Notification")
        print("2. View Notifications")
        print("3. Customize Notification Preferences")
        print("4. Exit")
        sub = input("Select: ")

        if sub == "1":
            notification_type = input("Notification type: ")
            message = input("Message: ")
            date = input("Date (YYYY-MM-DD): ")
            notification = Notification(
                notification_id=len(notifications) + 1,
                notification_type=notification_type,
                message=message,
                date=date
            )
            notifications.append(notification)
            print("Notification sent.")

        elif sub == "2":
            if notifications:
                for n in notifications:
                    print(f"{n.date}: {n.notification_type} - {n.message}")
            else:
                print("No notifications.")

        elif sub == "3":
            nm = NotificationManager(notification_manager_id=1)
            nm.customize_notification_preferences()

        elif sub == "4":
            break

        else:
            print("Invalid option.")

        input("Press Enter to continue...")
        
def showProgressReportMenu(user):
        report_id = 1
        report_date = input("Report date (YYYY-MM-DD): ")
        report = Report(report_id=report_id, report_date=report_date, content="Progress report content")
        # user.view_progress_report(report)
        report.generate_visual_representation([1, 2, 3, 4, 5])
        input("Press Enter to continue...")
        
def showEmergencyContactMenu(user):
    emergency_contacts = []
    while True:
        print("\nEmergency Contact Menu")
        print("1. Add Emergency Contact")
        print("2. View Emergency Contacts")
        print("3. Notify Emergency Contact")
        print("0. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == "0":
            break

        elif choice == "1":
            name = input("Contact Name: ")
            phone_number = input("Phone Number: ")
            relationship = input("Relationship: ")
            contact = EmergencyContact(contact_id=len(emergency_contacts)+1, name=name, phone_number=phone_number, relationship=relationship)
            emergency_contacts.append(contact)
            # do the save
            print("Emergency contact added.")

        elif choice == "2":
            if emergency_contacts:
                for c in emergency_contacts:
                    print(f"{c.contact_id}: {c.name}, {c.phone_number}, {c.relationship}")
            else:
                print("No emergency contacts added.")

        elif choice == "3":
            if emergency_contacts:
                contact_id = int(input("Enter contact ID to notify: "))
                if 0 < contact_id <= len(emergency_contacts):
                    message = input("Enter message (optional): ")
                    emergency_contacts[contact_id-1].notify_emergency_contact(message)
                else:
                    print("Invalid contact ID.")
            else:
                print("No emergency contacts to notify.")

        else:
            print("Invalid option. Please try again.")
            
def showProfileMenu(user):
    print("\nProfile Menu")
    print("1. Create Profile")
    print("2. Update Profile")
    print("3. View Profile")
    print("0. Back to Main Menu")

    choice = input("Select: ")

    if choice == "1":
        profile = Profile.create_profile()
        print(f"Profile created: Age {profile.age}, Height {profile.height} cm, Weight {profile.weight} kg")
    
    elif choice == "2":
        if 'profile' in globals():
            age = input("New Age (leave blank to keep current): ")
            height = input("New Height (cm, leave blank to keep current): ")
            weight = input("New Weight (kg, leave blank to keep current): ")
            profile.update_profile(age=int(age) if age else None, 
                                   height=float(height) if height else None, 
                                   weight=float(weight) if weight else None)
        else:
            print("No profile found. Please create a profile first.")
            
    elif choice == "3":
        if user.profile:
            print(user.profile)
        else:
            print("No profile found. Please create a profile first.")
    
    elif choice == "0":
        return
    
    else:
        print("Invalid option. Please try again.")
    
    input("Press Enter to continue...")


        