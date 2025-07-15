
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.user import User

from src.friend import Friend
from src.challenge import Challenge
from src.leaderboard import Leaderboard

class SocialManager:
    def __init__(self, user: 'User'):
        self.user = user
        # need to add loading saved vals(gotta save em first..)
        self.friends: list[Friend] = []
        self.challenges: list[Challenge] = []
        self.leaderboards: list[Leaderboard] = []
        

    def connectWithFriend(self, friend: Friend):
        print(f"Connecting with friend: {friend.friend_name}")

    def joinChallenge(self, challenge_name: str, start_date: str, end_date: str):
        self.challenges.append(Challenge(
            challenge_id=len(self.challenges)+1, 
            challenge_name=challenge_name, 
            start_date=start_date, 
            end_date=end_date
        ))
        print("Challenge joined.")
        
    def viewChallenges(self):
        if not self.challenges:
            print("No challenges joined.")
            return
        print("Challenges:")
        for challenge in self.challenges:
            print(f"{challenge.challenge_id}: {challenge.challenge_name}, {challenge.start_date} to {challenge.end_date}")

    def compete_on_leaderboard(self, leaderboard: Leaderboard):
        print(f"Competing on leaderboard with metric: {leaderboard.metric}")

    def shareActivity(self, user: 'User', activity_id: int):
        activity = user.activity_manager.getActivity(activity_id)
        if not activity:
            print(f"Activity with ID {activity_id} not found.")
            return
        print(f"Sharing activity: {activity.activity_type} for {activity.duration} minutes.")

    def share_progress_report(self, report_id: int):
        print(f"Sharing progress report with ID: {report_id}")
        
    def shareNutritionInfo(self, user: 'User'):
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
