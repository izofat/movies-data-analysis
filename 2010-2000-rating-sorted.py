import pandas as pd

movies_df = pd.read_csv('./movies.csv')
movies_df = movies_df.dropna(how='any')
movies_df['year'] = movies_df['year'].str.extract(r'(\d+)').astype(float)
movies_df['year'] = pd.to_numeric(movies_df['year'])
seperated_movied_df = movies_df[(movies_df['year'] >= 2000) & (movies_df['year'] <=2010)]
print(seperated_movied_df.shape)
seperated_movies_sorted_df = seperated_movied_df.sort_values(by='rating' ,ascending=False)
print(seperated_movies_sorted_df.head(20))