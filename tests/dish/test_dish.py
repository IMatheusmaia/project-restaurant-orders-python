import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
# noqa: F401, E261, E501


# Req 2
def test_dish():
    first_dish = Dish("Risoto de Camarão", 49.90)
    first_dish_duplicate = Dish("Risoto de Camarão", 49.90)
    second_dish = Dish("Hamburguer", 23.90)

    assert first_dish.name == "Risoto de Camarão"
    assert str(first_dish) == "Dish('Risoto de Camarão', R$49.90)"
    assert hash(first_dish) == hash(first_dish_duplicate)
    assert hash(first_dish) != hash(second_dish)
    assert first_dish == first_dish
    assert first_dish == first_dish_duplicate
    assert first_dish != second_dish

    with pytest.raises(TypeError,
                       match="Dish price must be float."):
        Dish("Any dish", '10')
    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("Another dish", 0)

    ingredient_second_dish = Ingredient("carne")
    second_dish.add_ingredient_dependency(ingredient_second_dish, 350)

    assert second_dish.recipe.get(ingredient_second_dish) == 350
    assert second_dish.get_restrictions() == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}

    ingredient_first_dish = Ingredient("camarão")
    first_dish.add_ingredient_dependency(ingredient_first_dish, 250)

    assert first_dish.recipe.get(ingredient_first_dish) == 250
    assert first_dish.get_restrictions() == {Restriction.ANIMAL_MEAT,
                                             Restriction.SEAFOOD,
                                             Restriction.ANIMAL_DERIVED}

    assert Ingredient("camarão") in first_dish.get_ingredients()
    assert Ingredient("carne") in second_dish.get_ingredients()
