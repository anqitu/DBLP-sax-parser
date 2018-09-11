# Import libraries
from xml.sax.handler import ContentHandler
import xml.sax
import datetime
import csv
import pandas as pd
import numpy as np

# Configure paths
xml_path = './data/dblp.xml'
# xml_path = './data/dblp_sample.xml'
pub_csv_path = './csv/publication.csv'

pub_subclass_csv_path = {
                        'article': './csv/article.csv',
                        'inproceedings': './csv/inproceedings.csv',
                        'incollection': './csv/incollection.csv',
                        'proceedings': './csv/proceedings.csv',
                        'book': './csv/book.csv',
                        'thesis': './csv/thesis.csv',
                        'www': './csv/www.csv',
                        }

month_csv_path = './csv/month.csv'
publisher_csv_path = './csv/publisher.csv'
school_csv_path = './csv/school.csv'
pub_school_csv_path = './csv/pub_school.csv'
alias_csv_path = './csv/alias.csv'
person_csv_path = './csv/person.csv'
authorship_csv_path = './csv/authorship.csv'
editorship_csv_path = './csv/editorship.csv'
citership_csv_path = './csv/citership.csv'

# table field and field names
pub_types = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www']

pub_attributes = {'key': 'pubKey', 'title': 'pubTitle', 'year': 'pubYear', 'mdate': 'pubMdate', 'type': 'pubType', 'publisher': 'publisherId'}
pub_subclass_attributes_map = {
                    'article': {'key': 'pubKey', 'journal': 'articleJournal', 'booktitle': 'articleBooktitle', 'number': 'articleNumber', 'pages': 'articlePages', 'volume': 'articleVolume', 'crossref': 'articleCrossref'},
                    'inproceedings': {'key': 'pubKey', 'booktitle': 'inproBooktitle', 'number': 'inproNumber', 'pages': 'inproPages', 'crossref': 'inproCrossref'},
                    'incollection': {'key': 'pubKey', 'chapter': 'incolChapter', 'booktitle': 'incolBooktitle', 'number': 'incolNumber', 'pages': 'incolPages', 'crossref': 'incolCrossref'},
                    'proceedings': {'key': 'pubKey', 'address': 'proceedAddress', 'journal': 'proceedJournal', 'booktitle': 'proceedBooktitle', 'number': 'proceedNumber', 'pages': 'proceedPages', 'series': 'proceedSeries', 'volume': 'proceedVolume', 'type': 'proceedType'},
                    'book': {'key': 'pubKey', 'booktitle': 'bookBooktitle', 'pages': 'bookPages', 'series': 'bookSeries', 'volume': 'bookVolume'},
                    'thesis': {'key': 'pubKey', 'number': 'thesisNumber', 'pages': 'thesisPages', 'series': 'thesisSeries', 'volume': 'thesisVolume'},
                    'www': {'key': 'pubKey', 'booktitle': 'wwwBooktitle'},
                    }

month_attributes = ['pubKey', 'month']
publisher_attributes = ['publisherId', 'publisherName']
school_attributes = ['schoolId', 'schoolName']
pub_school_attributes = ['schoolId', 'pubKey']
alias_attributes = ['aliasId', 'aliasFirstName', 'aliasLastName', 'personId']
person_attributes = ['personId', 'personKey', 'primaryAliasId']
authorship_attributes = ['pubKey', 'personId']
editorship_attributes = ['pubKey', 'personId']
citership_attributes = ['citingPubKey', 'citedPubKey']


class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._field_data = None
        self._pub_fields = None
        self._pub_subclass_fields = None
        self._current_pub_type = None
        self._is_publication = False
        self._pub_count = 0

        self._pub_subclass_writers = {
                            'article': csv.DictWriter(open(pub_subclass_csv_path['article'], 'w'), fieldnames = pub_subclass_attributes_map['article'].values(), delimiter = '|'),
                            'inproceedings': csv.DictWriter(open(pub_subclass_csv_path['inproceedings'], 'w'), fieldnames = pub_subclass_attributes_map['inproceedings'].values(), delimiter = '|'),
                            'incollection': csv.DictWriter(open(pub_subclass_csv_path['incollection'], 'w'), fieldnames = pub_subclass_attributes_map['incollection'].values(), delimiter = '|'),
                            'proceedings': csv.DictWriter(open(pub_subclass_csv_path['proceedings'], 'w'), fieldnames = pub_subclass_attributes_map['proceedings'].values(), delimiter = '|'),
                            'book': csv.DictWriter(open(pub_subclass_csv_path['book'], 'w'), fieldnames = pub_subclass_attributes_map['book'].values(), delimiter = '|'),
                            'thesis': csv.DictWriter(open(pub_subclass_csv_path['thesis'], 'w'), fieldnames = pub_subclass_attributes_map['thesis'].values(), delimiter = '|'),
                            'www': csv.DictWriter(open(pub_subclass_csv_path['www'], 'w'), fieldnames = pub_subclass_attributes_map['www'].values(), delimiter = '|'),
                            }
        for subclass_writer in self._pub_subclass_writers.values():
            subclass_writer.writeheader()

        self._pub_writer = csv.DictWriter(open(pub_csv_path, 'w'), fieldnames = pub_attributes.values(), delimiter = '|')
        self._pub_writer.writeheader()


    def _getCharacterData(self):
        data = ''.join(self._charBuffer).strip()
        self._charBuffer = []
        return data.strip()

    def parse(self, f):
        xml.sax.parse(f, self)

    def characters(self, data):
        self._charBuffer.append(data)

    def startElement(self, name, attrs):


        if name in pub_types and not (name == 'www' and ('homepages' in attrs.getValue('key') or 'persons' in attrs.getValue('key'))):

            self._is_publication = True
            self._current_pub_type = 'thesis' if name in ['mastersthesis', 'phdthesis'] else name

            key = attrs.getValue('key')
            mdate = attrs.getValue('mdate')

            self._pub_fields = {attribute: None for attribute in pub_attributes.keys()}
            self._pub_fields['key'] = key
            self._pub_fields['mdate'] = mdate
            self._pub_fields['type'] = name

            self._pub_subclass_fields = {attribute: None for attribute in pub_subclass_attributes_map[self._current_pub_type].keys()}
            self._pub_subclass_fields['key'] = key

            if self._current_pub_type == 'proceedings':
                self._pub_subclass_fields['type'] = key.split('/')[0]


            self._pub_count += 1
            if self._pub_count % 100000 == 0:
                print('Current count: {}'.format(self._pub_count))

    def endElement(self, name):

        self._field_data = self._getCharacterData()

        if self._is_publication:

            if name in pub_attributes.keys():

                # Only reserve the first appeared publisher as it is assumed that each publication can only have one publisher
                if name == 'publisher' and self._pub_fields['publisher'] != None:
                    self._pub_fields['publisher'] = self._field_data

                else:
                    self._pub_fields[name] = self._field_data

            elif name in pub_subclass_attributes_map[self._current_pub_type].keys():

                # combine several pages into one string seperate by ','
                if name == 'pages':
                    if self._pub_subclass_fields['pages'] != None:
                        self._pub_subclass_fields['pages'] = self._pub_subclass_fields['pages'] + ', ' + self._field_data
                    else:
                        self._pub_subclass_fields['pages'] = self._field_data

                # Only keep those longer version for publications with more than 1 series or colume
                elif name in ['series', 'volume']:
                    if self._pub_subclass_fields[name] != None:
                        self._pub_subclass_fields[name] = self._pub_subclass_fields[name] if len(self._pub_subclass_fields[name]) > len(self._field_data) else self._field_data
                    else:
                        self._pub_subclass_fields[name] = self._field_data

                else:
                    self._pub_subclass_fields[name] = self._field_data

            elif name in pub_types:

                self._pub_fields = {pub_attributes[key]: value for key, value in self._pub_fields.items()}
                self._pub_subclass_fields = {pub_subclass_attributes_map[self._current_pub_type][key]: value for key, value in self._pub_subclass_fields.items()}

                self._pub_writer.writerow(self._pub_fields)
                self._pub_subclass_writers[self._current_pub_type].writerow(self._pub_subclass_fields)

                self._is_publication = False

            else:
                pass


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

# map the publisherName to publisherId in publication.csv
pub_df = pd.read_csv(pub_csv_path, sep = '|')
publishers_df = pd.read_csv(publisher_csv_path, sep = '|')

publishers_map = {row['publisherName']: row['publisherId'] for index, row in publishers_df.iterrows()}
publishers_map[np.nan] = np.nan
pub_df['publisherId'] = pub_df['publisherId'].map(publishers_map)
pub_df.to_csv(pub_csv_path, sep = '|', index = False)

# pub_df.shape
# pub_df.isnull().sum()
# pub_df.head()
# pub_df.info()
# pub_df[pd.isna(pub_df['pubTitle'])]

# article_df = pd.read_csv('./csv/article.csv', sep = '|')
# book_df = pd.read_csv('./csv/book.csv', sep = '|')
# incollection_df = pd.read_csv('./csv/incollection.csv', sep = '|')
# inproceedings_df = pd.read_csv('./csv/inproceedings.csv', sep = '|')
# proceedings_df = pd.read_csv('./csv/proceedings.csv', sep = '|')
# thesis_df = pd.read_csv('./csv/thesis.csv', sep = '|')
# www_df = pd.read_csv('./csv/www.csv', sep = '|')
#
# row = 0
# for df in [article_df, book_df, incollection_df, inproceedings_df, proceedings_df, thesis_df, www_df]:
#     row += df.shape[0]
#     print(df.shape)
#     print(df.isnull().sum())
#     print(df.head())
#
# print(row)

# proceedings_df.head()
