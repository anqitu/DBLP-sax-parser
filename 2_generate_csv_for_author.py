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


person_keys = []
person_aliases = []
person_primary_aliases = []

class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._field_data = None

        self._is_www_homepages = False
        self._person_key = None
        self._person_alias = None
        self._pub_count = 0

    def _getCharacterData(self):
        data = ''.join(self._charBuffer).strip()
        self._charBuffer = []
        return data.strip()

    def parse(self, f):
        xml.sax.parse(f, self)

    def characters(self, data):
        self._charBuffer.append(data)

    def startElement(self, name, attrs):
        if name == 'www' and ('homepages' in attrs.getValue('key') or 'persons' in attrs.getValue('key')):
            self._is_www_homepages = True

            self._person_key = attrs.getValue('key')
            self._person_alias = []

            self._pub_count += 1
            if self._pub_count % 100000 == 0:
                print('Current count: {}'.format(self._pub_count))

    def endElement(self, name):

        self._field_data = self._getCharacterData()

        if name == 'www':
            for person_alias in self._person_alias:
                person_keys.append(self._person_key)
                person_aliases.append(person_alias)
                person_primary_aliases.append(self._person_alias[0])

            self._is_www_homepages = False

        elif self._is_www_homepages and name == 'author':
            self._person_alias.append(self._field_data)


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

print(len(person_keys))
print(len(person_aliases))
print(len(person_primary_aliases))


persons_df_full = pd.DataFrame(data = {'personKey': person_keys, 'aliasFullName': person_aliases, 'person_primary_alias': person_primary_aliases}).drop_duplicates(subset = ['aliasFullName'])
print(persons_df_full.shape)
# persons_df_full.head()

persons_df_primary = persons_df_full[['personKey', 'person_primary_alias']].drop_duplicates()
persons_df_primary['personId'] = range(1, persons_df_primary.shape[0] + 1)
print(persons_df_primary.shape)
# persons_df_primary.head()

alias_df = pd.read_csv('./csv/alias.csv', sep = '|')
persons_df = persons_df_primary.merge(alias_df[['aliasFullName', 'aliasId']], left_on = 'person_primary_alias', right_on = 'aliasFullName', how = 'left')
persons_df = persons_df[['personId', 'personKey', 'aliasId']].rename(columns = {'aliasId': 'primaryAliasId'})
print(persons_df.shape)
# persons_df.head()
persons_df.to_csv(person_csv_path, index = False, sep = '|')

alias_df = alias_df.merge(persons_df_full, on = 'aliasFullName', how = 'left')
alias_df = alias_df.merge(persons_df_primary, on = 'person_primary_alias', how = 'left')
alias_df = alias_df[['aliasFullName', 'aliasId', 'personId']]
print(alias_df.shape)
# alias_df.head()
# alias_df.isnull().sum()
alias_df.to_csv(alias_csv_path, index = False, sep = '|')

# @NOTE Though we only loop through authors, all alises has got their personId. This means all editors has been authors for some publications. In this case, there is no need to parse the xml for editors.
