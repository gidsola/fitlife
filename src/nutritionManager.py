

from src.nutrition import Nutrition

class NutritionManager:
    def __init__(self, nutrition_manager_id):
        self.nutrition_manager_id = nutrition_manager_id
        self.nutrition_logs = []

    def log_nutrition(self, nutrition: Nutrition, source="manual"):
        self.nutrition_logs.append(nutrition)
        print(f"Logging nutrition: {nutrition.food_item} from {source}")

    def calculate_nutritional_values(self, nutrition: Nutrition):
        nutritional_values = {"calories": nutrition.calories, "carbs": 30, "protein": 10}
        print(f"Calculating nutritional values for {nutrition.food_item}: {nutritional_values}")
        return nutritional_values

    def get_nutrition_logs(self):
        return self.nutrition_logs

