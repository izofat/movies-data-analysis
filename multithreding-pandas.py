import pandas as pd
from concurrent.futures import ProcessPoolExecutor , as_completed
import psutil
import time
from multiprocessing import Manager
 
def check_data(chunk , user_input , start_time , stop_flag):
    if stop_flag.value:
        return None
    movie : pd.DataFrame= chunk[chunk['title'] == user_input]
    if not movie.empty:
        stop_flag.value  = 1
        print(time.time() - start_time)
        return movie
    

def determine_chunk_size(file_path , target_memory_percentage):
    total_memory_mb = psutil.virtual_memory().total / 1024**2
    max_chunk_size_percentage = 60/100
    avg_rows = pd.read_csv(file_path , nrows=100)
    avg_rows_size = avg_rows.memory_usage(deep=True).mean() / 1024**2
    initial_chunk_size = int((target_memory_percentage / 100) * (total_memory_mb /avg_rows_size))
    max_chunk_size = int(total_memory_mb * max_chunk_size_percentage)
    ast_chunk_size = min(max_chunk_size , initial_chunk_size)
    print(ast_chunk_size)
    return ast_chunk_size

file_path = './movies-large.csv'
def read_file(user_input):
    manager = Manager()
    stop_flag = manager.Value('i' ,0)
    chunk_size =  determine_chunk_size(file_path=file_path , target_memory_percentage=50)
    df = pd.read_csv(file_path , chunksize=chunk_size)
    start_time = time.time()
    futures = []
    with ProcessPoolExecutor() as executor:
        for chunk in df:
            result =  executor.submit(check_data , chunk , user_input , start_time , stop_flag)
            futures.append(result)

        for future in futures:
            result = future.result()
            if isinstance(result , pd.DataFrame):
                print(result)
                break
  
if __name__ == '__main__':
    user_input = input('write a movie name :')
    read_file(user_input)
