


class Challenge:
    def __init__(self, challenge_id, challenge_name, start_date, end_date):
        self.challenge_id = challenge_id
        self.challenge_name = challenge_name
        self.start_date = start_date
        self.end_date = end_date
        
        
def showChallengesMenu(user):
    challenges = []
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
            challenge = Challenge(challenge_id=len(challenges)+1, challenge_name=challenge_name, start_date=start_date, end_date=end_date)
            challenges.append(challenge)
            print("Challenge joined.")

        elif choice == "2":
            if challenges:
                for c in challenges:
                    print(f"{c.challenge_id}: {c.challenge_name}, {c.start_date} to {c.end_date}")
            else:
                print("No challenges joined.")

        else:
            print("Invalid option. Please try again.")

        input("Press Enter to continue...")
        
        