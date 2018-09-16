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
            'series', 'sub', 'sup', 'tt', 'url', 'volume']
all_attributes = ['key', 'mdate', 'publtype', 'cdate']

attributes = []
author_names = []
field_counts = {pub_type:{field: set([]) for field in all_fields} for pub_type in pub_types}
attribute_counts = {pub_type:{attribute: set([]) for attribute in all_attributes} for pub_type in pub_types}
string_max_length = {field: 0 for field in (all_fields + all_attributes)}


class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._pub_field_counts = {}
        self._attribute_counts = {}
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
            self._pub_attribute_counts = {attribute: 0 for attribute in all_attributes}

            attributes.append(attrs)

            for attribute in all_attributes:
                if attribute in attrs.getNames():
                    self._pub_attribute_counts[attribute] = 1
                    string_max_length[attribute] = max(string_max_length[attribute], len(attrs.getValue(attribute)))

        elif name in all_fields:
            self._pub_field_counts[name] += 1


    def endElement(self, name):

        self._field_data = self._getCharacterData()

        if name == 'author':
            author_names.append(self._field_data)

        if name in pub_types:
            for field in all_fields:
                field_counts[name][field].add(self._pub_field_counts[field])
            for attribute in all_attributes:
                attribute_counts[name][attribute].add(self._pub_attribute_counts[attribute])
        elif name in all_fields:
            string_max_length[name] = max(string_max_length[name], len(self._field_data))


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

def map_count(field_count_set):
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

field_counts_no_zero = {pub_type:{field: map_count(field_counts[pub_type][field]) \
                        for field in field_counts[pub_type].keys() \
                        if field_counts[pub_type][field] != set([0])} \
                        for pub_type in pub_types}

attribute_counts_no_zero = {pub_type:{attribute: map_count(attribute_counts[pub_type][attribute]) for attribute in attribute_counts[pub_type].keys() if attribute_counts[pub_type][attribute] != set([0])} for pub_type in pub_types}

# 1. Common Fields and Attributes
print()
print('='*50)
print('1. Common Fields and Attributes for all publication types')

print('Common Fields: ')
common_fileds = set(all_fields)
for key, value in field_counts_no_zero.items():
    common_fileds = common_fileds.intersection(set(value.keys()))
print(common_fileds)

print('Common Attributes: ')
common_attributes = set(all_attributes)
for key, value in attribute_counts_no_zero.items():
    common_attributes = common_attributes.intersection(set(value.keys()))
print(common_attributes)


# 2. field counts -----------------------------------------------------------------
print()
print('='*50)
print('2. Field count for each publication')


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print('Attributes:')
print(pd.DataFrame.from_dict(attribute_counts_no_zero).reset_index())
print()
print('Fields:')
print(pd.DataFrame.from_dict(field_counts_no_zero))

for pub_type in pub_types:
    print('-'*50)
    print('Publication type: {}'.format(pub_type))
    print()

    df = pd.DataFrame.from_dict(data = attribute_counts_no_zero[pub_type], orient='index').reset_index()
    df.columns = ['Attributes', 'Count']
    print(df)

    print()

    df = pd.DataFrame.from_dict(data = field_counts_no_zero[pub_type], orient='index').reset_index()
    df.columns = ['Fields', 'Count']
    print(df)

# 3. field maximum string length
print()
print('='*50)
print('3. Maximum length for each string element')
df = pd.DataFrame.from_dict(data = string_max_length, orient='index').reset_index()
df.columns = ['Field', 'Max String Length']
print(df)


# 4. author maximum word length
print()
print('='*50)
print("4. Number of words in Authors' Name")


print()
print('-'*50)
print('Occurance of each possible number of words:')
author_names_word_counts = [len(name.split(' ')) for name in author_names]
from collections import Counter
author_names_word_counts = Counter(author_names_word_counts)
df = pd.DataFrame.from_dict(data = author_names_word_counts, orient='index').reset_index()
df.columns = ['Name Word Count', 'Occurance']
print(df.sort_values(['Name Word Count']))

for word_count in sorted(df['Name Word Count']):
    print()
    print('-'*50)
    print('Author name with {} words:'.format(word_count))
    author_names_words_max = df['Name Word Count'].max()
    name_list = set([name for name in author_names if len(name.split(' ')) == word_count])
    for name in list(name_list)[:min(20, len(name_list))]:
        print('\t' + name)


# 5. duplicated attributes
print()
print('='*50)
print("5. Check duplicated keys")
print('Length of Attributes: {}'.format(len(attributes)))
unique_keys = [attribute for attribute in attributes if 'key' in attribute]
print('Length of Unique Attributes: {}'.format(len(unique_keys)))
if len(unique_keys) == len(attributes):
    print('There is no duplicated keys')
else:
    print('There is duplicated keys')

s = [attribute.getValue('publtype') for attribute in attributes if 'publtype' in attribute]
set(s)
