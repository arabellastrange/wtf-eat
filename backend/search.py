import pandas as pd 
## hidden dependencies for reading from HuggingFace Hub
import fsspec
import huggingface_hub
import os.path as path

recipe_df = pd.DataFrame()

def set_dataframe(): 
    global recipe_df
    if(path.exists("./data/recipes.csv")):
        print(f"Fetching dataframe from local file")
        recipe_df = pd.read_csv("./data/recipes.csv", low_memory=False)
    else:
        print(f"Fetching dataframe from HuggingFace")
        recipe_df = pd.read_csv("hf://datasets/AkashPS11/recipes_data_food.com/recipes.csv", low_memory=False)
        recipe_df.to_csv("./data/recipes.csv", index=False)
        print(f"Saved dataframe to local file")
    
    print(f"Filtering dataframe for empty ingredients")
    recipe_df = recipe_df.dropna(subset=['RecipeIngredientParts'])
    recipe_df = recipe_df[['AuthorName', 'TotalTime', 'Keywords', 'Name',
                            'RecipeIngredientParts', 'RecipeIngredientQuantities', 
                            'RecipeInstructions']]
    print(f"Number of recipes found: {len(recipe_df)}")


def search_recipes(ingredients: list) -> pd.DataFrame:
    #TODO: prep return for jsonify 
    print(f"Searching for recipes with ingredients: {ingredients}")
    matching_recipes = recipe_df[recipe_df['RecipeIngredientParts'].str
                                 .contains('|'.join(ingredients), case=False)]
    print(f"Number of matching recipes found: {len(matching_recipes)}")
    if len(matching_recipes) == 0:
        return pd.DataFrame()
    else: 
        if len(matching_recipes) < 3:
            return matching_recipes
        else:
            return matching_recipes.sample(n=3)