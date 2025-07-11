

from src.nutrition import Nutrition

class NutritionManager:
    def __init__(self, nutrition_manager_id):
        self.nutrition_manager_id = nutrition_manager_id
        self.nutrition_logs = []

    def log_nutrition(self, nutrition_id, food_item, quantity, calories, nutritional_values, source="manual"):
        nutrition = Nutrition(
            nutrition_id=nutrition_id,
            food_item=food_item,
            quantity=quantity,
            calories=calories,
            nutritional_values=nutritional_values
        )
        self.nutrition_logs.append(nutrition)
        print(f"Logging nutrition: {nutrition.food_item} from {source}")

    def calculate_nutritional_values(self, food_item, quantity):
        """Calculates nutritional values based on food item and quantity."""
        responseJSON = {
            "protein": quantity * 0.1,
            "carbs": quantity * 0.2,
            "fats": quantity * 0.05
        }
        return responseJSON

    def getNutritionItems(self) -> list[Nutrition]:
        """Retrieves all nutrition logs."""
        return self.nutrition_logs

