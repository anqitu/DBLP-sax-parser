from xml.sax.handler import ContentHandler
import xml.sax
import datetime

xml_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/dblp.xml'
# xml_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/dblp.000.xml'

pub_types = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www']
all_fields = ['title',  'author',  'year',  'month',  'journal',  'crossref', \
        'address', 'booktitle', 'cdrom', 'chapter', 'cite', 'editor', 'ee', \
        'i', 'isbn', 'note', 'number', 'pages', 'publisher', 'school', \
        'series', 'sub', 'sup', 'tt', 'url', 'volume']
required_fields = ['title',  'author',  'year',  'month',  'journal',  'crossref']

attributes = []
dblps = []
results = {pub_type:[] for pub_type in pub_types}
article_elements = {}
pub_structure = []
xml_elements = set()
pub_field_counts = {pub_type:{field: set([0]) for field in all_fields} for pub_type in pub_types}

# pub_field_counts = {'article': {'address': 0,
#                                 'author': 287,
#                                 'booktitle': 1,
#                                 'cdrom': 1,
#                                 'chapter': 0,
#                                 'cite': 348,
#                                 'crossref': 1,
#                                 'dblp': 0,
#                                 'editor': 5,
#                                 'ee': 2,
#                                 'i': 38,
#                                 'isbn': 0,
#                                 'journal': 1,
#                                 'month': 1,
#                                 'note': 2,
#                                 'number': 1,
#                                 'pages': 1,
#                                 'publisher': 1,
#                                 'school': 0,
#                                 'series': 0,
#                                 'sub': 16,
#                                 'sup': 11,
#                                 'title': 1,
#                                 'tt': 2,
#                                 'url': 1,
#                                 'volume': 1,
#                                 'year': 1},
#
#                                 'book': {'address': 0,
#                                 'author': 18,
#                                 'booktitle': 1,
#                                 'cdrom': 1,
#                                 'chapter': 0,
#                                 'cite': 741,
#                                 'crossref': 0,
#                                 'dblp': 0,
#                                 'editor': 13,
#                                 'ee': 7,
#                                 'i': 2,
#                                 'isbn': 4,
#                                 'journal': 0,
#                                 'month': 1,
#                                 'note': 1,
#                                 'number': 0,
#                                 'pages': 2,
#                                 'publisher': 2,
#                                 'school': 2,
#                                 'series': 2,
#                                 'sub': 1,
#                                 'sup': 1,
#                                 'title': 1,
#                                 'tt': 0,
#                                 'url': 2,
#                                 'volume': 1,
#                                 'year': 1},
#
#
#                                 'incollection': {'address': 0,
#                                 'author': 50,
#                                 'booktitle': 1,
#                                 'cdrom': 1,
#                                 'chapter': 1,
#                                 'cite': 104,
#                                 'crossref': 1,
#                                 'dblp': 0,
#                                 'editor': 0,
#                                 'ee': 1,
#                                 'i': 3,
#                                 'isbn': 0,
#                                 'journal': 0,
#                                 'month': 0,
#                                 'note': 1,
#                                 'number': 1,
#                                 'pages': 1,
#                                 'publisher': 1,
#                                 'school': 0,
#                                 'series': 0,
#                                 'sub': 2,
#                                 'sup': 2,
#                                 'title': 1,
#                                 'tt': 0,
#                                 'url': 1,
#                                 'volume': 0,
#                                 'year': 1},
#
#                                 'inproceedings': {'address': 0,
#                                 'author': 139,
#                                 'booktitle': 1,
#                                 'cdrom': 2,
#                                 'chapter': 0,
#                                 'cite': 137,
#                                 'crossref': 2,
#                                 'dblp': 0,
#                                 'editor': 3,
#                                 'ee': 7,
#                                 'i': 10,
#                                 'isbn': 0,
#                                 'journal': 0,
#                                 'month': 1,
#                                 'note': 1,
#                                 'number': 1,
#                                 'pages': 1,
#                                 'publisher': 0,
#                                 'school': 0,
#                                 'series': 0,
#                                 'sub': 5,
#                                 'sup': 5,
#                                 'title': 1,
#                                 'tt': 1,
#                                 'url': 3,
#                                 'volume': 0,
#                                 'year': 1},
#
#                                 'mastersthesis': {'address': 0,
#                                 'author': 1,
#                                 'booktitle': 0,
#                                 'cdrom': 0,
#                                 'chapter': 0,
#                                 'cite': 0,
#                                 'crossref': 0,
#                                 'dblp': 0,
#                                 'editor': 0,
#                                 'ee': 1,
#                                 'i': 0,
#                                 'isbn': 0,
#                                 'journal': 0,
#                                 'month': 0,
#                                 'note': 0,
#                                 'number': 0,
#                                 'pages': 0,
#                                 'publisher': 0,
#                                 'school': 1,
#                                 'series': 0,
#                                 'sub': 0,
#                                 'sup': 0,
#                                 'title': 1,
#                                 'tt': 0,
#                                 'url': 0,
#                                 'volume': 0,
#                                 'year': 1},
#
#                                 'phdthesis': {'address': 0,
#                                 'author': 3,
#                                 'booktitle': 0,
#                                 'cdrom': 0,
#                                 'chapter': 0,
#                                 'cite': 0,
#                                 'crossref': 0,
#                                 'dblp': 0,
#                                 'editor': 0,
#                                 'ee': 7,
#                                 'i': 2,
#                                 'isbn': 3,
#                                 'journal': 0,
#                                 'month': 1,
#                                 'note': 2,
#                                 'number': 1,
#                                 'pages': 2,
#                                 'publisher': 1,
#                                 'school': 3,
#                                 'series': 1,
#                                 'sub': 2,
#                                 'sup': 1,
#                                 'title': 1,
#                                 'tt': 0,
#                                 'url': 1,
#                                 'volume': 1,
#                                 'year': 1},
#
#                                 'proceedings': {'address': 1,
#                                 'author': 1,
#                                 'booktitle': 1,
#                                 'cdrom': 0,
#                                 'chapter': 0,
#                                 'cite': 212,
#                                 'crossref': 1,
#                                 'dblp': 0,
#                                 'editor': 31,
#                                 'ee': 5,
#                                 'i': 1,
#                                 'isbn': 3,
#                                 'journal': 1,
#                                 'month': 0,
#                                 'note': 2,
#                                 'number': 1,
#                                 'pages': 1,
#                                 'publisher': 2,
#                                 'school': 0,
#                                 'series': 2,
#                                 'sub': 1,
#                                 'sup': 2,
#                                 'title': 1,
#                                 'tt': 0,
#                                 'url': 2,
#                                 'volume': 2,
#                                 'year': 1},
#
#                                 'www': {'address': 0,
#                                 'author': 10,
#                                 'booktitle': 1,
#                                 'cdrom': 0,
#                                 'chapter': 0,
#                                 'cite': 30,
#                                 'crossref': 1,
#                                 'dblp': 0,
#                                 'editor': 6,
#                                 'ee': 1,
#                                 'i': 0,
#                                 'isbn': 0,
#                                 'journal': 0,
#                                 'month': 0,
#                                 'note': 10,
#                                 'number': 0,
#                                 'pages': 0,
#                                 'publisher': 0,
#                                 'school': 0,
#                                 'series': 0,
#                                 'sub': 0,
#                                 'sup': 0,
#                                 'title': 1,
#                                 'tt': 0,
#                                 'url': 17,
#                                 'volume': 0,
#                                 'year': 1}}
#
# pub_field_counts = {pub_type:{field: pub_field_counts[pub_type][field] for field in pub_field_counts[pub_type].keys() if pub_field_counts[pub_type][field] != 0} for pub_type in pub_types}
#
# {pub_type:{field: pub_field_counts[pub_type][field] for field in pub_field_counts[pub_type].keys() if field in required_fields} for pub_type in pub_types}

class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._current_pub_type = ''
        self._field_count = {}

    def _getCharacterData(self):
        # data = ''.join(self._charBuffer).strip()
        # self._charBuffer = []
        # return data.strip() #remove strip() if whitespace is important
        pass

    def parse(self, f):
        xml.sax.parse(f, self)

    def characters(self, data):
        # self._charBuffer.append(data)

        pass

    def startElement(self, name, attrs):
        if name in results.keys():
            self._current_pub_type = name
            self._field_count = {}

        #     results[name].append({})
        #     attributes.append(attrs)
        #     pub_structure.append([])

    def endElement(self, name):
        if not name in results.keys():
            if not name in self._field_count.keys():
                self._field_count[name] = 1
            else:
                self._field_count[name] += 1
        else:
            for field, count in self._field_count.items():
                pub_field_counts[self._current_pub_type][field].add(count)



        #     results[self._current_pub_type][-1][name] = self._getCharacterData()
        #     pub_structure[-1].append(name)


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))


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
