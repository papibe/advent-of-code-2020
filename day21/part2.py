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
    identifiedAllergens = {}

    nallergen = len(allergensD.keys())
    while nallergen > 0:
        # Obtain one allergen
        for allergen, ingredientList in allergensD.items():
            inter = reduce(lambda a,b: a&b, ingredientList)
            if len(inter) == 1:
                aToRemove = inter.pop()
                identifiedAllergens[allergen] = aToRemove
                break

        # Remove discovered allerger from all foods
        for allergen, ingredientList in allergensD.items():
            for ingredient in ingredientList:
                if aToRemove in ingredient:
                    ingredient.remove(aToRemove)

        nallergen -= 1

    sortAllergens = list(identifiedAllergens.keys())
    sortAllergens.sort()

    # canonical dangerous ingredient list
    cdil = [identifiedAllergens[allergen] for allergen in sortAllergens]

    return ','.join(cdil)


if __name__ == "__main__":

    print(solution("./example.txt"))    # mxmxvkd,sqjhc,fvjkl
    print(solution("./input.txt"))
