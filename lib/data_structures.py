spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list = [food["name"] for food in spicy_foods]
    return names_list

def get_spiciest_foods(spicy_foods):
    spiciest_list = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name", "Unknown")
        heat_level = food.get("heat_level", 0)
        cuisine = food.get("cuisine", "Unknown")
        chilis =  "🌶" * heat_level        
        print(f"{name} ({cuisine}) | Heat Level: {chilis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
    
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get("heat_level", 0)
        name = food.get("name", "Unknown")
        cuisine = food.get("cuisine", "Unknown")
        chilis =  "🌶" * heat_level
        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {chilis}")

def get_average_heat_level(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
