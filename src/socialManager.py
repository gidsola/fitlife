

from src.friend import Friend
from src.challenge import Challenge
from src.leaderboard import Leaderboard
from src.activity import Activity
from src.progressReport import ProgressReport
from src.nutrition import Nutrition

from src.friend import showFriendsMenu
from src.challenge import showChallengesMenu
from src.leaderboard import showLeaderboardsMenu

class SocialManager:
    def __init__(self, social_manager_id):
        self.social_manager_id = social_manager_id

    def connect_with_friend(self, friend: Friend):
        print(f"Connecting with friend: {friend.friend_name}")

    def join_challenge(self, challenge: Challenge):
        print(f"Joining challenge: {challenge.challenge_name}")

    def compete_on_leaderboard(self, leaderboard: Leaderboard):
        print(f"Competing on leaderboard with metric: {leaderboard.metric}")

    def share_activity(self, activity: Activity):
        print(f"Sharing activity: {activity.activity_type}")

    def share_progress_report(self, progress_report: ProgressReport):
        print(f"Sharing progress report from: {progress_report.report_date}")
        
    def share_nutrition(self, nutrition: Nutrition):
        print(f"Sharing nutrition log: {nutrition.food_item} - {nutrition.calories} calories")
        
    def share_activity_achievement(self, activity):
        print(f"Sharing achievement: Completed {activity.activity_type} for {activity.duration} minutes!")

    def share_progress_report(self, progress_report):
        print(f"Sharing progress report from: {progress_report.report_date}")



    
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


        

        

        
        
    