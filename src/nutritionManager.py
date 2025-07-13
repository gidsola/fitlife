
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.user import User
from src.nutrition import Nutrition

class NutritionManager:
    def __init__(self, user: 'User'):
        self.user = user
        self.nutrition_logs: list[Nutrition] = []

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

    def getNutritionInfo(self, food_item, quantity):
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


    def shareNutritionLogs(self):
        nutrition_logs = self.getNutritionItems()
        generated = []
        for item in nutrition_logs:
            self.getNutritionInfo(item)
            generated.append(item)
            print(f"Sharing nutrition log: {item.food_item} - {item.calories} calories")
        return generated
