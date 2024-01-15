from typing import List
import pandas as pd
import numpy as np

class MovieFilter:
    """A class for filtering and adding new columns to the dataframe"""

    def __init__(self) -> None:
        self.read_file_success_init = False
        try:
            self.movies_df: pd.DataFrame = pd.read_csv("./movies.csv")
            if not self.movies_df.empty:
                self.movie = pd.DataFrame()
                self.add_movies_total_points()
                self.bind_movies()
                self.read_file_success_init = True
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)
        except pd.errors.EmptyDataError as empty_data_error:
            print(empty_data_error)
        except pd.errors.ParserError as parser_error:
            print(parser_error)
        # except Exception as error:
        #     print(error)

    def add_movies_total_points(self) -> None:
        """It addes a new column 'total_points' to the dataframe
        by multiplying votes and rating column"""
        self.movies_df["total_points"] = (
            self.movies_df["votes"] * self.movies_df["rating"]
        )

    def bind_movies(self) -> None:
        """It checks the movies runtime and categorize it"""
        self.movies_df["runtime_category"] = pd.cut(
            self.movies_df["runtime"],
            bins=[0, 50, 100, 150, 500],
            labels=["episode", "short_movie", "normal_movie", "long_movie"],
        )

    def filter_movie(self, filter_condition: str) -> pd.DataFrame:
        """Filters the movie with the user input"""
        self.movie: pd.DataFrame = self.movies_df.loc[
            self.movies_df["title"] == filter_condition
        ]
        return self.movie


class LogMovie:
    """A class for printing the output to the terminal"""

    def __init__(self, movie: pd.DataFrame) -> None:
        self.movie: pd.DataFrame = movie
        self.get_columns()
        self.get_datas()

    def get_columns(self) -> None:
        """Gets columns from the dataframe"""
        self.movie_columns: List[str] = list(self.movie.columns)

    def get_datas(self) -> None:
        """Gets values from the dataframe"""
        self.movie_datas: np.ndarray = self.movie.values[0]

    def log_movie(self) -> None:
        """Logs the movie to the console"""
        print("------------")
        for column, data in zip(self.movie_columns, self.movie_datas):
            print(f"{column} : {data}")
        print("------------")


def main():
    """Runs the project"""
    if movie_filter.read_file_success_init:
        user_movie: str = input("Enter a movie name to search : ")
        movie_filtered: pd.DataFrame = movie_filter.filter_movie(user_movie)
        if not movie_filtered.empty:
            log_movie: LogMovie = LogMovie(movie_filtered)
            log_movie.log_movie()
        else:
            print("No movie found")
            main()
    else:
        print("No data found in the dataset")


movie_filter: MovieFilter = MovieFilter()
main()
