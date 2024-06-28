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
    names = [dict_item.get("name") for dict_item in spicy_foods]
    return names
    # names = []
    # for dict_item in spicy_foods:
    #     names.append(dict_item.get("name"))
    # return names


def get_spiciest_foods(spicy_foods):
    names = [dict_item for dict_item in spicy_foods if dict_item.get("heat_level") > 5]
    return names

def print_spicy_foods(spicy_foods):
    for dict_item in spicy_foods:
        print(f'{dict_item.get("name")} ({dict_item.get("cuisine")}) | Heat Level: {"🌶" * dict_item.get("heat_level")}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    names = [dict_item for dict_item in spicy_foods if dict_item.get("cuisine") == cuisine]
    return names[0]

def print_spiciest_foods(spicy_foods):
    for dict_item in spicy_foods:
        if dict_item.get("heat_level") > 5:
            print(f'{dict_item.get("name")} ({dict_item.get("cuisine")}) | Heat Level: {"🌶" * dict_item.get("heat_level")}')


def get_average_heat_level(spicy_foods):
    names = [dict_item.get("heat_level") for dict_item in spicy_foods]
    return sum(names)/len(names)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
