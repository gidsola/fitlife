
from src.friend import showFriendsMenu
from src.challenge import showChallengesMenu
from src.leaderboard import showLeaderboardsMenu
# from src.notification import Notification
# from src.progressReport import ProgressReport


class SocialManager:
    def __init__(self, social_manager_id):
        self.social_manager_id = social_manager_id

    def connect_with_friend(self, friend):
        print(f"Connecting with friend: {friend.friend_name}")

    def join_challenge(self, challenge):
        print(f"Joining challenge: {challenge.challenge_name}")

    def compete_on_leaderboard(self, leaderboard):
        print(f"Competing on leaderboard with metric: {leaderboard.metric}")


    
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


        

        

        
        
    