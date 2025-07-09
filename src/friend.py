


class Friend:
    def __init__(self, friend_id, friend_name):
        self.friend_id = friend_id
        self.friend_name = friend_name
        
        
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
        
        