
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
