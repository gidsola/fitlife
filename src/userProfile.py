
# from src.dataManager import DataManager
# from src.user import User

class Profile:
    def __init__(self, age: int, height: float, weight: float):
        self.age = age
        self.height = height
        self.weight = weight
        
    def __str__(self):
        return (
            f"--- User Profile ---\n"
            f"Age    : {self.age} years\n"
            f"Height : {self.height} cm\n"
            f"Weight : {self.weight} kg\n"
            f"---------------------"
        )

    def update_profile(self, age=None, height=None, weight=None):
        if age:
            self.age = age
        if height:
            self.height = height
        if weight:
            self.weight = weight
        print("Profile updated")
    
    @staticmethod    
    def create_profile() -> 'Profile':
        print("Create Your Profile")
        
        age = input("Age: ")
        height = input("Height (cm): ")
        weight = input("Weight (kg): ")

        return Profile(int(age), float(height), float(weight))
    

    # def set_profile(self, profile):
    #     self.profile = profile
    #     print(f"Profile updated for user {self.name}.")
    
    
def showProfileMenu(user):
    print("\nProfile Menu")
    print("1. Create Profile")
    print("2. Update Profile")
    print("3. View Profile")
    print("0. Back to Main Menu")

    choice = input("Select: ")

    if choice == "1":
        profile = Profile.create_profile()
        print(f"Profile created: Age {profile.age}, Height {profile.height} cm, Weight {profile.weight} kg")
    
    elif choice == "2":
        if 'profile' in globals():
            age = input("New Age (leave blank to keep current): ")
            height = input("New Height (cm, leave blank to keep current): ")
            weight = input("New Weight (kg, leave blank to keep current): ")
            profile.update_profile(age=int(age) if age else None, 
                                   height=float(height) if height else None, 
                                   weight=float(weight) if weight else None)
        else:
            print("No profile found. Please create a profile first.")
            
    elif choice == "3":
        if user.profile:
            print(user.profile)
        else:
            print("No profile found. Please create a profile first.")
    
    elif choice == "0":
        return
    
    else:
        print("Invalid option. Please try again.")
    
    input("Press Enter to continue...")
    
    