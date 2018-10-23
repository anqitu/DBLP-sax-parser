# Import libraries
from xml.sax.handler import ContentHandler
import xml.sax
import datetime
import csv

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

class StreamHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._charBuffer = []
        self._field_data = None

        self._is_www_homepages = False
        self._person_key = None
        self._person_names = None
        self._pub_count = 0

        self._pub_fields = None
        self._pub_subclass_fields = None
        self._current_pub_type = None
        self._is_publication = False

        self._key = None
        self._months = None
        self._pub_cites = None
        self._pub_authors = None
        self._pub_editors = None
        self._pub_schools = None

        self._person_writer = csv.DictWriter(open(person_csv_path, 'w'), fieldnames = person_attributes, delimiter = '|')
        self._person_writer.writeheader()

        self._alias_writer = csv.DictWriter(open(alias_csv_path, 'w'), fieldnames = alias_attributes, delimiter = '|')
        self._alias_writer.writeheader()

        self._pub_subclass_writers = {
                            'article': csv.DictWriter(open(pub_subclass_csv_path['article'], 'w'), fieldnames = pub_subclass_attributes_map['article'].values(), delimiter = '|'),
                            'inproceedings': csv.DictWriter(open(pub_subclass_csv_path['inproceedings'], 'w'), fieldnames = pub_subclass_attributes_map['inproceedings'].values(), delimiter = '|'),
                            'incollection': csv.DictWriter(open(pub_subclass_csv_path['incollection'], 'w'), fieldnames = pub_subclass_attributes_map['incollection'].values(), delimiter = '|'),
                            'proceedings': csv.DictWriter(open(pub_subclass_csv_path['proceedings'], 'w'), fieldnames = pub_subclass_attributes_map['proceedings'].values(), delimiter = '|'),
                            'book': csv.DictWriter(open(pub_subclass_csv_path['book'], 'w'), fieldnames = pub_subclass_attributes_map['book'].values(), delimiter = '|'),
                            'thesis': csv.DictWriter(open(pub_subclass_csv_path['thesis'], 'w'), fieldnames = pub_subclass_attributes_map['thesis'].values(), delimiter = '|'),
                            'www': csv.DictWriter(open(pub_subclass_csv_path['www'], 'w'), fieldnames = pub_subclass_attributes_map['www'].values(), delimiter = '|'),
                            }
        for subclass_writer in self._pub_subclass_writers.values():
            subclass_writer.writeheader()

        self._pub_writer = csv.DictWriter(open(pub_csv_path, 'w'), fieldnames = pub_attributes.values(), delimiter = '|')
        self._pub_writer.writeheader()

        self._month_writer = csv.DictWriter(open(month_csv_path, 'w'), fieldnames = month_attributes, delimiter = '|')
        self._month_writer.writeheader()

        self._citership_writer = csv.DictWriter(open(citership_csv_path, 'w'), fieldnames = citership_attributes, delimiter = '|')
        self._citership_writer.writeheader()

        self._pub_school_writer = csv.DictWriter(open(pub_school_csv_path, 'w'), fieldnames = pub_school_attributes, delimiter = '|')
        self._pub_school_writer.writeheader()

        self._authorship_writer = csv.DictWriter(open(authorship_csv_path, 'w'), fieldnames = authorship_attributes, delimiter = '|')
        self._authorship_writer.writeheader()

        self._editorship_writer = csv.DictWriter(open(editorship_csv_path, 'w'), fieldnames = editorship_attributes, delimiter = '|')
        self._editorship_writer.writeheader()

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

            self._pub_count += 1
            if self._pub_count % 100000 == 0:
                print('Current count: {}'.format(self._pub_count))

            if name == 'www' and ('homepages' in attrs.getValue('key')):

                self._is_www_homepages = True

                self._person_key = attrs.getValue('key')
                self._person_names = []

            elif name != 'www' or (name == 'www' and 'www' in attrs.getValue('key')):

                self._is_publication = True
                self._current_pub_type = 'thesis' if name in ['mastersthesis', 'phdthesis'] else name

                self._key = attrs.getValue('key')
                mdate = attrs.getValue('mdate')

                self._pub_fields = {attribute: '\\N' for attribute in pub_attributes.keys()}
                self._pub_fields['key'] = self._key
                self._pub_fields['mdate'] = mdate
                self._pub_fields['type'] = name

                self._pub_subclass_fields = {attribute: '\\N' for attribute in pub_subclass_attributes_map[self._current_pub_type].keys()}
                self._pub_subclass_fields['key'] = self._key

                if self._current_pub_type == 'proceedings':
                    self._pub_subclass_fields['type'] = self._key.split('/')[0]

                self._months = []
                self._pub_cites = []
                self._pub_authors = []
                self._pub_editors = []
                self._pub_schools = []



    def endElement(self, name):
        self._field_data = self._getCharacterData().replace('|', '-').replace('"', '')

        if self._is_www_homepages:
            if name == 'author':
                self._person_names.append(self._field_data)
            elif name == 'www' and len(self._person_names) != 0:
                self._person_writer.writerow({'personKey': self._person_key, 'personFullName': self._person_names[0]})
                for alias in self._person_names[1:]:
                    self._alias_writer.writerow({'personKey': self._person_key, 'personFullName': alias})

                self._is_www_homepages = False

        elif self._is_publication:

            if name == 'cite':
                self._pub_cites.append(self._field_data)

            elif name == 'title':
                self._pub_fields[name] = self._field_data

                if self._current_pub_type == 'proceedings':
                    for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
                        if month in self._field_data:
                            self._months.append(month)

            elif name == 'year':
                self._pub_fields[name] = self._field_data

            elif name == 'publisher' and self._pub_fields['publisher'] == '\\N':
                self._pub_fields['publisher'] = self._field_data

            elif name == 'month':
                # split months if more than one
                for month in self._field_data.replace('-', '/').split('/'):
                    self._months.append(month)

            elif name == 'school':
                self._pub_schools.append(self._field_data)

            elif name == 'author':
                self._pub_authors.append(self._field_data)

            elif name == 'editor':
                self._pub_editors.append(self._field_data)

            elif name in pub_subclass_attributes_map[self._current_pub_type].keys():

                # combine several pages into one string seperate by ','
                if name == 'pages':
                    if self._pub_subclass_fields['pages'] != '\\N':
                        self._pub_subclass_fields['pages'] = self._pub_subclass_fields['pages'] + ', ' + self._field_data
                    else:
                        self._pub_subclass_fields['pages'] = self._field_data

                # Only keep those longer version for publications with more than 1 series or colume
                elif name in ['series', 'volume']:
                    if self._pub_subclass_fields[name] != '\\N':
                        self._pub_subclass_fields[name] = self._pub_subclass_fields[name] if len(self._pub_subclass_fields[name]) > len(self._field_data) else self._field_data
                    else:
                        self._pub_subclass_fields[name] = self._field_data

                else:
                    self._pub_subclass_fields[name] = self._field_data

            elif name in pub_types:

                self._pub_fields = {pub_attributes[key]: value for key, value in self._pub_fields.items()}
                self._pub_subclass_fields = {pub_subclass_attributes_map[self._current_pub_type][key]: value for key, value in self._pub_subclass_fields.items()}

                self._pub_writer.writerow(self._pub_fields)
                self._pub_subclass_writers[self._current_pub_type].writerow(self._pub_subclass_fields)

                for month in self._months:
                    self._month_writer.writerow({'pubKey': self._key, 'pubMonth': month})

                for cited_pub in set(self._pub_cites):
                    self._citership_writer.writerow({'citingPubKey': self._key, 'citedPubKey': cited_pub})

                for author in set(self._pub_authors):
                    self._authorship_writer.writerow({'pubKey': self._key, 'personFullName': author})

                for editor in set(self._pub_editors):
                    self._editorship_writer.writerow({'pubKey': self._key, 'personFullName': editor})

                for school in set(self._pub_schools):
                    self._pub_school_writer.writerow({'pubKey': self._key, 'schoolName': school})

                self._is_publication = False

            else:
                pass



print('{}: Start parsing'.format(datetime.datetime.now()))
StreamHandler().parse(xml_path)
print('{}: End parsing'.format(datetime.datetime.now()))
