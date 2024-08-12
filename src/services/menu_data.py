import csv
from typing_extensions import Set
from models.ingredient import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self._read_csv_and_create_dishes()

    def _read_csv_and_create_dishes(self) -> Set[Dish]:
        dish_dict = dict()

        with open(self.source_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                quantity = int(row["recipe_amount"])

                if dish_name not in dish_dict:
                    dish_dict[dish_name] = Dish(dish_name, price)

                dish_dict[dish_name].add_ingredient_dependency(
                    Ingredient(ingredient_name), quantity
                )

        return set(dish_dict.values())
