import json

from Constants import inp_jsons, unit_convert_prompt, sys_prompt_1
from utils import get_completion, combine_file

# For Converting the units to the standard units - "oz", "tsp", "tbsp", "cup", "clove", "pieces"
for i in range(len(inp_jsons)):
    user_prompt = unit_convert_prompt + f"``` {inp_jsons[i]} ```"
    out_json_string = get_completion(sys_prompt_1, user_prompt)

    try:
        out_json = json.loads(out_json_string)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

    else:
        with open(rf"C:\Users\MAHE\PycharmProjects\AddIngredients\Interim_jsons\interim_{i+1}.json", "w") as file_out:
            json.dump(out_json, file_out)
        print(f"JSON data saved to interim_{i+1}.json")


# For consolidatig the json files containing ingredients & combining the synonymous ingredients mentioned multiple times
file_prefix = r"C:\Users\MAHE\PycharmProjects\AddIngredients\Interim_jsons\interim_"
file_paths = [file_prefix + f"{i+1}.json" for i in range(2)]

merged_ingredients = combine_file(file_paths)

try:
    out_json = json.loads(json.dumps(merged_ingredients))

except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")

else:
    with open(rf"C:\Users\MAHE\PycharmProjects\AddIngredients\merged.json", "w") as file_out:
        json.dump(out_json, file_out)
    print(f"JSON data saved to merged.json")





