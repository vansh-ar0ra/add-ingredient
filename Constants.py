
with open(r"C:\Users\MAHE\PycharmProjects\AddIngredients\ingredients\ingredients.json") as f:
    text = f.read()

inp_jsons = [text[:2318], text[2318:4338], text[4338:6340], text[6340:8375], text[8375:]]

# User Prompt for Unit Conversion
unit_convert_prompt = """ Get an ordered list of units of ingredient from the json delimited by triple back ticks. 

   Convert the quantities of all the ingredients to any of the following units: "oz","tbsp","tsp","pieces","cloves",
   "cups" expressing the quantities of each ingredient in only these terms. 

   Plug these values for units and quantities back to the original json with units exactly matching the ones given in quotation marks : "oz","tbsp",
   "tsp","pieces","cloves","cups".

    """
# System Prompt for Unit Conversion
sys_prompt_1 = """Return the output in a single json in the format: [{"ingredientName":<name>, "ingredientID":<id>, 
"quantity": <quantity>, "unit": <unit>, "notes": <notes>, "optional": <optional>}]"""

# User Prompt for extracting synonymous ingredient names
synonym_prompt = """Extract the ingredient names from the data delimited by three back ticks.

Find the ingredient names which are synonymous or interchangeable in a recipe and group those ingredients together.

Return the output as a dictionary with keys as the parent products of the groups and values as lists of ingredients in each group.
Include only the elements which are in a group in the dictionary.
"""

# System Prompt for extracting synonymous ingredient names
sys_prompt_2 = """Return the output as a dictionary in the format: {<parent_product>: [<component_ingredients>]}"""


## Conversion rates of the units where row i and column j represent conversion rate from unit i ot unit j
#                       oz   tsp   tbsp   cup   clove
unit_convert_matrix = \
                       [[1,    6,     2,   1/8,   1/2],   # oz
                       [1/6,  1,   1/3,  1/48,  1/12],    # tsp
                       [1/2,  3,     1,  1/16,   1/4],    # tbsp
                       [8,   48,    16,     1,     4],    # cup
                       [2,   12,     4,   1/4,     1]]    # clove
