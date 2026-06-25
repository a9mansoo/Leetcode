from collections import deque

recipes = ["bread","sandwich"]
ingredients = [["yeast","flour"],["bread","meat"]]
supplies = ["yeast","flour","meat"]

ingredient_to_recipe = {}
recipe_ingredient_counter = {}


for recipe, ingredient in zip(recipes, ingredients):
    recipe_ingredient_counter[recipe] = len(ingredient)
    for ing in ingredient:
        if ing in ingredient_to_recipe:
            ingredient_to_recipe[ing].append(recipe)
        else:
            ingredient_to_recipe[ing] = [recipe]


print(ingredient_to_recipe)
print(recipe_ingredient_counter)

q = deque()

for supply in supplies:
    q.append(supply)

result = []
while q:
    item = q.popleft()

    if item not in ingredient_to_recipe:
        continue

    for recipe in ingredient_to_recipe[item]:
        recipe_ingredient_counter[recipe] -= 1
        if recipe_ingredient_counter[recipe] == 0:
            result.append(recipe)
            q.append(recipe)

print(result)



