


class Leaderboard:
    def __init__(self, leaderboard_id, metric):
        self.leaderboard_id = leaderboard_id
        self.metric = metric

    def update_rankings(self):
        print(f"Updating rankings for leaderboard {self.leaderboard_id}")