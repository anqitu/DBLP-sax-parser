# DBLP XML Structure

## pub_types

```
['article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www']
```
## fields
```
# Included fields
['title', 'author', 'year', 'month', 'journal', 'crossref']
```
```
# All fields
['title', 'author', 'year', 'month', 'journal', 'crossref', 'address', 'booktitle', 'cdrom', 'chapter', 'cite', 'editor', 'ee', 'i', 'isbn', 'note', 'number', 'pages', 'publisher', 'school', 'series', 'sub', 'sup', 'tt', 'url', 'volume']
 ```

## field counts for each publication
```
{'article':
  {'author': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 64, 65, 67, 68, 69, 71, 74, 75, 78, 79, 86, 92, 95, 96, 99, 101, 105, 112, 118, 119, 263, 287},
  'booktitle': {0, 1},
  'cdrom': {0, 1},
  'cite': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76, 78, 79, 81, 83, 84, 86, 87, 89, 90, 91, 92, 94, 99, 100, 101, 105, 106, 107, 109, 114, 116, 117, 120, 123, 126, 136, 137, 140, 158, 159, 163, 165, 171, 172, 174, 194, 198, 205, 232, 249, 252, 348},
  'crossref': {0, 1},
  'editor': {0, 1, 2, 3, 4, 5},
  'ee': {0, 1, 2},
  'i': {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 21, 32, 38},
  'journal': {0, 1},
  'month': {0, 1},
  'note': {0, 1, 2},
  'number': {0, 1},
  'pages': {0, 1},
  'publisher': {0, 1},
  'sub': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16},
  'sup': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11},
  'title': {0, 1},
  'tt': {0, 1, 2},
  'url': {0, 1},
  'volume': {0, 1},
  'year': {0, 1}},
 'book':
  {'author': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 17, 18},
  'booktitle': {0, 1},
  'cdrom': {0, 1},
  'cite': {0, 63, 115, 156, 189, 284, 342, 365, 421, 643, 741},
  'editor': {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 13},
  'ee': {0, 1, 2, 3, 4, 5, 6, 7},
  'i': {0, 2},
  'isbn': {0, 1, 2, 3, 4},
  'month': {0, 1},
  'note': {0, 1},
  'pages': {0, 1, 2},
  'publisher': {0, 1, 2},
  'school': {0, 1, 2},
  'series': {0, 1, 2},
  'sub': {0, 1},
  'sup': {0, 1},
  'title': {0, 1},
  'url': {0, 1, 2},
  'volume': {0, 1},
  'year': {0, 1}},
 'incollection':
  {'author': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 25, 28, 29, 32, 50},
  'booktitle': {0, 1},
  'cdrom': {0, 1},
  'chapter': {0, 1},
  'cite': {0, 1, 2, 3, 7, 8, 9, 10, 11, 16, 17, 19, 20, 23, 30, 31, 40, 43, 44, 45, 49, 59, 60, 87, 104},
  'crossref': {0, 1},
  'ee': {0, 1},
  'i': {0, 1, 2, 3},
  'note': {0, 1},
  'number': {0, 1},
  'pages': {0, 1},
  'publisher': {0, 1},
  'sub': {0, 1, 2},
  'sup': {0, 1, 2},
  'title': {0, 1},
  'url': {0, 1},
  'year': {0, 1}},
 'inproceedings':
  {'author': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 53, 55, 56, 57, 60, 61, 62, 64, 65, 70, 76, 77, 94, 102, 104, 114, 139},
  'booktitle': {0, 1},
  'cdrom': {0, 1, 2},
  'cite': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 75, 76, 78, 79, 81, 85, 87, 88, 89, 95, 100, 101, 102, 122, 124, 137},
  'crossref': {0, 1, 2},
  'editor': {0, 1, 2, 3},
  'ee': {0, 1, 2, 3, 5, 7},
  'i': {0, 1, 2, 3, 4, 5, 6, 7, 9, 10},
  'month': {0, 1},
  'note': {0, 1},
  'number': {0, 1},
  'pages': {0, 1},
  'sub': {0, 1, 2, 3, 4, 5},
  'sup': {0, 1, 2, 3, 4, 5},
  'title': {0, 1},
  'tt': {0, 1},
  'url': {0, 1, 3},
  'year': {0, 1}},
 'mastersthesis':
  {'author': {0, 1},
  'ee': {0, 1},
  'school': {0, 1},
  'title': {0, 1},
  'year': {0, 1}},
 'phdthesis':
  {'author': {0, 1, 2, 3},
  'ee': {0, 1, 2, 3, 4, 5, 6, 7},
  'i': {0, 1, 2},
  'isbn': {0, 1, 2, 3},
  'month': {0, 1},
  'note': {0, 1, 2},
  'number': {0, 1},
  'pages': {0, 1, 2},
  'publisher': {0, 1},
  'school': {0, 1, 2, 3},
  'series': {0, 1},
  'sub': {0, 2},
  'sup': {0, 1},
  'title': {0, 1},
  'url': {0, 1},
  'volume': {0, 1},
  'year': {0, 1}},
 'proceedings':
  {'address': {0, 1},
  'author': {0, 1},
  'booktitle': {0, 1},
  'cite': {0, 212},
  'crossref': {0, 1},
  'editor': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 26, 27, 31},
  'ee': {0, 1, 2, 3, 4, 5},
  'i': {0, 1},
  'isbn': {0, 1, 2, 3},
  'journal': {0, 1},
  'note': {0, 1, 2},
  'number': {0, 1},
  'pages': {0, 1},
  'publisher': {0, 1, 2},
  'series': {0, 1, 2},
  'sub': {0, 1},
  'sup': {0, 1, 2},
  'title': {0, 1},
  'url': {0, 1, 2},
  'volume': {0, 1, 2},
  'year': {0, 1}},
 'www':
  {'author': {0, 1, 2, 3, 4, 5, 6, 10},
  'booktitle': {0, 1},
  'cite': {0, 1, 2, 4, 6, 30},
  'crossref': {0, 1},
  'editor': {0, 1, 2, 4, 5, 6},
  'ee': {0, 1},
  'note': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
  'title': {0, 1},
  'url': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17},
  'year': {0, 1}}}
```

## maximum field counts for each publication
```
{'article': {'author': 287,
 'booktitle': 1,
 'cdrom': 1,
 'cite': 348,
 'crossref': 1,
 'editor': 5,
 'ee': 2,
 'i': 38,
 'journal': 1,
 'month': 1,
 'note': 2,
 'number': 1,
 'pages': 1,
 'publisher': 1,
 'sub': 16,
 'sup': 11,
 'title': 1,
 'tt': 2,
 'url': 1,
 'volume': 1,
 'year': 1},
'book': {'author': 18,
 'booktitle': 1,
 'cdrom': 1,
 'cite': 741,
 'editor': 13,
 'ee': 7,
 'i': 2,
 'isbn': 4,
 'month': 1,
 'note': 1,
 'pages': 2,
 'publisher': 2,
 'school': 2,
 'series': 2,
 'sub': 1,
 'sup': 1,
 'title': 1,
 'url': 2,
 'volume': 1,
 'year': 1},
'incollection': {'author': 50,
 'booktitle': 1,
 'cdrom': 1,
 'chapter': 1,
 'cite': 104,
 'crossref': 1,
 'ee': 1,
 'i': 3,
 'note': 1,
 'number': 1,
 'pages': 1,
 'publisher': 1,
 'sub': 2,
 'sup': 2,
 'title': 1,
 'url': 1,
 'year': 1},
'inproceedings': {'author': 139,
 'booktitle': 1,
 'cdrom': 2,
 'cite': 137,
 'crossref': 2,
 'editor': 3,
 'ee': 7,
 'i': 10,
 'month': 1,
 'note': 1,
 'number': 1,
 'pages': 1,
 'sub': 5,
 'sup': 5,
 'title': 1,
 'tt': 1,
 'url': 3,
 'year': 1},
'mastersthesis': {'author': 1, 'ee': 1, 'school': 1, 'title': 1, 'year': 1},
'phdthesis': {'author': 3,
 'ee': 7,
 'i': 2,
 'isbn': 3,
 'month': 1,
 'note': 2,
 'number': 1,
 'pages': 2,
 'publisher': 1,
 'school': 3,
 'series': 1,
 'sub': 2,
 'sup': 1,
 'title': 1,
 'url': 1,
 'volume': 1,
 'year': 1},
'proceedings': {'address': 1,
 'author': 1,
 'booktitle': 1,
 'cite': 212,
 'crossref': 1,
 'editor': 31,
 'ee': 5,
 'i': 1,
 'isbn': 3,
 'journal': 1,
 'note': 2,
 'number': 1,
 'pages': 1,
 'publisher': 2,
 'series': 2,
 'sub': 1,
 'sup': 2,
 'title': 1,
 'url': 2,
 'volume': 2,
 'year': 1},
'www': {'author': 10,
 'booktitle': 1,
 'cite': 30,
 'crossref': 1,
 'editor': 6,
 'ee': 1,
 'note': 10,
 'title': 1,
 'url': 17,
 'year': 1}}
```

## maximum string length for each field
```
{'address': 8,
 'author': 66,
 'booktitle': 206,
 'cdrom': 50,
 'chapter': 2,
 'cite': 47,
 'crossref': 38,
 'editor': 47,
 'ee': 253,
 'i': 462,
 'isbn': 18,
 'journal': 75,
 'month': 25,
 'note': 310,
 'number': 24,
 'pages': 31,
 'publisher': 162,
 'school': 104,
 'series': 135,
 'sub': 208,
 'sup': 384,
 'title': 741,
 'tt': 80,
 'url': 271,
 'volume': 31,
 'year': 4}
```

## Examples

```
<article key="journals/cacm/Gentry10" mdate="2010-04-26">
<author>Craig Gentry</author>
<title>Computing arbitrary functions of encrypted data.</title>
<pages>97-105</pages>
<year>2010</year>
<volume>53</volume>
<journal>Commun. ACM</journal>
<number>3</number>
<ee>http://doi.acm.org/10.1145/1666420.1666444</ee>
<url>db/journals/cacm/cacm53.html#Gentry10</url>
</article>
```

```
<inproceedings key="conf/focs/Yao82a" mdate="2011-10-19">
<title>Theory and Applications of Trapdoor Functions (Extended Abstract)</title>
<author>Andrew Chi-Chih Yao</author>
<pages>80-91</pages>
<crossref>conf/focs/FOCS23</crossref>
<year>1982</year>
<booktitle>FOCS</booktitle>
<url>db/conf/focs/focs82.html#Yao82a</url>
<ee>http://doi.ieeecomputersociety.org/10.1109/SFCS.1982.45</ee>
</inproceedings>
```

```
<www mdate="2004-03-23" key="homepages/g/OdedGoldreich">
<author>Oded Goldreich</author>
<title>Home Page</title>
<url>http://www.wisdom.weizmann.ac.il/~oded/</url>
</www>
```
