def main():
    restaurants = [
        {"name": "Joe’s Gourmet Burgers", "vegetarian": False, "vegan": False, "gluten_free": False},
        {"name": "Main Street Pizza Company", "vegetarian": True, "vegan": False, "gluten_free": True},
        {"name": "Corner Café", "vegetarian": True, "vegan": True, "gluten_free": True},
        {"name": "Mama’s Fine Italian", "vegetarian": True, "vegan": False, "gluten_free": False},
        {"name": "The Chef’s Kitchen", "vegetarian": True, "vegan": True, "gluten_free": True} 
        ]

    vegetarian = input("Is anyone in your party a vegetarian? ").lower() == 'yes'
    vegan = input("Is anyone in your party a vegan? ").lower() == 'yes'
    gluten_free = input("Is anyone in your party gluten-free? ").lower() == 'yes'

    print("Here are your restaurant choices:")
    for restaurant in restaurants:
        if (not vegetarian or restaurant["vegetarian"]) and \
           (not vegan or restaurant["vegan"]) and \
           (not gluten_free or restaurant["gluten_free"]):
            print(restaurant["name"])

main()