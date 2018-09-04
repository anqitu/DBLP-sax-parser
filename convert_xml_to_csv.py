from xml.sax.handler import ContentHandler
import xml.sax
import datetime

xml_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/dblp.xml'
# xml_path = '/Users/anqitu/Workspaces/NTU/CZ4031-Project1-Querying-Databases-Efficiently/data/dblp.000.xml'

pub_types = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www']
fields = ['title',  'author',  'year',  'month',  'journal',  'crossref', \
        'address', 'booktitle', 'cdrom', 'chapter', 'cite', 'editor', 'ee', \
        'i', 'isbn', 'note', 'number', 'pages', 'publisher', 'school', \
        'series', 'sub', 'sup', 'tt', 'url', 'volume']

attributes = []
dblps = []
results = {pub_type:[] for pub_type in pub_types}
article_elements = {}
pub_structure = []
xml_elements = set()
pub_field_counts = {pub_type:{field: 0 for field in fields} for pub_type in pub_types}
pub_field_counts


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
                pub_field_counts[self._current_pub_type][field] = max(count, pub_field_counts[self._current_pub_type][field])



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
