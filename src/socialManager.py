

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.user import User

from src.friend import Friend
from src.challenge import Challenge
from src.leaderboard import Leaderboard
from src.progressReport import ProgressReport

from src.friend import showFriendsMenu
from src.challenge import showChallengesMenu
from src.leaderboard import showLeaderboardsMenu

class SocialManager:
    def __init__(self, user: 'User'):
        self.user = user
        self.friends: list[Friend] = []
        self.challenges: list[Challenge] = []
        self.leaderboards: list[Leaderboard] = []
        

    def connect_with_friend(self, friend: Friend):
        print(f"Connecting with friend: {friend.friend_name}")

    def join_challenge(self, challenge: Challenge):
        print(f"Joining challenge: {challenge.challenge_name}")

    def compete_on_leaderboard(self, leaderboard: Leaderboard):
        print(f"Competing on leaderboard with metric: {leaderboard.metric}")

    def shareActivity(self, user: 'User', activity_id: int):
        activity = user.activity_manager.getActivity(activity_id)
        if not activity:
            print(f"Activity with ID {activity_id} not found.")
            return
        print(f"Sharing activity: {activity.activity_type} for {activity.duration} minutes.")

    def share_progress_report(self, progress_report: ProgressReport):
        print(f"Sharing progress report from: {progress_report.report_date}")
        
    def getNutritionInfo(self, user: 'User'):
        nutrition_items = user.nutrition_manager.getNutritionItems()
        if len(nutrition_items) == 0:
            print("No nutrition log to share.")
            return []
        print(f"Sharing nutrition log")
        
        for item in nutrition_items:
            print(f"Food Item: {item.food_item}, Quantity: {item.quantity}, Calories: {item.calories}, Nutritional Values: {item.nutritional_values}")
        return nutrition_items
    
    def share_activity_achievement(self, user: 'User', activity):
        message = f"Congratulations! You completed {activity.activity_type} for {activity.duration} minutes."
        user.notification_manager.sendNotification("Achievement", message, "2023-10-01")



    
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


        

        

        
        
    