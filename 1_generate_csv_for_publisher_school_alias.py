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

# tables to be created ---------------------------------------------------------
publishers = []
schools = []
aliases = []

class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._field_data = None
        self._field_data = None

    def _getCharacterData(self):
        data = ''.join(self._charBuffer).strip()
        self._charBuffer = []
        return data.strip()

    def parse(self, f):
        xml.sax.parse(f, self)

    def characters(self, data):
        self._charBuffer.append(data)

    def startElement(self, name, attrs):
        pass

    def endElement(self, name):
        self._field_data = self._getCharacterData()

        if name == 'publisher':
            publishers.append(self._field_data)
        if name == 'school':
            schools.append(self._field_data)
        if name in ['author', 'editor']:
            aliases.append(self._field_data)

print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

# add generated ID and write to csv --------------------------------------------
publishers = list(set(publishers))
schools = list(set(schools))
aliases = list(set(aliases))

print('Length of publishers: {}'.format(len(publishers)))
print('Length of schools: {}'.format(len(schools)))
print('Length of aliases: {}'.format(len(aliases)))

# 2018-09-10 06:36:56.956671: Start parsing
# 2018-09-10 06:39:35.445560: End parsing
# Length of publishers: 1995
# Length of schools: 1641
# Length of aliases: 2194488


publishers_df = pd.DataFrame(data = {'publisherId': range(1, len(publishers) + 1), 'publisherName': publishers})
publishers_df.to_csv(publisher_csv_path, index = False, sep = '|')

schools_df = pd.DataFrame(data = {'schoolId': range(1, len(schools) + 1), 'schoolName': schools})
schools_df.to_csv(school_csv_path, index = False, sep = '|')


alias_df = pd.DataFrame(data = {'aliasId': range(1, len(aliases) + 1), 'aliasFullName': aliases})
alias_df.to_csv(alias_csv_path, index = False, sep = '|')
