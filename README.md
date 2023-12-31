# Processing Ingredients

The assignment sanitizes and prepares the json file containing ingredients. This includes the following two tasks:
1. Normalising and standardising the units of ingredients to a certain set of standard units
2. Consolidating multiple JSON files containing ingredients, combining synonymous ingredients by making the required
in the quantity 

## How Tasks were Completed

### Task 1
- The units of ingredients were converted to the standard set of units by using the OpenAI Chat Completion API using 
gpt-3.5-turbo model.
- System prompt specifying the format of the output and user prompt specifying the task along with a JSON containing the
ingredients were given and the output was received in the required format.
- The JSON files with standardised units have been added to the Interim_jsons directory  

### Task 2
- The JSON files with the standardised units were consolidated. The synonymous ingredient names were then identified 
through a prompt to the Chat Completions API in the form of a dictionary containing the lists of synonymous ingredients.
- The synonymous ingredient names were then combined together following the given steps: 
1) ingredientName and ingredientID set to the common name of all component ingredients of a list of synonymous ingredients
2) Units changed to a common standard unit.
3) Quantities associated with the units changed using a Unit Conversion Matrix with all standard units expressed in 
terms of each other.
4) Notes for all component ingredients were added to the combined ingredient and a new key "Forms" added containing the
names of the compononent ingredients
- The final JSON of ingredients have been added to merged.json 

Set-up
1) Requirements: openai==0.28.0
2) OpenAI API key to be added in the utils.py before running the code

