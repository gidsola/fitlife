

class Nutrition:
    def __init__(self, nutrition_id, food_item, quantity, calories, nutritional_values):
        self.nutrition_id = nutrition_id
        self.food_item = food_item
        self.quantity = quantity
        self.calories = calories
        self.nutritional_values = nutritional_values
        
        
def showNutritionMenu():
    nutritions = []
    while True:
        print("\nNutrition Tracking Menu")
        print("1. Log Nutrition")
        print("2. View Nutrition Log")
        print("0. Back to Main Menu")
        
        sub = input("Select: ")
        
        if sub == "1":
            food_item = input("Food item: ")
            quantity = input("Quantity: ")
            calories = int(input("Calories: "))
            nutritional_values = input("Nutritional values (e.g., Protein, Carbs, Fats): ")
            
            nutrition = Nutrition(nutrition_id=len(nutritions)+1, food_item=food_item, quantity=quantity, calories=calories, nutritional_values=nutritional_values)
            nutritions.append(nutrition)
            print("Nutrition logged.")
            
        elif sub == "2":
            if nutritions:
                for n in nutritions:
                    print(f"{n.nutrition_id}: {n.food_item}, {n.quantity}, {n.calories} cal, {n.nutritional_values}")
            else:
                print("No nutrition logged.")
                
        elif sub == "0":
            break
            
        else:
            print("Invalid option. Please try again.")
        
        input("Press Enter to continue...")