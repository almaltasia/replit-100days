# Day 3 Challenge
# 1. Create these as a variable:
# - A type of food
# - A type of plant
# - A method of cooking
# - A word to describe burned food
# - A household item
# 2. . Output a nice looking Recipe page that *concatenates* a dish in this format:
#     - cooking food with burned plant on a bed of item

food = input("Name a type of food: ")
plant = input("Name a plant: ")
cookingType = input("What is a way to cook something? ")
burntFood = input("How do you describe burnt food? ")
householdItem = input("Name something in your house: ")
print()
print("Tonight's dinner:")
print("For dinner you should make", cookingType, food, "with", burntFood, plant, "on a plate of", householdItem)