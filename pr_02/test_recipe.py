import unittest
from pr_02_cooker import Recipe, Ingredient

class TestRecipe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recipes = [
            {
                "title": "Пицца с ананасом",
                "ingredients_list": [
                    ('Тесто', 500, 500, 150),
                    ('Сыр', 200, 180, 250),
                    ('Помидор', 100, 70, 60),
                    ('Ананас', 130, 95, 300),
                    ('Колбаса', 150, 139, 200)
                ],
            },

            {
                "title": "Мармелад с томатным соком",
                "ingredients_list": [
                    ('Томатное пюре', 80, 70, 99),
                    ('Сахар', 40, 38, 30),
                    ('Патока', 100, 80, 200),
                    ('Желатин', 20, 15, 30),
                    ('Лимонная кислота', 15, 14, 40)
                ],
            }
        ]

    def setUp(self):
        self.dishes = [Recipe(recipe['title'], recipe['ingredients_list']) for recipe in self.recipes]

    def test_calc_cost(self):
        params = [960.0, 399.0]
        for i, dish in enumerate(self.dishes):
            with self.subTest("test_calc_cost"):
                self.assertEqual(dish.calc_cost(), params[i])

    def test_calc_raw_weight(self):
        params = [1080.0, 255.0]
        for i, dish in enumerate(self.dishes):
            with self.subTest("test_calc_raw_weight"):
                self.assertEqual(dish.calc_weight(), params[i])

    def test_calc_weight(self):
        params = [984.0, 217.0]
        for i, dish in enumerate(self.dishes):
            with self.subTest("test_calc_weight"):
                self.assertEqual(dish.calc_weight(raw=False), params[i])

    def test_ingredient_validation(self):
        params = [
            {
                'name'      : '',
                'raw_weight': 1,
                'weight'    : 1,
                'cost'      : 1,
            },
            {
                'name'      : 'name',
                'raw_weight': -1,
                'weight'    : 1,
                'cost'      : 1,
            },
            {
                'name'      : 'name',
                'raw_weight': 1,
                'weight'    : -1,
                'cost'      : 1,
            },
            {
                'name'      : 'name',
                'raw_weight': 1,
                'weight'    : 1,
                'cost'      : -1,
            },
        ]
        for param in params:
            with self.subTest("test_ingredient_validation"):
                with self.assertRaises(ValueError):
                    Ingredient(**param)


if __name__ == '__main__':
    unittest.main()