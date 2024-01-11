import csv
import pandas as pd
import time
with open('./movies-large.csv' , 'r' , encoding='utf-8') as file :
    start_time_csv = time.time()
    reader = csv.reader(file)
    csv_data = []
    for row in reader:
        csv_data.append(row)
    
    print(time.time() - start_time_csv)
    


start_time_pandas = time.time()
movies_df = pd.read_csv('./movies-large.csv')
pandas_data = []
for row in movies_df.values:
    pandas_data.append(row)
print(time.time() - start_time_pandas)

# pandas is fasterr