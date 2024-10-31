# (П)орынов -> (П)ицца с ананасом
# (М)атвей -> (М)армелад с томатным соком

from pydantic import BaseModel, field_validator


class Ingredient(BaseModel):
    name       : str
    raw_weight : float
    weight     : float
    cost       : float

    @field_validator('name')
    def validate_name(cls, v):
        if not v:
            raise ValueError("field name must not be empty")
        return v
        
    @field_validator('raw_weight')
    def validate_raw_weight(cls, v):
        if v < 0:
            raise ValueError("field raw_weight must be positive")
        return v
    
    @field_validator('weight')
    def validate_weight(cls, v):
        if v < 0:
            raise ValueError("field weight must be positive")
        return v
    
    @field_validator('cost')
    def validate_cost(cls, v):
        if v < 0:
            raise ValueError("field cost must be positive")
        return v
    


class Recipe:

    def __init__(self, name:str, ingredient_list:list[tuple[str, int, int, int]]) -> None:
        self.name = name
        self.ingredients = [
            Ingredient(
                name=_name, 
                raw_weight=raw_weight, 
                weight=weight, 
                cost=cost
            ) 
            for _name, raw_weight, weight, cost 
            in ingredient_list
        ]

    def calc_cost(self, portions=1):
        return sum(map(lambda x: x.cost, self.ingredients)) * portions

    def calc_weight(self, portions=1, raw=True):
        return sum(map(lambda x: x.raw_weight if raw else x.weight, self.ingredients)) * portions

    def __str__(self) -> str:
        return f"Recipe(name={self.name}, ingredients=[{', '.join([ingredient.name for ingredient in self.ingredients])}])"



if __name__ == '__main__':
    recipe_list_1 = {
    "title": "Пицца с ананасом",
        "ingredients_list": [
            ('Тесто', 500, 500, 150),
            ('Сыр', 200, 180, 250),
            ('Помидор', 100, 70, 60),
            ('Ананас', 130, 95, 300),
            ('Колбаса', 150, 139, 200)
        ],
    }

    recipe_list_2 = {
        "title": "Мармелад с томатным соком",
        "ingredients_list": [
            ('Томатное пюре', 80, 70, 99),
            ('Сахар', 40, 38, 30),
            ('Патока', 100, 80, 200),
            ('Желатин', 20, 15, 30),
            ('Лимонная кислота', 15, 14, 40)
        ],
    }

    recipe_1 = Recipe(recipe_list_1['title'], recipe_list_1['ingredients_list'])
    recipe_2 = Recipe(recipe_list_2['title'], recipe_list_2['ingredients_list'])

    # напишите самопроверку, что вызовы отрабатывают без ошибок на Вашем Рецепте
    print(recipe_1.calc_cost())
    print(recipe_1.calc_weight())
    print(recipe_1.calc_weight(raw=False))

    print(recipe_2.calc_cost())
    print(recipe_2.calc_weight())
    print(recipe_2.calc_weight(raw=False))

