# Import libraries
from xml.sax.handler import ContentHandler
import xml.sax
import datetime
import csv
import pandas as pd
import numpy as np

# Configure data path
xml_path = './data/dblp.xml'

# Configure csv output path
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

pub_attributes = {'key': 'pubKey', 'title': 'pubTitle', 'year': 'pubYear', 'mdate': 'pubMdate', 'type': 'pubType', 'publisher': 'publisherName'}
pub_subclass_attributes_map = {
                    'article': {'key': 'pubKey', 'journal': 'articleJournal', 'booktitle': 'articleBooktitle', 'number': 'articleNumber', 'pages': 'articlePages', 'volume': 'articleVolume', 'crossref': 'articleCrossref'},
                    'inproceedings': {'key': 'pubKey', 'booktitle': 'inproBooktitle', 'number': 'inproNumber', 'pages': 'inproPages', 'crossref': 'inproCrossref'},
                    'incollection': {'key': 'pubKey', 'chapter': 'incolChapter', 'booktitle': 'incolBooktitle', 'number': 'incolNumber', 'pages': 'incolPages', 'crossref': 'incolCrossref'},
                    'proceedings': {'key': 'pubKey', 'address': 'proceedAddress', 'journal': 'proceedJournal', 'booktitle': 'proceedBooktitle', 'number': 'proceedNumber', 'pages': 'proceedPages', 'series': 'proceedSeries', 'volume': 'proceedVolume', 'type': 'proceedType'},
                    'book': {'key': 'pubKey', 'booktitle': 'bookBooktitle', 'pages': 'bookPages', 'series': 'bookSeries', 'volume': 'bookVolume'},
                    'thesis': {'key': 'pubKey', 'number': 'thesisNumber', 'pages': 'thesisPages', 'series': 'thesisSeries', 'volume': 'thesisVolume'},
                    'www': {'key': 'pubKey', 'booktitle': 'wwwBooktitle'},
                    }

month_attributes = ['pubKey', 'pubMonth']
pub_school_attributes = ['schoolName', 'pubKey']
alias_attributes = ['personFullName', 'personKey']
person_attributes = ['personKey', 'personFullName']
authorship_attributes = ['pubKey', 'personFullName']
editorship_attributes = ['pubKey', 'personFullName']
citership_attributes = ['citingPubKey', 'citedPubKey']

# tables to be created ---------------------------------------------------------

key = []
title = []
class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._field_data = None

        self._field_title = None

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
            key.append(attrs.getValue('key'))
            self._field_title = ''



    def endElement(self, name):
        self._field_data = self._getCharacterData()

        if name == 'title':
            self._field_title = self._field_data

        if name in pub_types:
            title.append(self._field_title)



print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))



df = pd.DataFrame(data = {'key': key, 'title': title})

df.head()
df.sort_values(['name']).head()
df.groupby('name')['number'].count()
int(0001)

[title_ for title_ in title if '||' in title]
[title_ for title_ in title if '|' in title]
