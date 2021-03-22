#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce


def load_input(input_file):
    foods = defaultdict(dict)
    i = 0
    with open(input_file) as f:
        for line in f:
            ingredients, allergens = line.strip().split("(contains ")
            foods[i]["ingredients"] = ingredients.split()
            foods[i]["allergens"] = allergens.replace(')', '').split(', ')
            i += 1
    return foods


def build_danger_ingredients(foods):
    # fish -> {{mxmxvkd kfcds sqjhc nhms}, {sqjhc mxmxvkd sbzzf}}
    # dairy -> {{mxmxvkd kfcds sqjhc nhms}, {trh fvjkl sbzzf mxmxvkd}}
    allergens_ingredients = defaultdict(list)
    for i, food in foods.items():
        for allergen in food["allergens"]:
            allergens_ingredients[allergen].append(food["ingredients"])
    # print(allergens_ingredients)

    danger_map = {}
    danger_ingredients = set()
    for allergen, v in allergens_ingredients.items():
        ingredients_with_allergy = set(reduce(
            lambda x, y: set.intersection(set(x), set(y)), v))
        # print(allergen, ingredients_with_allergy)
        danger_map[allergen] = ingredients_with_allergy
        for x in ingredients_with_allergy:
            danger_ingredients.add(x)

    # print("Danger: ", danger_ingredients)
    return danger_ingredients, danger_map


def part1(input_file):
    foods = load_input(input_file)
    danger_ingredients, _ = build_danger_ingredients(foods)

    safe_ingredients = 0
    for food in foods.values():
        for ingredient in food["ingredients"]:
            if ingredient not in danger_ingredients:
                safe_ingredients += 1

    return safe_ingredients


def part2(input_file):
    foods = load_input(input_file)
    _, danger_map = build_danger_ingredients(foods)

    print(danger_map)

    while True:
        for allergy, v in danger_map.items():
            if len(v) == 1:
                v_copy = v.copy()
                ingredient = v_copy.pop()
                # print(f"Remove {ingredient} from other allergy")
                for k2, v2 in danger_map.items():
                    if ingredient in v2 and k2 != allergy:
                        # print(f"Removing {ingredient} from {k2}")
                        v2.remove(ingredient)

                if all(len(v) == 1 for v in danger_map.values()):
                    danger_map = {k: v.pop() for k, v in danger_map.items()}
                    keys_sorted = sorted(danger_map)
                    result = ''
                    for k in keys_sorted:
                        print(k, danger_map[k])
                        result += danger_map[k] + ','
                    return result[:-1]

    return None


if __name__ == "__main__":
    print(part2("input.txt"))
