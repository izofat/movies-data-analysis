import pandas as pd
import ast
movies_df = pd.read_csv('./movies.csv')
actors_df = movies_df['stars'].apply(ast.literal_eval).explode()
print(actors_df.value_counts())
