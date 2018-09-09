# Import libraries
from xml.sax.handler import ContentHandler
import xml.sax
import datetime
import csv
import pandas as pd

# Configure paths
# xml_path = './data/dblp.xml'
xml_path = './data/dblp_sample.xml'
pub_csv_path = './csv/publication.csv'
publisher_csv_path = './csv/publisher.csv'
school_csv_path = './csv/school.csv'
alias_csv_path = './csv/alias.csv'
person_csv_path = './csv/person.csv'

# table field and field names
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

class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._field_data = None

        self._publisher_fields = {}
        self._school_fields = {}
        self._pub_fields = {}

        self._publisher_writer = csv.DictWriter(open(publisher_csv_path, 'w'), fieldnames = publisher_attributes, delimiter='|')
        self._publisher_writer.writeheader()

        self._school_writer = csv.DictWriter(open(school_csv_path, 'w'), fieldnames = school_attributes, delimiter='|')
        self._alias_writer.writeheader()

        self._alias_writer = csv.DictWriter(open(alias_csv_path, 'w'), fieldnames = alias_attributes, delimiter='|')
        self._alias_writer.writeheader()

    def _getCharacterData(self):
        data = ''.join(self._charBuffer).strip()
        self._charBuffer = []
        return data.strip()

    def parse(self, f):
        xml.sax.parse(f, self)

    def characters(self, data):
        self._charBuffer.append(data)

    def startElement(self, name, attrs):
        if name in pub_types:
            self._pub_fields = {field: None for field in pub_field_names}
            self._pub_field['key'] = attrs.getValue('key')

    def endElement(self, name):
        self._field_data = self._getCharacterData()
        if name in pub_field_names:
            self._pub_field[name] = self._field_data
        elif name in pub_types:
            self._pub_writer.writerow(self._pub_field)
        if name == 'author':
            author_names.append(self._field_data)

print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))


# attributes
len(attributes)
attr = attributes[0]
attr.getValue('key')
attr.getNames()
attr.getType('key')
attr.getLength()
set(pub_structure)
