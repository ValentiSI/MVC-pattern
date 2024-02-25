from dataclasses import dataclass
from typing import List

# # 1 -------------------------------------------------------------------------------
# print('Задание 1. Создайте класс Обувь. Необходимо хранить следующую информацию:\
# \n■ тип обуви;\
# \n\t✓ мужская,\
# \n\t✓ женская;\
# \n■ вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.);\
# \n■ цвет;\
# \n■ цена;\
# \n■ производитель;\
# \n■ размер.\
# \nСоздайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Обувь и код для использования модели, контроллера и представления.\n')

@dataclass
class Shoe:
    shoe_type: str
    shoe_style: str
    color: str
    price: float
    manufacturer: str
    size: int

    def update_price(self, new_price):
        self.price = new_price

    def update_size(self, new_size):
        self.size = new_size
        
    def update_color(self, new_color):
        self.color = new_color
        
class ShoeModel:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)
        
    def remove_shoe(self, shoe):
        self.shoes.remove(shoe)

    def get_all_shoes(self):
        return self.shoes

class ShoeView:
    def display_shoes(self, shoes):
        for shoe in shoes:
            shoe_dict = {
                "Тип обуви": shoe.shoe_type,
                "Вид обуви": shoe.shoe_style,
                "Цвет": shoe.color,
                "Цена": ("$" + str(shoe.price)),
                "Производитель": shoe.manufacturer,
                "Размер": shoe.size
            }
            for key, value in shoe_dict.items():
                print(f"{key}: {value}")
            print()

class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_shoe(self, shoe):
        self.model.add_shoe(shoe)
        
    def remove_shoe(self, shoe):
        self.model.remove_shoe(shoe)

    def update_price(self, shoe, new_price):
        shoe.update_price(new_price)

    def update_size(self, shoe, new_size):
        shoe.update_size(new_size)
        
    def update_color(self, shoe, new_color):
        shoe.update_color(new_color)

    def show_shoes(self):
        shoes = self.model.get_all_shoes()
        self.view.display_shoes(shoes)
        
# Создаем экземпляры модели, представления и контроллера
model = ShoeModel()
view = ShoeView()
controller = ShoeController(model, view)

# Добавляем обувь в модель
shoe1 = Shoe("мужская", "кроссовки", "черный", 99.37, "Nike", 42)
controller.add_shoe(shoe1)

shoe2 = Shoe("женская", "туфли", "красный", 79.65, "Gucci", 37)
controller.add_shoe(shoe2)

shoes3 = Shoe("мужская", "туфли", "белый", 120.00, "Adidas", 45)
controller.add_shoe(shoes3)

controller.show_shoes()
print('********************************')

controller.update_price(shoe1, 109.45)
controller.update_size(shoe2, 39)
controller.update_color(shoes3, "зеленый")

controller.show_shoes()

# 2 --------------------------------------------------------------------------------------
print('Задание 2. Создайте класс Рецепт. Необходимо хранить следующую информацию:\
\n■ название рецепта;\
\n■ автор рецепта;\
\n■ тип рецепта (первое, второе блюдо и т.д.);\
\n■ текстовое описание рецепта;\
\n■ ссылка на видео с рецептом;\
\n■ список ингредиентов;\
\n■ название кухни (итальянская, французская, украинская и т.д.).\
\nСоздайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Рецепт и код для использования модели, контроллера и представления.\n')

@dataclass
class RecipeModel:
    name: str
    author: str
    recipe_type: str
    description: str
    video_link: str
    ingredients: List[str]
    cuisine: str

    def update_description(self, new_description):
        self.description = new_description
    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
                
class RecipeView:
    def display_recipe(self, recipe):
        print(f"Название: {recipe.name}")
        print(f"Автор: {recipe.author}")
        print(f"Тип: {recipe.recipe_type}")
        print(f"Описание: {recipe.description}")
        print(f"Ссылка на видео: {recipe.video_link}")
        print("Ингредиенты (на 2 л бульона):")
        for ingredient in recipe.ingredients:
            print(f"- {ingredient}")
        print(f"Кухня: {recipe.cuisine}")


class RecipeController:
    def __init__(self, model: RecipeModel, view: RecipeView):
        self.model = model
        self.view = view

    def update_description(self, new_description):
        self.model.description = new_description
    
    def add_ingredient(self, ingredient):
        self.model.ingredients.append(ingredient)
        
    def show_recipe(self):
        self.view.display_recipe(self.model)

model = RecipeModel(
    name = "Борщ",
    author = "Иванова",
    recipe_type = "Первое блюдо",
    description = "Традиционный украинский суп с капустой, свеклой и мясом.",
    video_link = "https://www.youtube.com/watch?v=ur_lfpcwjAY",
    ingredients = ["500 г Мясо на косточке", "200 г свеклы", "150 г капусты", "110 г картофеля", "100 г моркови", "100 г лука", "2 ст.л. томатного пюре", "3 ч.л. уксуса 9%", "3 ч.л. сахара", "зелень", "соль", "перец болгарский", "сметана для подачи", "масло для жарки и тушения"],
    cuisine = "Украинская"
)

view = RecipeView()
controller = RecipeController(model, view)
controller.show_recipe()
print('********************************')

controller.update_description("Вкусный украинский суп с ароматным чесночком, капустой, свеклой, cмачным мясом.")
controller.add_ingredient("чеснок")

controller.show_recipe()