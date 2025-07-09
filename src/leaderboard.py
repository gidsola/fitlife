


class Leaderboard:
    def __init__(self, leaderboard_id, metric):
        self.leaderboard_id = leaderboard_id
        self.metric = metric

    def update_rankings(self):
        print(f"Updating rankings for leaderboard {self.leaderboard_id}")
        
        
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
        
        