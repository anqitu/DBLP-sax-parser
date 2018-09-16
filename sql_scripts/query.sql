-- Question 1
SELECT pubType, COUNT(*) FROM PUBLICATION
WHERE pubYear >= 2000 AND pubYear <= 2017
GROUP BY pubType;

-- Question 2
SELECT conference, MAX(pubCount) AS pubCount FROM (
	SELECT PROCEEDING.pubKey as `pubKey`, COUNT(*) AS pubCount, SUBSTRING_INDEX(SUBSTRING_INDEX(PROCEEDING.pubKey, 'conf/', -1), '/', 1) AS conference
	FROM PROCEEDING, INPROCEEDING, PUBMONTH
	WHERE proceedType = "conf"
	AND PROCEEDING.pubKey = INPROCEEDING.inproCrossRef
	AND PUBMONTH.pubMonth = "July" AND PUBMONTH.pubKey = PROCEEDING.pubKey
	GROUP BY PROCEEDING.pubKey
) AS CONFERENCES
WHERE pubCount > 200
GROUP BY conference

-- Question 3 a
-- X(author) = "Mohamed-Slim Alouini"
SELECT PUBLICATION.pubKey, pubTitle, pubYear, pubMdate, pubType, publisherId, CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) as pubAuthor
FROM PUBLICATION, AUTHORSHIP, PERSON
WHERE PUBLICATION.pubKey = AUTHORSHIP.pubKey
AND AUTHORSHIP.personKey = PERSON.personKey
AND PUBLICATION.pubYear = 2015
AND PERSON.personFirstName = "Mohamed-Slim" AND PERSON.personLastName = "Alouini";

-- Question 3 b
-- X(author) = "Mohamed-Slim Alouini", Y(year) = 2015, Z(conference) = 'icc'
SELECT * FROM (
	SELECT INPROCEEDING.pubKey, pubTitle, pubYear, pubMdate, pubType, publisherId,
	CONCAT(PERSON.personFirstName, " ", PERSON.personLastName) as pubAuthor,
	SUBSTRING_INDEX(SUBSTRING_INDEX(PROCEEDING.pubKey, 'conf/', -1), '/', 1) AS conference
	FROM INPROCEEDING, AUTHORSHIP, PERSON, PROCEEDING, PUBLICATION
	WHERE INPROCEEDING.pubKey = PUBLICATION.pubKey
	AND INPROCEEDING.pubKey = AUTHORSHIP.pubKey
	AND AUTHORSHIP.personKey = PERSON.personKey
	AND PROCEEDING.pubKey = INPROCEEDING.inproCrossRef
	AND PERSON.personFirstName = "Mohamed-Slim" AND PERSON.personLastName = "Alouini"
	AND PUBLICATION.pubYear = 2015
) AS AUTHOR_PUBLICATIONS
WHERE conference = "icc";
