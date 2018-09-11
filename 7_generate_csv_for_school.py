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

        self._pub_school_writer = csv.DictWriter(open(pub_school_csv_path, 'w'), fieldnames = ['pubKey', 'schoolName'], delimiter = '|')
        self._pub_school_writer.writeheader()


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

        if self._is_publication and name == 'school':
            self._pub_school_writer.writerow({'pubKey': self._key, 'schoolName': self._field_data})

        elif name in pub_types:
            self._is_publication = False

        else:
            pass


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

pub_school_df = pd.read_csv(pub_school_csv_path, sep = '|')
# pub_school_df.shape
# pub_school_df.head()

school_df = pd.read_csv(school_csv_path, sep = '|')
# school_df.shape

pub_school_df = pub_school_df.merge(school_df, on = 'schoolName', how = 'left')
# pub_school_df.shape
# pub_school_df['schoolId'].value_counts()
# pub_school_df.head()
pub_school_df[school_attributes].to_csv(pub_school_csv_path, index = False, sep = '|')
