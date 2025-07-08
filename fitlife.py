

import datetime

# from src.dataManager import DataManager
from src.activity import Activity
from src.activityManager import ActivityManager
from src.user import User
from src.userProfile import Profile
from src.goal import Goal
from src.emergencyContact import EmergencyContact
from src.nutrition import Nutrition
from src.nutritionManager import NutritionManager
from src.friend import Friend
from src.challenge import Challenge
from src.leaderboard import Leaderboard
from src.fitnessTracker import FitnessTracker
from src.smartwatch import Smartwatch
from src.notification import Notification
from src.notificationManager import NotificationManager
from src.progressReport import ProgressReport
from src.login import Login
from src.itSecurityOfficer import ITSecurityOfficer
from src.deviceManager import DeviceManager



def main_menu(user):
    activity_manager = ActivityManager(activity_manager_id=1)
    nutrition_manager = NutritionManager(nutrition_manager_id=1)
    device_manager = DeviceManager(device_manager_id=1)
    activities = []
    nutritions = []
    friends = []
    challenges = []
    notifications = []
    leaderboards = []

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
        print("9. Update Profile")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "0":
            print("Exiting FitLife. Goodbye!")
            break

        elif choice == "1":
            Goal.goalMenu(user)

        elif choice == "2":
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

                activity = Activity(activity_id=len(activities)+1, activity_type=activity_type, duration=duration, calories_burned=calories_burned, date=date)
                activities.append(activity)
                activity_manager.track_activity(activity)
                print("Activity tracked.")

            elif sub == "2":
                if activities:
                    for a in activities:
                        print(f"{a.date}: {a.activity_type}, {a.duration} min, {a.calories_burned} cal")
                else:
                    print("No activities tracked.")

            input("Press Enter to continue...")

        elif choice == "3":
            print("\n1. Log Nutrition\n2. View Nutrition Logs")
            sub = input("Select: ")

            if sub == "1":
                food_item = input("Food item: ")
                quantity = input("Quantity: ")
                calories = input("Calories: ")
                nutritional_values = input("Nutritional values (comma separated): ")
                nutrition = Nutrition(nutrition_id=len(nutritions)+1, food_item=food_item, quantity=quantity, calories=calories, nutritional_values=nutritional_values)
                nutritions.append(nutrition)
                nutrition_manager.log_nutrition(nutrition)
                print("Nutrition logged.")

            elif sub == "2":
                if nutritions:
                    for n in nutritions:
                        print(f"{n.food_item}, {n.quantity}, {n.calories} cal, {n.nutritional_values}")
                else:
                    print("No nutrition logs.")

            input("Press Enter to continue...")

        elif choice == "4":
            print("\n1. Add Friend\n2. View Friends\n3. Join Challenge\n4. View Challenges\n5. Compete on Leaderboard\n6. View Leaderboard")
            sub = input("Select: ")

            if sub == "1":
                friend_name = input("Friend name: ")
                friend = Friend(friend_id=len(friends)+1, friend_name=friend_name)
                friends.append(friend)
                print("Friend added.")

            elif sub == "2":
                if friends:
                    for f in friends:
                        print(f"{f.friend_id}: {f.friend_name}")
                else:
                    print("No friends added.")

            elif sub == "3":
                challenge_name = input("Challenge name: ")
                start_date = input("Start date (YYYY-MM-DD): ")
                end_date = input("End date (YYYY-MM-DD): ")
                challenge = Challenge(challenge_id=len(challenges)+1, challenge_name=challenge_name, start_date=start_date, end_date=end_date)
                challenges.append(challenge)
                print("Challenge joined.")

            elif sub == "4":
                if challenges:
                    for c in challenges:
                        print(f"{c.challenge_id}: {c.challenge_name}, {c.start_date} to {c.end_date}")
                else:
                    print("No challenges joined.")

            elif sub == "5":
                metric = input("Leaderboard metric (e.g., Steps, Calories): ")
                leaderboard = Leaderboard(leaderboard_id=len(leaderboards)+1, metric=metric)
                leaderboards.append(leaderboard)
                print(f"Competing on leaderboard with metric: {leaderboard.metric}")

            elif sub == "6":
                if leaderboards:
                    for lb in leaderboards:
                        print(f"{lb.leaderboard_id}: {lb.metric}")
                else:
                    print("No leaderboards available.")

            input("Press Enter to continue...")

        elif choice == "5":
            print("\n1. Sync Fitness Tracker\n2. Sync Smartwatch")
            sub = input("Select: ")

            if sub == "1":
                brand = input("Tracker brand: ")
                model = input("Tracker model: ")
                tracker = FitnessTracker(tracker_id=1, brand=brand, model=model)
                device_manager.sync_with_fitness_tracker(tracker)
                print(f"Synced with fitness tracker: {tracker.brand} {tracker.model}")

            elif sub == "2":
                brand = input("Smartwatch brand: ")
                model = input("Smartwatch model: ")
                watch = Smartwatch(watch_id=1, brand=brand, model=model)
                device_manager.sync_with_smartwatch(watch)
                print(f"Synced with smartwatch: {watch.brand} {watch.model}")

            input("Press Enter to continue...")

        elif choice == "6":
            print("\n1. Send Notification\n2. View Notifications")
            sub = input("Select: ")

            if sub == "1":
                notification_type = input("Notification type: ")
                message = input("Message: ")
                date = input("Date (YYYY-MM-DD): ")
                notification = Notification(notification_id=len(notifications)+1, notification_type=notification_type, message=message, date=date)
                notifications.append(notification)
                print("Notification sent.")

            elif sub == "2":
                if notifications:
                    for n in notifications:
                        print(f"{n.date}: {n.notification_type} - {n.message}")
                else:
                    print("No notifications.")

            input("Press Enter to continue...")

        elif choice == "7":
            report_id = 1
            report_date = input("Report date (YYYY-MM-DD): ")
            report = ProgressReport(report_id=report_id, report_date=report_date)
            user.view_progress_report(report)
            report.generate_visual_representation([1, 2, 3, 4, 5])
            input("Press Enter to continue...")

        elif choice == "8":
            print("\n1. Set Emergency Contact\n2. Notify Emergency Contact\n3. View Emergency Contact")
            sub = input("Select: ")

            if sub == "1":
                name = input("Contact name: ")
                phone = input("Phone number: ")
                relationship = input("Relationship: ")
                contact = EmergencyContact(contact_id=1, name=name, phone_number=phone, relationship=relationship)
                user.set_emergency_contact(contact)

            elif sub == "2":
                if user.emergency_contact:
                    user.emergency_contact.notify_emergency_contact()
                else:
                    print("No emergency contact set.")

            elif sub == "3":
                if user.emergency_contact:
                    c = user.emergency_contact
                    print(f"{c.name} ({c.relationship}) - {c.phone_number}")
                else:
                    print("No emergency contact set.")

            input("Press Enter to continue...")

        elif choice == "9":
            print("\n1. Update Profile\n2. View Profile")
            sub = input("Select: ")

            if sub == "1":
                age = input("Age: ")
                height = input("Height (cm): ")
                weight = input("Weight (kg): ")
                profile = Profile(profile_id=1, age=age, height=height, weight=weight)
                user.set_profile(profile)

            elif sub == "2":
                if user.profile:
                    # profile_attrs = vars(dict(user.profile))
                    print(f"Name: {user.name}")
                    print(f"Email: {user.email}")
                    print(f"Profile: {user.profile}")
                else:
                    print("No profile set.")

            input("Press Enter to continue...")


def start_app():
    while True:
        user = Login.loginMenu()
        
        if isinstance(user, ITSecurityOfficer):
            user.it_security_menu(user)
            break
        elif isinstance(user, User):
            main_menu(user)
            break
        
        else:
            print("Invalid login. Please try again.")

if __name__ == "__main__":
    start_app()