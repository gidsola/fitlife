

class SocialManager:
    def __init__(self, social_manager_id):
        self.social_manager_id = social_manager_id

    def connect_with_friend(self, friend):
        print(f"Connecting with friend: {friend.friend_name}")

    def join_challenge(self, challenge):
        print(f"Joining challenge: {challenge.challenge_name}")

    def compete_on_leaderboard(self, leaderboard):
        print(f"Competing on leaderboard with metric: {leaderboard.metric}")


    