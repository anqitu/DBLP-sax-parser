import random
import os
import glob
import json
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# read from folders
def read_folder(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
           if file.endswith("sv"):
               all_files.append(os.path.join(root, file))
    return all_files


csv_file_paths = read_folder('./csv')
csv_file_paths

pub_csv_path = './csv/publication.csv'
pub_subclass_csv_path = {
                        'article': './csv/article.csv',
                        'inproceedings': './csv/inproceeding.csv',
                        'incollection': './csv/incollection.csv',
                        'proceedings': './csv/proceeding.csv',
                        'book': './csv/book.csv',
                        'thesis': './csv/thesis.csv',
                        'www': './csv/www.csv',
                        }
month_csv_path = './csv/pubmonth.csv'
pub_school_csv_path = './csv/pub_school.csv'
alias_csv_path = './csv/alias.csv'
person_csv_path = './csv/person.csv'
authorship_csv_path = './csv/authorship.csv'
editorship_csv_path = './csv/editorship.csv'
citership_csv_path = './csv/citership.csv'

publication_df = pd.read_csv(pub_csv_path, sep = '|')

from sklearn.model_selection import train_test_split
publication_df_keep, publication_df_drop = train_test_split(publication_df, test_size=0.63, random_state=0, stratify = publication_df['pubType'])
publication_df['pubType'].value_counts().sum() / 4
publication_df_keep['pubType'].value_counts().sum()
publication_df_keep['pubType'].value_counts()

for df_path, crossref in {pub_subclass_csv_path['article']: 'articleCrossref',\
                        pub_subclass_csv_path['inproceedings']: 'inproCrossref',\
                        pub_subclass_csv_path['incollection']: 'incolCrossref'}.items():
    pub_df = pd.read_csv(df_path, sep = '|')
    pub_df = pub_df.merge(publication_df_keep[['pubKey']], on = 'pubKey')
    pub_df = pub_df[pub_df[crossref].isin(list(publication_df_keep['pubKey']) + ['\\N'])]
    pub_df.to_csv(df_path.replace('/csv/', '/csv_quarter/'), index = False, sep = '|', line_terminator='\r\n')
    print(df_path.replace('/csv/', '/csv_quarter/'))
    print(pub_df.shape)

for df_path in [pub_subclass_csv_path['proceedings'], pub_subclass_csv_path['book'], \
                pub_subclass_csv_path['thesis'], pub_subclass_csv_path['www'], \
                month_csv_path, pub_school_csv_path]:
    pub_df = pd.read_csv(df_path, sep = '|')
    pub_df = pub_df.merge(publication_df_keep[['pubKey']], on = 'pubKey')
    pub_df.to_csv(df_path.replace('/csv/', '/csv_quarter/'), index = False, sep = '|', line_terminator='\r\n')
    print(df_path.replace('/csv/', '/csv_quarter/'))
    print(pub_df.shape)

pubKey_keep = []
for pub_path in pub_subclass_csv_path.values():
    pub_df = pd.read_csv(pub_path.replace('/csv/', '/csv_quarter/'), sep = '|')
    pubKey_keep.append(pub_df[['pubKey']])

pubKey_keep = pd.concat(pubKey_keep)
pubKey_keep.shape
publication_df_keep.shape
publication_df_keep = publication_df_keep.merge(pubKey_keep)
publication_df_keep.to_csv(pub_csv_path.replace('/csv/', '/csv_quarter/'), index = False, sep = '|', line_terminator='\r\n')

citership_df = pd.read_csv(citership_csv_path, sep = '|')
citership_df_keep = citership_df_keep[citership_df_keep['citingPubKey'].isin(publication_df_keep['pubKey'])]
citership_df_keep = citership_df_keep[citership_df_keep['citedPubKey'].isin(publication_df_keep['pubKey'])]
citership_df_keep.shape
citership_df_keep.to_csv(citership_csv_path.replace('/csv/', '/csv_quarter/'), index = False, sep = '|', line_terminator='\r\n')


authorship_df = pd.read_csv(authorship_csv_path, sep = '|')
editorship_df = pd.read_csv(editorship_csv_path, sep = '|')
authorship_df = authorship_df[authorship_df['pubKey'].isin(publication_df_keep['pubKey'])]
authorship_df.to_csv(authorship_csv_path.replace('/csv/', '/csv_quarter/'), index = False, sep = '|', line_terminator='\r\n')
editorship_df = editorship_df[editorship_df['pubKey'].isin(publication_df_keep['pubKey'])]
editorship_df.to_csv(editorship_csv_path.replace('/csv/', '/csv_quarter/'), index = False, sep = '|', line_terminator='\r\n')

personship_df = pd.concat([authorship_df, editorship_df])
personship_df.shape
personship_df.head()
personship_df['pubKey'].value_counts().head()
personship_df[['personFullName']].drop_duplicates().shape

alias_df = pd.read_csv(alias_csv_path, sep = '|')
alias_df.shape
alias_df.head()
alias_df_keep = alias_df.merge(personship_df[['personFullName']].drop_duplicates(), on = 'personFullName')
alias_df_keep.shape
alias_df_keep.to_csv(alias_csv_path.replace('/csv/', '/csv_quarter/'), index = False, sep = '|', line_terminator='\r\n')


person_df = pd.read_csv(person_csv_path, sep = '|')
person_df.head()
person_df.shape
person_df_keep1 = person_df.merge(personship_df[['personFullName']].drop_duplicates(), on = 'personFullName')
person_df_keep1.shape

person_df_keep2 = person_df.merge(alias_df_keep[['personKey']], on = 'personKey')
person_df_keep2.shape

person_df_keep = pd.concat([person_df_keep1, person_df_keep2]).drop_duplicates()
person_df_keep.to_csv(person_csv_path.replace('/csv/', '/csv_quarter/'), index = False, sep = '|', line_terminator='\r\n')
