# Import libraries
from xml.sax.handler import ContentHandler
import xml.sax
import datetime
import csv

# Configure paths
# xml_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/dblp.xml'
xml_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/dblp.000.xml'
pub_csv_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/publication.csv'

# table field and field names
pub_types = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www']


# required_fields = ['title',  'author',  'year',  'month',  'journal',  'crossref']
# required_attributes = ['key']

pub_fields = ['pubKey', 'pubTitle', 'pubYear', 'pubMonth']
author_fields = ['authorId', 'authorFirstName', 'authorSecondName']

attributes = []

results = {pub_type:[] for pub_type in pub_types}
article_elements = {}
pub_structure = []
author_names = []
author_names = []

xml_elements = set()

pub_field_counts = {pub_type:{field: set([0]) for field in all_fields} for pub_type in pub_types}
pub_field_counts_new = {pub_type:{field: pub_field_counts[pub_type][field] for field in pub_field_counts[pub_type].keys() if pub_field_counts[pub_type][field] != set([0])} for pub_type in pub_types}
pub_field_counts_new_required = {pub_type:{field: pub_field_counts_new[pub_type][field] for field in pub_field_counts_new[pub_type].keys() if field in required_fields} for pub_type in pub_types}

field_max_len = {field: 0 for field in all_fields}



class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._current_authorID = ''
        self._pub_fields = {}
        self._author_fields = {}
        self._authoredBy_fields = {}
        self._field_data = None

        self._pub_writer = csv.DictWriter(open(pub_csv_path, 'w'), fieldnames = pub_field_names, delimiter='|')
        self._pub_writer.writeheader()

    def _getCharacterData(self):
        data = ''.join(self._charBuffer).strip()
        self._charBuffer = []
        return data.strip() #remove strip() if whitespace is important

        # pass

    def parse(self, f):
        xml.sax.parse(f, self)

    def characters(self, data):
        self._charBuffer.append(data)

        # pass

    def startElement(self, name, attrs):
        if name in pub_types:
            self._pub_fields = {field: None for field in pub_field_names}
            self._pub_field['key'] = attrs.getValue('key')

        #     results[name].append({})
        #     attributes.append(attrs)
        #     pub_structure.append([])
        # pass

    def endElement(self, name):
        self._field_data = self._getCharacterData()
        if name in pub_field_names:
            self._pub_field[name] = self._field_data
        elif name in pub_types:
            self._pub_writer.writerow(self._pub_field)
        if name == 'author':
            author_names.append(self._field_data)


        #     results[self._current_pub_type][-1][name] = self._getCharacterData()
        #     pub_structure[-1].append(name)


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

[name for name in author_names if len(name.split(' ')) > 5]
author_names

pub_field_counts

xml_elements

# attributes
len(attributes)
attr = attributes[0]
attr.getValue('key')
attr.getNames()
attr.getType('key')
attr.getLength()

results.keys()
len(results['article'])
results['article'][0]


len(pub_structure)
set(pub_structure)
