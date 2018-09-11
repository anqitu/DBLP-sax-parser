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
        self._key = None
        self._is_publication = False

        self._pub_count = 0

        self._authorship_writer = csv.DictWriter(open(authorship_csv_path, 'w'), fieldnames = ['pubKey', 'aliasFullName'], delimiter = '|')
        self._authorship_writer.writeheader()

        self._editorship_writer = csv.DictWriter(open(editorship_csv_path, 'w'), fieldnames = ['pubKey', 'aliasFullName'], delimiter = '|')
        self._editorship_writer.writeheader()

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
            self._key = attrs.getValue('key')

            self._pub_count += 1
            if self._pub_count % 100000 == 0:
                print('Current count: {}'.format(self._pub_count))

    def endElement(self, name):

        self._field_data = self._getCharacterData()

        if self._is_publication and name == 'author':
            self._authorship_writer.writerow({'pubKey': self._key, 'aliasFullName': self._field_data})

        elif self._is_publication and name == 'editor':
            self._editorship_writer.writerow({'pubKey': self._key, 'aliasFullName': self._field_data})

        elif name in pub_types:
            self._is_publication = False

        else:
            pass


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

authorship_df = pd.read_csv(authorship_csv_path, sep = '|')
# authorship_df.shape
# authorship_df.head()
# authorship_df.isnull().sum()
# authorship_df['pubKey'].value_counts().head(10)
# authorship_df['aliasFullName'].value_counts().head(10)

editorship_df = pd.read_csv(editorship_csv_path, sep = '|')
# editorship_df.shape
# editorship_df.head()
# editorship_df.isnull().sum()
# editorship_df['pubKey'].value_counts().head(10)
# editorship_df['aliasFullName'].value_counts().head(10)


persons_df = pd.read_csv(person_csv_path, sep = '|')
# persons_df.head()

alias_df = pd.read_csv(alias_csv_path, sep = '|')
# alias_df.head()

authorship_df = authorship_df.merge(alias_df, on = 'aliasFullName', how = 'left')
# authorship_df.shape
# authorship_df.head()
# authorship_df['aliasFullName'].value_counts()
# authorship_df['personId'].value_counts()
authorship_df[authorship_attributes].to_csv(authorship_csv_path, index = False, sep = '|')

editorship_df = editorship_df.merge(alias_df, on = 'aliasFullName', how = 'left')
# editorship_df.shape
# editorship_df.head()
# editorship_df['aliasFullName'].value_counts()
# editorship_df['personId'].value_counts()
editorship_df[editorship_attributes].to_csv(editorship_csv_path, index = False, sep = '|')


alias_df['aliasFirstName']= [' '.join(name.split(' ')[:-1]) if len(name.split(' ')) != 1 else name for name in alias_df['aliasFullName']]
alias_df['aliasLastName']= [name.split(' ')[-1] if len(name.split(' ')) != 1 else '' for name in alias_df['aliasFullName']]
alias_df = alias_df[alias_attributes]
alias_df.to_csv(alias_csv_path, index = False, sep = '|')

# alias_df.shape
# alias_df[alias_df['aliasFullName'].duplicated()]
# alias_df[alias_df[['aliasFirstName', 'aliasLastName']].duplicated()]
