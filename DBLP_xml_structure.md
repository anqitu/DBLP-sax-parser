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
