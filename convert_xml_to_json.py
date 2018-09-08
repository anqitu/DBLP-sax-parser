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
json_sample_path = './data/dblp_sample.json'

pub_types = ['article', 'inproceedings', 'proceedings', 'book', 'incollection', \
            'phdthesis', 'mastersthesis', 'www']
all_fields = ['title',  'author',  'year',  'month',  'journal',  'crossref']
all_attributes = ['key']

dblp = {}

class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._pub_elements = {}
        self._pubID = 0


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
            self._pubID += 1

            if self._pubID % 100000 == 0:
                print(elf._pubID)

            self._pub_elements = {'pubType': name}

            for attribute in all_attributes:
                if attribute in attrs.getNames():
                    self._pub_elements[attribute] = attrs.getValue(attribute)

    def endElement(self, name):

        if name in all_fields:
            if name not in self._pub_elements:
                self._pub_elements[name] = [self._getCharacterData()]
            else:
                self._pub_elements[name].append(self._getCharacterData())

        if name in pub_types:
            dblp[self._pubID] = self._pub_elements


print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))


with open(json_path, 'w') as outfile:
    json.dump(dblp, outfile)


pubId_sample = range(1, 100001)
dblp_sample = {pubID: dblp[pubID] for pubID in pubId_sample}
dblp_sample[1]
with open(json_sample_path, 'w') as outfile:
    json.dump(dblp, outfile)
