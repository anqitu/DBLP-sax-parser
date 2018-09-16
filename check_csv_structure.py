import random
import os
import glob
import json
import pandas as pd

# read from folders
def read_folder(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
           if file.endswith("sv"):
               all_files.append(os.path.join(root, file))
    return all_files


csv_file_paths = read_folder('./csv')
db_csv_file_paths = read_folder('./db_csv')


# for file_path in sorted(csv_file_paths):
#     if 'full' not in file_path:
#         print(os.path.basename(file_path))
#
#         df = pd.read_csv(file_path, sep = '|')
#         print('Shape: {}'.format(df.shape))
#         # print('Columns: {}'.format(list(df.columns)))
#         # print(df.info())
#         # print(df.head())
#         print('-' * 50)

# # create sample file
# full_paths = [path for path in csv_file_paths if 'full' in path]
# n = 10
# for path in full_paths:
#     df = pd.read_csv(path, sep = '|', skiprows=lambda i: i % n != 0)
#     df.to_csv(path.replace('/full', ''), sep = '|', index = False, line_terminator='\r\n')
#     print(path.replace('/full', ''))


# alias_df = pd.read_csv('./csv/alias.csv', sep = '|')
# www_df = pd.read_csv('./csv/www.csv', sep = '|')
# editorship_df = pd.read_csv('./csv/editorship.csv', sep = '|')
# inproceedings_df = pd.read_csv('./csv/inproceeding.csv', sep = '|')
article_df = pd.read_csv('./csv/article.csv', sep = '|')
# proceedings_df = pd.read_csv('./csv/proceeding.csv', sep = '|')
# authorship_df = pd.read_csv('./csv/authorship.csv', sep = '|')
# pubmonth_df = pd.read_csv('./csv/pubmonth.csv', sep = '|')
# incollection_df = pd.read_csv('./csv/incollection.csv', sep = '|')
# thesis_df = pd.read_csv('./csv/thesis.csv', sep = '|')
# pub_school_df = pd.read_csv('./csv/pub_school.csv', sep = '|')
publication_df = pd.read_csv('./csv/publication.csv', sep = '|')
# person_df = pd.read_csv('./csv/person.csv', sep = '|')
citership_df = pd.read_csv('./csv/citership.csv', sep = '|')
# book_df = pd.read_csv('./csv/book.csv', sep = '|')

publication_df.shape

article_df.shape
article_merge_df = article_df[~pd.isna(article_df['articleCrossref'])][['articleCrossref']].merge(publication_df[['pubKey']], left_on = 'articleCrossref', right_on = 'pubKey',how = 'left')
article_merge_df.shape
article_df.isnull().sum()
article_merge_df[article_merge_df['']]

citership_df = citership_df[citership_df['citedPubKey'] != '...']
citership_df = citership_df[citership_df['citedPubKey'] != '']
citership_df.shape
merge_df = citership_df.merge(publication_df[['pubKey']], left_on = 'citedPubKey', right_on = 'pubKey',how = 'left')
merge_df.shape
merge_df[pd.isna(merge_df['pubKey'])]

citership_df.isnull().sum()
