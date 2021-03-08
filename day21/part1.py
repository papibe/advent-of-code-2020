import re
import itertools
from functools import reduce
from copy import deepcopy

def solution(filename):

    def getLines(filename):
        with open(filename, 'r') as fp:
            data = fp.read().splitlines()
        return data

    foodLine = re.compile('^([^\(]*)\(contains (.*)\)')

    allergensD = {}
    onlyIngredientsList = []

    data = getLines(filename)
    for line in data:
        mg = foodLine.match(line)

        # parse ingredients
        rawIngredients = mg[1]
        ingredients = rawIngredients.strip().split()
        onlyIngredientsList.append(ingredients)

        # parse allergens
        rawAllergens = mg[2]
        splitAllergens = rawAllergens.split(',')
        allergens = [s.strip() for s in splitAllergens]

        for allergen in allergens:
            if allergen not in allergensD:
                allergensD[allergen] = [set(ingredients)]
            else:
                allergensD[allergen].append(set(ingredients))

    originalFoods = deepcopy(allergensD)

    nallergen = len(allergensD.keys())
    while nallergen > 0:
        # Obtain one allergen
        for allergen, ingredientList in allergensD.items():
            inter = reduce(lambda a,b: a&b, ingredientList)
            if len(inter) == 1:
                aToRemove = inter.pop()
                break

        # Remove discovered allergers from all foods
        for allergen, ingredientList in allergensD.items():
            for ingredient in ingredientList:
                if aToRemove in ingredient:
                    ingredient.remove(aToRemove)

        nallergen -= 1

    # Mix all non allergen ingredients:
    goodFood = set()
    for allergen, ingredientList in allergensD.items():
        foods = reduce(lambda a,b: a|b, ingredientList)
        goodFood |= foods

    appear = 0
    for ingredientList in onlyIngredientsList:
        for ingredient in ingredientList:
            if ingredient in goodFood:
                appear += 1

    return appear


if __name__ == "__main__":
    print(solution("./example.txt"))    # 5
    print(solution("./input.txt"))
