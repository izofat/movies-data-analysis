import pandas as pd

movies_df = pd.read_csv("./movies.csv")
actors_movies_df = movies_df[
    (movies_df["stars"].str.contains("Kemal Sunal")) |
    (movies_df["stars"].str.contains("Leonardo DiCaprio")) |
    (movies_df["stars"].str.contains('Al Pacino'))
]

actors_movies_sorted_df = actors_movies_df.sort_values(by='rating')
print(actors_movies_df.head(8))