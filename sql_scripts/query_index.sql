RESET QUERY CACHE;
FLUSH QUERY CACHE;
SET SESSION query_cache_type=0;

-- Question 1
CREATE INDEX type_year_index ON PUBLICATION (pubType, pubYear);
CREATE INDEX pubType_index ON PUBLICATION (pubType);
CREATE INDEX pubYear_index ON PUBLICATION (pubYear);

EXPLAIN SELECT pubType, COUNT(*) FROM PUBLICATION
WHERE pubYear >= 2000 AND pubYear <= 2017
GROUP BY pubType;

ALTER TABLE PUBLICATION DROP INDEX type_year_index;
ALTER TABLE PUBLICATION DROP INDEX pubYear_index;
ALTER TABLE PUBLICATION DROP INDEX pubType_index;


-- Question 2
CREATE INDEX proceedType_index ON PROCEEDING (proceedType);
CREATE INDEX pubMonth_index ON PUBMONTH (pubMonth);

EXPLAIN SELECT conference, MAX(pubCount) AS pubCount FROM (
	SELECT PROCEEDING.pubKey, COUNT(*) AS pubCount, SUBSTRING_INDEX(SUBSTRING_INDEX(PROCEEDING.pubKey, 'conf/', -1), '/', 1) AS conference
	FROM PROCEEDING, INPROCEEDING, PUBMONTH
	WHERE PROCEEDING.pubKey = INPROCEEDING.inproCrossRef
	AND PUBMONTH.pubKey = PROCEEDING.pubKey
	AND PUBMONTH.pubMonth = "July"
	AND proceedType = "conf"
	GROUP BY PROCEEDING.pubKey
) AS CONFERENCES
WHERE pubCount > 200
GROUP BY conference;

ALTER TABLE PROCEEDING DROP INDEX proceedType_index;
ALTER TABLE PUBMONTH DROP INDEX pubMonth_index;


-- Question 3 a
-- X(author) = "Mohamed-Slim Alouini"
CREATE INDEX pubYear_index ON PUBLICATION (pubYear);
CREATE INDEX personFullName_index ON PERSON (personFirstName, personLastName);

EXPLAIN SELECT PUBLICATION.pubKey, pubTitle, pubYear, pubMdate, pubType, publisherId, CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) as pubAuthor
FROM PUBLICATION, AUTHORSHIP, PERSON
WHERE PUBLICATION.pubKey = AUTHORSHIP.pubKey
AND AUTHORSHIP.personKey = PERSON.personKey
AND PUBLICATION.pubYear = 2015
AND PERSON.personFirstName = "Mohamed-Slim" AND PERSON.personLastName = "Alouini";

ALTER TABLE PUBLICATION DROP INDEX pubYear_index;
ALTER TABLE PERSON DROP INDEX personFullName_index;

-- Question 3 b
-- X(author) = "Alexander Sprintson", Y(year) = 2015, Z(conference) = "allerton"
CREATE INDEX pubYear_index ON PUBLICATION (pubYear);
CREATE INDEX personFullName_index ON PERSON (personFirstName, personLastName);

EXPLAIN SELECT * FROM (
	SELECT INPROCEEDING.pubKey, pubTitle, pubYear, pubMdate, pubType,
	CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) as pubAuthor,
	SUBSTRING_INDEX(SUBSTRING_INDEX(PROCEEDING.pubKey, 'conf/', -1), '/', 1) AS conference
	FROM INPROCEEDING, AUTHORSHIP, PERSON, PROCEEDING, PUBLICATION
	WHERE INPROCEEDING.pubKey = PUBLICATION.pubKey
	AND INPROCEEDING.pubKey = AUTHORSHIP.pubKey
	AND AUTHORSHIP.personKey = PERSON.personKey
	AND PROCEEDING.pubKey = INPROCEEDING.inproCrossRef
	AND PERSON.personFirstName = "Alexander" AND PERSON.personLastName = "Sprintson"
	AND PUBLICATION.pubYear = 2015
) AS AUTHOR_PUBLICATIONS
WHERE conference = "allerton";

ALTER TABLE PUBLICATION DROP INDEX pubYear_index;
ALTER TABLE PERSON DROP INDEX personFullName_index;

-- Question 3 c
-- Z(conference) = "sigmod", Y(year) = 2014
CREATE INDEX pubYear_index ON PUBLICATION (pubYear);
CREATE INDEX personKey_index ON PUBLICATION (AUTHORSHIP);

EXPLAIN SELECT
AUTHORSHIP.personKey,
CONCAT(personFirstName, " ", PERSON.personLastName) as personName,
COUNT(*) AS pubCount
FROM PUBLICATION, INPROCEEDING, AUTHORSHIP, PROCEEDING, PERSON
WHERE INPROCEEDING.pubKey = PUBLICATION.pubKey
AND INPROCEEDING.pubKey = AUTHORSHIP.pubKey
AND PROCEEDING.pubKey = INPROCEEDING.inproCrossRef
AND PERSON.personKey = AUTHORSHIP.personKey
AND PUBLICATION.pubYear = 2014
AND SUBSTRING_INDEX(SUBSTRING_INDEX(PROCEEDING.pubKey, 'conf/', -1), '/', 1) = 'sigmod'
GROUP BY personKey
HAVING COUNT(*) >= 2;

ALTER TABLE PUBLICATION DROP INDEX pubYear_index;

-- Question 4 a
SELECT CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) AS pubAuthor,
PVLDB.count AS pvldbCount,
SIGMOD.count AS sigmodCount
FROM
(
	SELECT COUNT(*) AS count, AUTHORSHIP.personKey AS personKey FROM PUBLICATION, AUTHORSHIP
	WHERE PUBLICATION.pubKey = AUTHORSHIP.pubKey
	AND PUBLICATION.pubKey LIKE "%pvldb%"
	GROUP BY AUTHORSHIP.personKey
) AS PVLDB,
(
	SELECT COUNT(*) AS count, AUTHORSHIP.personKey AS personKey FROM PUBLICATION, AUTHORSHIP
	WHERE PUBLICATION.pubKey = AUTHORSHIP.pubKey
	AND PUBLICATION.pubKey LIKE "%sigmod%"
	GROUP BY AUTHORSHIP.personKey
) AS SIGMOD,
PERSON
WHERE PERSON.personKey = PVLDB.personKey
AND PVLDB.personKey = SIGMOD.personKey
AND PVLDB.count >= 10
AND SIGMOD.count >= 10;

-- Question 4 b
SELECT CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) AS pubAuthor,
PVLDB.count AS pvldbCount,
KDD.count AS kddCount
FROM PERSON,
(
	SELECT COUNT(*) AS count, AUTHORSHIP.personKey AS personKey FROM PUBLICATION, AUTHORSHIP
	WHERE PUBLICATION.pubKey = AUTHORSHIP.pubKey
	AND PUBLICATION.pubKey LIKE "%pvldb%"
	GROUP BY AUTHORSHIP.personKey
) AS PVLDB LEFT JOIN
(
	SELECT COUNT(*) AS count, AUTHORSHIP.personKey AS personKey FROM PUBLICATION, AUTHORSHIP
	WHERE PUBLICATION.pubKey = AUTHORSHIP.pubKey
	AND PUBLICATION.pubKey LIKE "%kdd%"
	GROUP BY AUTHORSHIP.personKey
) AS KDD ON PVLDB.personKey = KDD.personKey
WHERE KDD.personKey IS NULL
AND PERSON.personKey = PVLDB.personKey
AND PVLDB.count >= 15;

-- Question 5
CREATE INDEX pubType_index ON PUBLICATION (pubType);

Select (FLOOR(pubYear/10) * 10) AS year, COUNT(*) AS count
from PUBLICATION
WHERE pubType = 'inproceedings'
AND FLOOR(pubYear/10) >=197
GROUP BY (FLOOR(pubYear/10) * 10);

ALTER TABLE PUBLICATION DROP INDEX pubType_index;


-- Question 6
SELECT CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) AS pubAuthor, Count(AUTHORSHIP.personKey) as pubCount
FROM PERSON,
(
	SELECT AUTHORSHIP.pubKey, COUNT(AUTHORSHIP.pubKey) AS authorCount
	FROM PUBLICATION, INPROCEEDING, AUTHORSHIP
	WHERE PUBLICATION.pubKey = INPROCEEDING.inproCrossref
	AND AUTHORSHIP.pubKey = INPROCEEDING.pubKey
	AND PUBLICATION.pubTitle COLLATE UTF8_GENERAL_CI REGEXP '[[:<:]]data[[:>:]]'
	GROUP BY INPROCEEDING.pubKey
	HAVING authorCount > 1) AS COLAB_PUB LEFT JOIN
	AUTHORSHIP USING(pubKey)
WHERE PERSON.personKey = AUTHORSHIP.personKey
GROUP BY AUTHORSHIP.personKey
ORDER BY Count(AUTHORSHIP.personKey) DESC;

-- Question 7
SELECT CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) AS pubAuthor, COUNT(AUTHORSHIP.personKey) AS pubCount
FROM PUBLICATION, INPROCEEDING, AUTHORSHIP, PERSON
WHERE PUBLICATION.pubKey = INPROCEEDING.inproCrossref
AND AUTHORSHIP.pubKey = INPROCEEDING.pubKey
AND PERSON.personKey = AUTHORSHIP.personKey
AND PUBLICATION.pubTitle COLLATE UTF8_GENERAL_CI REGEXP '[[:<:]]data[[:>:]]'
AND PUBLICATION.pubYear > YEAR(CURRENT_TIMESTAMP) - 5
GROUP BY AUTHORSHIP.personKey
ORDER BY Count(AUTHORSHIP.personKey) DESC LIMIT 10;

-- Question 8
SELECT conference, pubTitle, pubCount FROM (
	SELECT PROCEEDING.pubKey, COUNT(*) AS pubCount, SUBSTRING_INDEX(SUBSTRING_INDEX(PROCEEDING.pubKey, 'conf/', -1), '/', 1) AS conference
	FROM PROCEEDING, INPROCEEDING, PUBMONTH
	WHERE PROCEEDING.pubKey = INPROCEEDING.inproCrossRef
	AND PUBMONTH.pubMonth = "June"
	AND PUBMONTH.pubKey = PROCEEDING.pubKey
	AND proceedType = "conf"
	GROUP BY PROCEEDING.pubKey
) AS CONFERENCES
LEFT JOIN
PUBLICATION
USING (pubKey)
WHERE pubCount > 100;

-- Question 9 a
SELECT CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) AS pubAuthor, yearCount FROM
(SELECT personKey, COUNT(*) AS yearCount FROM
(SELECT DISTINCT personKey, pubYear FROM PUBLICATION
LEFT JOIN AUTHORSHIP USING (pubKey)
LEFT JOIN PERSON USING (personKey)
WHERE personLastName LIKE 'H%'
AND pubYear > 1988) AS p
GROUP BY personKey
HAVING yearCount = 30) AS i,
PERSON
WHERE PERSON.personKey = i.personKey;

-- Question 9 b
SELECT CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) AS pubAuthor,
COUNT(*) AS pubCount FROM
AUTHORSHIP, PUBLICATION, PERSON,
(SELECT DISTINCT AUTHORSHIP.personKey
FROM PUBLICATION, AUTHORSHIP WHERE
PUBLICATION.pubKey = AUTHORSHIP.pubKey
AND pubYear = (SELECT MIN(pubYear) FROM PUBLICATION)) AS oldAuthors
WHERE oldAuthors.personKey = PERSON.personKey
AND PERSON.personKey = AUTHORSHIP.personKey
AND AUTHORSHIP.pubKey = PUBLICATION.pubKey
GROUP BY AUTHORSHIP.personKey;

-- Question 10
-- Question: List down the TOP 10 publishers that publish the most publications
CREATE INDEX publisherName_index ON PUBLISHER (publisherName);

SELECT PUBLISHER.publisherName, COUNT(*) AS pubCount
FROM PUBLICATION, PUBLISHER
WHERE PUBLICATION.publisherId = PUBLISHER.publisherId
GROUP BY PUBLISHER.publisherName
ORDER BY pubCount DESC LIMIT 10;

ALTER TABLE PUBLISHER DROP INDEX publisherName_index;
