import os
import glob
import json
import pandas as pd

# read from folders
def read_folder(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
           if file.endswith(".csv"):
               all_files.append(os.path.join(root, file))
    return all_files

directory = './csv'

file_paths = read_folder(directory)

for file_path in file_paths:
    print(os.path.basename(file_path))

    df = pd.read_csv(file_path, sep = '|')
    print('Shape: {}'.format(df.shape))
    print('Columns: {}'.format(list(df.columns)))
    print('-' * 50)
