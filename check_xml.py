# Import libraries
from xml.sax.handler import ContentHandler
import xml.sax
import datetime
import csv
import pandas as pd

# Configure paths
xml_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/dblp.xml'
# xml_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/dblp.000.xml'


pub_types = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', \
            'phdthesis', 'mastersthesis', 'www']
all_fields = ['title',  'author',  'year',  'month',  'journal',  'crossref', \
            'address', 'booktitle', 'cdrom', 'chapter', 'cite', 'editor', 'ee', \
            'i', 'isbn', 'note', 'number', 'pages', 'publisher', 'school', \
            'series', 'sub', 'sup', 'tt', 'url', 'volume', 'key', 'mdate']
attributes = ['key', 'mdate']

author_names = []
field_counts = {pub_type:{field: set([0]) for field in all_fields} for pub_type in pub_types}
field_max_length = {field: 0 for field in all_fields}


class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._pub_field_counts = {}
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

        if name in pub_types:
            self._pub_field_counts = {field: 0 for field in all_fields}
            if 'key' in attrs.getNames():
                self._pub_field_counts['key'] += 1
            elif 'mdate' in attrs.getNames():
                self._pub_field_counts['mdate'] += 1
        elif name in all_fields:
            self._pub_field_counts[name] += 1


    def endElement(self, name):

        self._field_data = self._getCharacterData()

        if name == 'author':
            author_names.append(self._field_data)
        if name in pub_types:
            for field in all_fields:
                field_counts[name][field].add(self._pub_field_counts[field])
        elif name in all_fields:
            field_max_length[name] = max(field_max_length[name], len(self._field_data))



print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

# field counts -----------------------------------------------------------------
print('='*50)
print('1. Field relation for each publication')
def map_count_to_relation(field_count_set):
    if field_count_set == set([0]):
        return '0'
    elif field_count_set == set([1]):
        return '1 and only 1'
    elif field_count_set == set([0, 1]):
        return '0 or 1'
    elif max(field_count_set) > 1:
        if 0 in field_count_set:
            return '0 or many'
        else:
            if 1 in field_count_set:
                return '1 or many'
            else:
                return 'many'

field_relations = {pub_type:{field: map_count_to_relation(field_counts[pub_type][field]) for field in field_counts[pub_type].keys() if field_counts[pub_type][field] != set([0])} for pub_type in pub_types}
field_relations_no_zero = {pub_type:{field: map_count_to_relation(field_counts[pub_type][field]) for field in field_counts[pub_type].keys() if field_counts[pub_type][field] != set([0])} for pub_type in pub_types}
for key, value in field_relations_no_zero.items():
    print('-'*50)
    print('Publication type: {}'.format(key))
    df = pd.DataFrame.from_dict(data = value, orient='index').reset_index()
    df.columns = ['Field', 'Relation']
    print(df)

# field maximum string length
print('='*50)
print('2. Maximum string length for each field')
df = pd.DataFrame.from_dict(data = field_max_length, orient='index').reset_index()
df.columns = ['Field', 'Max String Length']
print(df)


# author maximum string length
print('='*50)
print("3. Number of words in Authors' Name")
author_names_words = set([len(name.split(' ')) for name in author_names])
print('Possible Number of words: {}'.format(author_names_words))

author_names_words_max = max(author_names_words)
print('Author name with maximum number of words:')
print([name for name in author_names if len(name.split(' ')) == author_names_words_max])
