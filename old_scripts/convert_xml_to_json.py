# Import libraries
from xml.sax.handler import ContentHandler
import xml.sax
import datetime
import csv
import pandas as pd
import json

# Configure paths
xml_path = './data/dblp.xml'
# xml_path = './data/dblp_sample.xml'
json_path = './data/dblp.json'

pub_types = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', \
            'phdthesis', 'mastersthesis', 'www']
all_fields = ['title',  'author',  'year',  'month',  'crossref']
all_attributes = ['key', 'mdate']

dblp = {}

class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._pub_elements = {}
        self.data = None


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

            self._pub_elements = {'pubType': name}
            self._pub_elements['key'] = attrs.getValue('key')
            # self._pub_elements['mdate'] = attrs.getValue('mdate')

    def endElement(self, name):

        self.data = self._getCharacterData()

        if name in ['year', 'month', 'booktitle', 'crossref']:
            if name not in self._pub_elements:
                self._pub_elements[name] = self.data

        if name in ['cite', 'editor', 'author']:
            if name not in self._pub_elements:
                self._pub_elements[name] = [self.data]
            else:
                self._pub_elements[name].append(self.data)

        if name in pub_types:
            dblp[self._pub_elements['key']] = self._pub_elements


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))

with open(json_path, 'w') as outfile:
    json.dump(dblp, outfile)
