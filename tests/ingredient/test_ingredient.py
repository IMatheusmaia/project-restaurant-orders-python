from src.models.ingredient import Ingredient, Restriction
import enum # noqa: F401, E261, E501

# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("Cebola")
    ingredient_2 = Ingredient("Cebola")

    assert ingredient_1.name == "Cebola"
    assert ingredient_1.restrictions == set()
    assert repr(ingredient_1) == "Ingredient('Cebola')"
    assert ingredient_1 == ingredient_2
    assert hash(ingredient_1) == hash("Cebola")

    ingredient_3 = Ingredient("bacon")
    ingredient_4 = Ingredient("camarão")
    
    assert ingredient_3.name == "bacon"
    assert ingredient_4.name == "camarão"

    assert repr(ingredient_3) == "Ingredient('bacon')"
    assert repr(ingredient_4) == "Ingredient('camarão')"
    assert ingredient_3 != ingredient_4
    assert hash(ingredient_3) == hash("bacon")