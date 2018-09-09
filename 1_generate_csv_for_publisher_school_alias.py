# Import libraries -------------------------------------------------------------
from xml.sax.handler import ContentHandler
import xml.sax
import datetime
import csv
import pandas as pd

# Configure paths --------------------------------------------------------------
xml_path = './data/dblp.xml'
# xml_path = './data/dblp_sample.xml'
pub_csv_path = './csv/publication.csv'
publisher_csv_path = './csv/publisher.csv'
school_csv_path = './csv/school.csv'
alias_csv_path = './csv/alias.csv'
person_csv_path = './csv/person.csv'

# table field and field names --------------------------------------------------
pub_types = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www']

pub_attributes = ['pubKey', 'pubTitle', 'pubYear', 'pubMonth', 'pubMdate', 'pubType', 'publisherId']
pub_attributes_map = {
                    'article': ['pubKey', 'journal', 'booktitle', 'number', 'pages', 'volume', 'crossref'],
                    'inproceedings': ['pubKey', 'boottitle', 'number', 'pages', 'crossref'],
                    'incollection': ['pubKey', 'chapter', 'booktitle', 'number', 'pages', 'crossref'],
                    'proceedings': ['pubKey', 'address', 'journal', 'booktitle', 'number', 'pages', 'series', 'volume'],
                    'book': ['pubKey', 'booktitle', 'pages', 'series', 'volume'],
                    'phdthesis': ['pubKey', 'number', 'pages', 'series', 'volume'],
                    'mastersthesis': ['pubKey', 'schoolId'],
                    'www': ['pubKey', 'booktitle'],
                    }

publisher_attributes = ['publisherId', 'publisherName']

school_attributes = ['schoolId', 'schoolName']
pub_school_attributes = ['schoolId', 'pubKey']

alias_attributes = ['aliasId', 'aliasFirstName', 'aliasLastName', 'personId']
person_attributes = ['personID', 'personKey', 'primaryAliasId']
authorship_attributes = ['pubKey', 'personID']
editor_attributes = ['pubKey', 'personID']

citership_attributes = ['citingPubKey', 'citedPubKey']

# tables to be created ---------------------------------------------------------
publishers = []
schools = []
alias = []

class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
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
            alias.append(self._field_data)

print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

# add generated ID and write to csv --------------------------------------------
publishers = set(publishers)
schools = set(schools)
alias = set(alias)

print('Length of publishers: {}'.format(len(publishers)))
print('Length of schools: {}'.format(len(schools)))
print('Length of alias: {}'.format(len(alias)))

publishers = pd.DataFrame(data = {'publisherId': range(1, len(publishers) + 1), 'publisherName': publishers})
publishers.to_csv(publisher_csv_path, index = False, sep = '|')

schools = pd.DataFrame(data = {'schoolId': range(1, len(schools) + 1), 'schoolName': schools})
schools.to_csv(school_csv_path, index = False, sep = '|')

alias = pd.DataFrame(data = {'aliasId': range(1, len(alias) + 1), \
                            'aliasFirstName': [''.join(name.split(' ')[:-1]) if len(name.split(' ')) != 1 else name for name in alias], \
                            'aliasLastName': [''.join(name.split(' ')[-1]) if len(name.split(' ')) != 1 else None for name in alias]})
alias.to_csv(alias_csv_path, index = False, sep = '|')
