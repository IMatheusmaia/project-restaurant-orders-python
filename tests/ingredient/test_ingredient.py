from src.models.ingredient import Ingredient, Restriction
# noqa: F401, E261, E501


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
    assert ingredient_3.restrictions == {Restriction.ANIMAL_MEAT,
                                         Restriction.ANIMAL_DERIVED}
    assert ingredient_4.restrictions == {Restriction.ANIMAL_MEAT,
                                         Restriction.SEAFOOD,
                                         Restriction.ANIMAL_DERIVED}
    assert ingredient_3.__eq__(ingredient_4) is False
    assert repr(ingredient_3) == "Ingredient('bacon')"
    assert repr(ingredient_4) == "Ingredient('camarão')"
    assert ingredient_3 != ingredient_4
    assert hash(ingredient_3) == hash("bacon")
