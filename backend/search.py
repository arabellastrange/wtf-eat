import pandas as pd 
## hidden dependencies for reading from HuggingFace Hub
import fsspec
import huggingface_hub

def search_recipes(ingredients: list) -> pd.DataFrame:
    #TODO: search for recipes based on ingredients
    #TODO: prep return for jsonify 
    print(f"Searching for recipes with ingredients: {ingredients}")
    print(f"Fetching dataframe from HuggingFace")
    df = pd.read_csv("hf://datasets/AkashPS11/recipes_data_food.com/recipes.csv")
    print(f"Filtering dataframe for empty ingredients")
    df = df.dropna(subset=['RecipeIngredientParts'])
    print(f"Number of recipes found: {len(df)}")
    return df.sample(n=3)