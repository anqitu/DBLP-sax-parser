from collections import Counter
import json
import random
import datetime
flatten = lambda l: [item for sublist in l for item in sublist]

json_path = './data/dblp.json'

print('{}: Start reading json file'.format(datetime.datetime.now()))
with open(json_path) as f:
    dblp = json.load(f)
print('{}: Finish reading json file'.format(datetime.datetime.now()))

len([pub for pub in dblp.values() if 'author' not in pub and 'editor' not in pub])

# address @NOTE only three proceedings has address in New York
address = [pub for pub in dblp.values() if 'address' in pub]

# chapter @NOTE only 2 incollection has chapter
chapter = [pub for pub in dblp.values() if 'chapter' in pub]

# month @NOTE proceedings extract month, some articles has 2-3 months
len([pub['pubType'] for pub in dblp.values() if 'month' in pub and len(pub['month'].split('/')) > 1])
len([pub['pubType'] for pub in dblp.values() if 'month' in pub and len(pub['month'].split('-')) > 1])
Counter([pub['month'] for pub in dblp.values() if 'month' in pub])

[pub for pub in dblp.values() if 'month' in pub and len(pub['month'].split('/')) > 1]

# pages @NOTE there are 14 publications with 2 pages, but by convention, all others separete two pages with ','
pages = [pub for pub in dblp.values() if 'pages' in pub and len(pub['pages']) > 1]
len(pages)
pages = [pub['pages'][0] for pub in dblp.values() if 'pages' in pub and len((pub['pages'][0].split(','))) > 1]

# school
school = flatten([pub['school'] for pub in dblp.values() if 'school' in pub])
school = [pub for pub in dblp.values() if 'school' in pub and len(pub['school']) > 1 and pub['pubType'] == 'phdthesis']
len(school)
len(set(school))

# series
series = [pub for pub in dblp.values() if 'series' in pub]
series = [pub for pub in dblp.values() if 'series' in pub and len(pub['series']) > 1]

# [{'key': 'conf/f-egc/2016',
#   'pubType': 'proceedings',
#   'series': ['RNTI', "Revue des Nouvelles Technologies de l'Information"],
#   'volume': ['E-30'],
#   'year': '2016'},
#  {'key': 'conf/f-egc/2017',
#   'pubType': 'proceedings',
#   'series': ['RNTI', "Revue des Nouvelles Technologies de l'Information"],
#   'volume': ['E-33'],
#   'year': '2017'},
#  {'key': 'series/lncs/Torra16',
#   'pages': ['1-118'],
#   'pubType': 'book',
#   'series': ['Lecture Notes in Computer Science',
#    'Lecture Notes in Computer Science'],
#   'volume': ['9980'],
#   'year': '2016'},
#  {'key': 'series/lncs/Skrzypczak16',
#   'pages': ['1-206'],
#   'pubType': 'book',
#   'series': ['Lecture Notes in Computer Science',
#    'Lecture Notes in Computer Science'],
#   'volume': ['9802'],
#   'year': '2016'},
#  {'key': 'series/rnti/E27',
#   'pubType': 'book',
#   'series': ['RNTI', "Revue des Nouvelles Technologies de l'Information"],
#   'volume': ['E-27'],
#   'year': '2014'}]


volume = [pub['volume'] for pub in dblp.values() if 'volume' in pub and len(pub['volume']) > 1]
volume


authors = flatten([pub['author'] for pub in dblp.values() if 'author' in pub])
editors = flatten([pub['editor'] for pub in dblp.values() if 'editor' in pub])
len(set(authors).difference(set(editors)))
len(set(editors).intersection(set(authors)))
len(set(editors).difference(set(authors)))
len(set(editors))
len(set(authors))
Counter(editors)

[pub['publisher'] for pub in dblp.values() if 'publisher' in pub and len(pub['publisher']) > 1]

publishers = [pub['publisher'] for pub in dblp.values() if 'publisher' in pub and len(pub['publisher']) > 1]
publishers
len(set(editors))
Counter(editors)

volumns = [pub['publisher'] for pub in dblp.values() if 'publisher' in pub and len(pub['publisher']) > 1]
publishers
len(set(editors))
Counter(editors)

pub_lists = [pub['pubType'] for pub in dblp.values()]
Counter(pub_lists)
# Counter({'article': 1883358,
#          'book': 15413,
#          'incollection': 47356,
#          'inproceedings': 2245681,
#          'mastersthesis': 10,
#          'phdthesis': 67442,
#          'proceedings': 38178,
#          'www': 2150508})
pub_types = set(pub_lists)


article = {key:value for key, value in dblp.items() if value['pubType'] == 'article'}
book = {key:value for key, value in dblp.items() if value['pubType'] == 'book'}
incollection = {key:value for key, value in dblp.items() if value['pubType'] == 'incollection'}
inproceedings = {key:value for key, value in dblp.items() if value['pubType'] == 'inproceedings'}
mastersthesis = {key:value for key, value in dblp.items() if value['pubType'] == 'mastersthesis'}
phdthesis = {key:value for key, value in dblp.items() if value['pubType'] == 'phdthesis'}
proceedings = {key:value for key, value in dblp.items() if value['pubType'] == 'proceedings'}
www = {key:value for key, value in dblp.items() if value['pubType'] == 'www'}


# article -------------------------------------------------------------------------
Counter([(pub['key']).split('/')[0] for pub in article.values()])
[pub for pub in article.values() if (pub['key']).split('/')[0] == 'conf']
[pub for pub in article.values() if (pub['key']).split('/')[0] == 'conf' and 'journal' not in pub]
[pub for pub in article.values() if (pub['key']).split('/')[0] == 'tr']
[pub for pub in article.values() if (pub['key']).split('/')[0] == 'journals']
[pub for pub in article.values() if (pub['key']).split('/')[0] == 'dblpnote']
[pub for pub in article.values() if (pub['key']).split('/')[0] == 'persons']

article_with_crossrefs = [pub for pub in article.values() if ('crossref' in pub)]
article_with_crossrefs
crossrefs = [pub['crossref'][0] for pub in article_with_crossrefs]
len(crossrefs)
crossrefs = [pub for pub in dblp.values() if pub['key'] in crossrefs]
Counter([pub['pubType'] for pub in crossrefs])
Counter([pub['key'].split('/')[0] for pub in crossrefs])
[pub for pub in crossrefs if pub['key'].split('/')[0] == 'conf']
[pub for pub in crossrefs if pub['key'].split('/')[0] == 'journals']
# @NOTE: All articles are referencing to a conference or a journal

[pub for pub in article.values() if 'booktitle' in pub and 'crossref' not in pub]

# book -------------------------------------------------------------------------
Counter([(pub['key']).split('/')[0] for pub in book.values()])
[pub for pub in book.values() if (pub['key']).split('/')[0] == 'conf']
[pub for pub in book.values() if (pub['key']).split('/')[0] == 'phd']
[pub for pub in book.values() if (pub['key']).split('/')[0] == 'series']
[pub for pub in book.values() if (pub['key']).split('/')[0] == 'tr']

[pub for pub in book.values() if 'booktitle' in pub]


# incollection -------------------------------------------------------------------------
Counter([(pub['key']).split('/')[0] for pub in incollection.values()])
[pub for pub in incollection.values() if (pub['key']).split('/')[0] == 'series']
[pub for pub in incollection.values() if (pub['key']).split('/')[0] == 'books']
[pub for pub in incollection.values() if (pub['key']).split('/')[0] == 'journals']
[pub for pub in incollection.values() if (pub['key']).split('/')[0] == 'reference']
[pub for pub in incollection.values() if (pub['key']).split('/')[0] == 'conf']

incollection_with_crossrefs = [pub for pub in incollection.values() if ('crossref' in pub)]
incollection_crossrefs = [pub['crossref'][0] for pub in incollection_with_crossrefs]
Counter([key.split('/')[0] for key in incollection_crossrefs])

[pub for pub in book.values() if 'booktitle' in pub]



# inproceedings ----------------------------------------------------------------
# Some inproceedings has many crossref
pub_with_many_crossrefs = [pub for pub in inproceedings.values() if ('crossref' in pub and len(pub['crossref']) > 1)]
pub_with_many_crossrefs
len(pub_with_many_crossrefs)
conf_keys = list(set(flatten([pub['crossref'] for pub in pub_with_many_crossrefs])))
print(conf_keys)
print(json.dumps([pub for pub in dblp.values() if pub['key'] in conf_keys], indent = 4))
[pub for pub in dblp.values() if ('crossref' in pub and pub['crossref'][0] == conf_keys[0])]
[pub for pub in dblp.values() if ('crossref' in pub and pub['crossref'][0] == conf_keys[1])]
[pub for pub in dblp.values() if ('crossref' in pub and pub['crossref'][0] == conf_keys[2])]

# @NOTE the second crossref is a combination of the first crossref and a letter, we take first crossref

[pub for pub in dblp.values() if 'crossref' in pub and 'conf' in pub['crossref'][0] ][:10]
pub_with_many_crossrefs


[pub for pub in inproceedings.values() if 'booktitle' in pub]

# mastersthesis -------------------------------------------------------------------------



# phdthesis -------------------------------------------------------------------------


# proceedings -------------------------------------------------------------------------
proceedings
# Some proceedings has a crossref
proceedings_with_crossrefs = [pub for pub in proceedings.values() if ('crossref' in pub and len(pub['crossref']) == 1)]
print('No of proceedings with a crossref: {}'.format(len(proceedings_with_crossrefs)))

proceedings_with_crossref_same_key = [proceedings_with_crossref for proceedings_with_crossref in proceedings_with_crossrefs if proceedings_with_crossref['crossref'][0] == proceedings_with_crossref['key']]
print('No. of proceedings with crossref same as key: {}'.format(len(proceedings_with_crossref_same_key)))

# @NOTE: those proceedings with a crossref have the key same as the crossref

proceedings_with_crossref_diff_key = [proceedings_with_crossref for proceedings_with_crossref in proceedings_with_crossrefs if proceedings_with_crossref['crossref'][0] != proceedings_with_crossref['key']]
print('No. of proceedings with crossref different from key: {}'.format(len(proceedings_with_crossref_diff_key)))
print('proceedings with crossref different from key:')
print(json.dumps(proceedings_with_crossref_diff_key, indent = 4))

print(json.dumps([pub for pub in proceedings.values() if pub['key'] == proceedings_with_crossref_diff_key[0]['crossref'][0]], indent = 4))
print(json.dumps([pub for pub in dblp.values() if 'crossref' in pub and pub['crossref'][0] == proceedings_with_crossref_diff_key[0]['crossref'][0]], indent = 4))
print(json.dumps([pub for pub in dblp.values() if 'crossref' in pub and pub['crossref'][0] == proceedings_with_crossref_diff_key[0]['key'][0]], indent = 4))

# @NOTE: There is one proceedings with a crossref that is a key of another proceeding. But it does not have inproceedings


# Proceedings start with different word
Counter([(pub['key']).split('/')[0] for pub in proceedings.values()])
[pub for pub in proceedings.values() if (pub['key']).split('/')[0] == 'series']
[pub for pub in proceedings.values() if (pub['key']).split('/')[0] == 'books']
[pub for pub in proceedings.values() if (pub['key']).split('/')[0] == 'journals']
len([pub for pub in proceedings.values() if (pub['key']).split('/')[0] == 'journals'])
[pub for pub in proceedings.values() if (pub['key']).split('/')[0] == 'reference']
[pub for pub in proceedings.values() if (pub['key']).split('/')[0] == 'conf'][0]['key']
[pub for pub in proceedings.values() if (pub['key']).split('/')[0] == 'tr'][0]['key']

[pub for pub in proceedings.values() if '/sp/' in pub['key']]

# Some proceedings has a journal
proceedings_with_journal = [pub for pub in proceedings.values()]

proceeding_keys = [pub['key'] for pub in proceedings.values()]
proceeding_keys
proceeding_keys_start = [pub['key'].split('/')[0] for pub in proceedings.values()]
Counter(proceeding_keys_start)

conf_names = [pub.split('/')[1] for pub in proceeding_keys]
len(conf_names)
len(set(conf_names))
[conf_key for conf_key in conf_keys if 'pvldb' in conf_key]
[conf_key for conf_key in conf_keys if 'sigmod' in conf_key]

# @NOTE have a column of conference name for each conference

# www -------------------------------------------------------------------------
www
Counter([(pub['key']).split('/')[0] for pub in www.values()])
[pub for pub in www.values() if (pub['key']).split('/')[0] == 'www']
[pub for pub in www.values() if (pub['key']).split('/')[0] == 'persons']
[pub for pub in www.values() if (pub['key']).split('/')[0] == 'homepages']

# some authors have many names
author_keys = [pub['key'] for pub in www.values() if (pub['key']).split('/')[0] == 'homepages']
author_names = flatten([pub['author'] for pub in www.values() if ('author' in pub) and ((pub['key']).split('/')[0] == 'homepages')])
author_primary_names = [pub['author'][0] for pub in www.values() if ('author' in pub) and ((pub['key']).split('/')[0] == 'homepages')]
len(author_keys)
len(set(author_keys))
len(author_names)
len(set(author_names))
len(author_primary_names)
len(set(author_primary_names))

pub_author_names = flatten([pub['author'] for pub in www.values() if ('author' in pub)])
len(pub_author_names)
len(set(pub_author_names))

len(set(pub_author_names).difference(set(author_names)))
len(set(pub_author_names).difference(set(author_primary_names)))

# @NOTE each author has many names which could appears in the publication

# some www has crossref
wwws_with_crossrefs = [pub['crossref'].split('/')[0] for pub in www.values() if ('crossref' in pub)]
set(wwws_with_crossrefs)
[pub for pub in wwws_with_crossrefs if ('author' in pub)]
# @NOTE ignore those crossref for www


crossrefs = [pub['crossref'] for pub in dblp.values() if 'crossref' in pub]
pub_with_crossrefs = [pub['pubType'] for pub in dblp.values() if 'crossref' in pub]
len(crossrefs)
len(set(crossrefs))
Counter([crossref.split('/')[0] for crossref in crossrefs])
Counter(pub_with_crossrefs)


keys = [pub['key'] for pub in dblp.values()]
len(keys)
len(set(keys))

len(set(crossrefs).intersection(set(keys)))
set(crossrefs).difference(set(keys))
# @NOTE there are two crossrefs which do not appear as a key in another publications
[pub for pub in dblp.values() if pub['crossref'] in set(crossrefs).difference(set(keys))]

# booktitle
wwws_with_crossrefs = [pub for pub in www.values() if ('booktitle' in pub)]
wwws_with_crossrefs

# cite
wwws_with_crossrefs = [pub for pub in www.values() if ('booktitle' in pub)]

# editors
wwws_with_editors = [pub for pub in www.values() if ('editor' in pub)]
wwws_with_editors

# author
www.values()
wwws_with_authors = [pub for pub in www.values() if ('author' in pub)]
wwws_with_authors


# check publications being referenced by ---------------------------------------
crossrefs = set([pub['crossref'] for pub in dblp.values() if 'crossref' in pub and pub['pubType'] != 'www'])
publication_referenced = []
for crossref in crossrefs:
    try:
        publication_referenced.append(dblp[crossref])
    except:
        print(crossref)
        pass
# homepages/181/2310
# homepages/71/7475

Counter([pub['pubType'] for pub in publication_referenced])
# Counter({'book': 1228, 'proceedings': 37980, 'www': 313})

# @NOTE ignore www referenced by
# [pub for pub in publication_referenced if pub['pubType'] == 'www' and 'homepages' not in pub['key']]

# @NOTE book is referenced by {'incollection', 'inproceedings'}
book_crossrefed_keys = set([pub['key'] for pub in publication_referenced if pub['pubType'] == 'book'])
len(book_crossrefed_keys)
book_referenced = [pub for pub in publication_referenced if pub['pubType'] == 'book']
pub_referencing_book = [pub['pubType'] for pub in dblp.values() if 'crossref' in pub and pub['crossref'] in book_crossrefed_keys]
set(pub_referencing_book)


Counter([pub['key'].split('/')[0] for pub in book_referenced])
[pub for pub in book_referenced if pub['key'].split('/')[0] == 'conf']
[pub for pub in dblp.values() if pub['crossref'] in ]

# @NOTE proceedings is referenced by {'article', 'incollection', 'inproceedings', 'proceedings'(ignore)}
proceeding_crossrefed_keys = set([pub['key'] for pub in publication_referenced if pub['pubType'] == 'proceedings'])
len(proceeding_crossrefed_keys)
proceeding_referenced = [pub for pub in publication_referenced if pub['pubType'] == 'book']
pub_referencing_proceeding = [pub['pubType'] for pub in dblp.values() if 'crossref' in pub and pub['crossref'] in proceeding_crossrefed_keys]
set(pub_referencing_proceeding)


proceeding_referenced = [pub for pub in publication_referenced if pub['pubType'] == 'proceedings']
proceeding_referenced
Counter([pub['key'].split('/')[0] for pub in proceeding_referenced])


publication_referenced_has_same_cr_as_key = [pub for pub in publication_referenced if 'crossref' in pub and pub['crossref'] == pub['key']]
len(publication_referenced_has_same_cr_as_key)

len([pub for pub in publication_referenced if 'crossref' in pub and pub['crossref'] != pub['key']])
publication_referenced_has_cr = [pub for pub in publication_referenced if 'crossref' in pub and pub['crossref'] != pub['key']]
publication_referenced_has_cr
set([pub['key'] for pub in publication_referenced_has_cr])
set([pub['crossref'] for pub in publication_referenced_has_cr])

[pub for pub in dblp.values() if pub['key'] == 'conf/webist/2006-1']
[pub for pub in dblp.values() if pub['key'] == 'conf/webist/2006-2']

pub_citing = [pub for pub in dblp.values() if 'cite' in pub]
[pub for pub in pub_citing if pub['pubType'] == 'www']
Counter([pub['pubType'] for pub in pub_citing])



cites = [pub['cite'] for pub in dblp.values() if 'cite' in pub]
len(cites)
cites = flatten(cites)
len(cites)
len(set(cites))

pub_cited = []
pub_cited_unfound = []
for key in [key for key in cites if key != '...']:
    try:
        pub_cited.append(dblp[key])
    except:
        pub_cited_unfound.append(key)
Counter([pub['pubType'] for pub in pub_cited])


# @NOTE citing
# Counter({'article': 1840,
#          'book': 10,
#          'incollection': 42,
#          'inproceedings': 6370,
#          'proceedings': 1,
#          'www': 102})
# @NOTE cited
# Counter({'article': 44018,
#          'book': 6614,
#          'incollection': 1377,
#          'inproceedings': 59713,
#          'mastersthesis': 3,
#          'phdthesis': 244,
#          'proceedings': 606,
#          'www': 51})
