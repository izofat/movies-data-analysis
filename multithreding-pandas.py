from typing import List, Union
import pandas as pd
import threading
from concurrent.futures import ThreadPoolExecutor 
from concurrent.futures._base import Future
user_movie = input('write your movie name :')

def read_csv_file_find_movie(file_path : str , movie_name : str) -> Union[pd.DataFrame , str]:
    movies_df : pd.DataFrame= pd.read_csv(file_path)

    movie : pd.DataFrame= movies_df[movies_df['title'] == movie_name]
    if len(movie) > 0:
        return movie
    else:
        return 'not found'
file_paths : List[str]= ['moviesmulti0.csv' , 'moviesmulti1.csv' ,'moviesmulti2.csv']

read_csv_file_find_movie(file_paths[0] , user_movie)
futures : List[Future]= []
with ThreadPoolExecutor(max_workers= 3) as executor:
    for file_path in file_paths:
        result : Future= executor.submit(read_csv_file_find_movie , file_path , user_movie)
        futures.append(result)

for future in futures:
    result : Union[str , pd.DataFrame]= future.result()
    if isinstance(result , pd.DataFrame):
        print(result)
    
