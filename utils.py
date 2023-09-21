import openai
import json

from Constants import synonym_prompt, sys_prompt_2, unit_convert_matrix

# Add openai api key here before running
openai.api_key = 'sk-'


def get_completion(system_prompt, user_prompt, model="gpt-3.5-turbo"):
    """
    Takes the prompt for both system and user roles and returns the completion by the GPT model
    """
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


def combine_file(file_paths):
    """
    Takes the JSON files containing the ingredients, gets a dictionary of synonymous ingredients through GPT Completion,
    and combines the synonymous ingredients together.

    :param file_paths: JSON files path containing the ingredients
    :return: Consolidated list of all the ingredients after combining synonymous ingredients
    """
    merged_ingredients = []
    for file_path in file_paths:
        with open(file_path, 'r') as file_in:
            merged_ingredients.extend(json.load(file_in))

    # user_prompt = " ".join([synonym_prompt, "```", str(merged_ingredients), "```"])
    # synonym_dict = get_completion(sys_prompt_2, user_prompt)
    synonym_dict = {"Garlic": ["Garlic Powder", "Fresh Garlic", "garlic cloves"], "Tomatotes":["Stewed Tomatoes", "Roasted Tomatoes"],
                    "Kosher Salt": ["kosher salt"]}  # Added for Testing, to be replaced by the synonyms returned by ChatGPT

    for key, value in synonym_dict.items():
        new_ingredient = {"ingredientName": key, "ingredientID": "_".join(key.split()), "quantity": 0, "notes": "", "forms": []}
        for ingredient_name in value:
            for i, ingredient in enumerate(merged_ingredients):
                if ingredient_name.lower() == ingredient["ingredientName"].lower():
                    new_ingredient = combine_ingredients(new_ingredient, ingredient)
                    merged_ingredients.pop(i)

        merged_ingredients.append(new_ingredient)

    return merged_ingredients


def combine_ingredients(ingredient_1, ingredient_2):
    """
    Takes two ingredients and combines them by adding a common ingredientName, ingredientID, changing the unit of the
    first ingredient to that of the second ingredient, adding the quantities, joining the notes and adding "forms" key
    containing the different ingredients combined
    """
    index_1 = unit_to_index(ingredient_1.get("unit", ingredient_2["unit"]))
    index_2 = unit_to_index(ingredient_2["unit"])
    ingredient_1["unit"] = ingredient_2["unit"]
    try:
        ingredient_1["quantity"] = float(ingredient_1["quantity"]) * unit_convert_matrix[index_1][index_2] + float(ingredient_2["quantity"])
    except:
        pass
    ingredient_1["notes"] = " ;".join([ingredient_1["notes"], ingredient_2.get("notes","")])
    ingredient_1["forms"].append(ingredient_2["ingredientID"])

    return ingredient_1


def unit_to_index(unit):
    """
    Changes the unit to an index number
    """
    if unit.lower() in ["cup", "cups"]:
        unit = "cups"
    elif unit.lower() in ["clove", "cloves"]:
        unit = "cloves"

    unit_index_map = {"oz": 0, "tsp": 1, "tbsp": 2, "cups": 3, "cloves": 4}

    return unit_index_map.get(unit.lower(), "")
