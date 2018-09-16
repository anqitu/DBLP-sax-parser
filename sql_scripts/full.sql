/* INIT */

-- DROP DATABASE dblpDB;

CREATE DATABASE IF NOT EXISTS dblpDB
CHARACTER SET utf8
COLLATE utf8_bin;

USE dblpDB;

DROP TABLE IF EXISTS PUB_SCHOOL;
DROP TABLE IF EXISTS CITERSHIP;
DROP TABLE IF EXISTS EDITORSHIP;
DROP TABLE IF EXISTS AUTHORSHIP;

DROP TABLE IF EXISTS WWW;
DROP TABLE IF EXISTS THESIS;
DROP TABLE IF EXISTS INCOLLECTION;
DROP TABLE IF EXISTS BOOK;
DROP TABLE IF EXISTS INPROCEEDING;
DROP TABLE IF EXISTS PROCEEDING;
DROP TABLE IF EXISTS ARTICLE;

DROP TABLE IF EXISTS PUBMONTH;
DROP TABLE IF EXISTS PUBLICATION;

DROP TABLE IF EXISTS PERSON;
DROP TABLE IF EXISTS ALIAS;
DROP TABLE IF EXISTS SCHOOL;
DROP TABLE IF EXISTS PUBLISHER;

/* ========================================================================= */
/* ACTORS                                                                    */
/* ========================================================================= */
CREATE TABLE PUBLISHER(
publisherId				INT     			AUTO_INCREMENT,
publisherName			VARCHAR(300)	    NOT NULL,

PRIMARY KEY (publisherId));

CREATE TABLE SCHOOL(
schoolId				INT     			AUTO_INCREMENT,
schoolName			    VARCHAR(300)	    NOT NULL,

PRIMARY KEY (schoolId));

CREATE TABLE PERSON(
personKey				VARCHAR(200)		,
personFullName			VARCHAR(100)	    ,
personFirstName			VARCHAR(100)	    ,
personLastName			VARCHAR(100)	    ,

PRIMARY KEY (personKey));

CREATE TABLE ALIAS(
aliasId					INT     			AUTO_INCREMENT,
personFullName			VARCHAR(100)	    ,
aliasFirstName			VARCHAR(100)	    ,
aliasLastName			VARCHAR(100)		,
personKey				VARCHAR(200)     	NOT NULL,

PRIMARY KEY (aliasId));


/* ========================================================================= */
/* Publications                                                              */
/* ========================================================================= */
CREATE TABLE PUBLICATION(
pubKey				VARCHAR(150)     		,
pubTitle			VARCHAR(1000)	    	NOT NULL,
pubYear				SMALLINT    			,
pubMdate	    	DATE					,
pubType            	VARCHAR(50)				,
publisherName		VARCHAR(300)		    ,

PRIMARY KEY (pubKey));

CREATE TABLE PUBMONTH(
pubKey					VARCHAR(150)		,
pubMonth				VARCHAR(20)			,

PRIMARY KEY (pubKey,pubMonth));

/* Sub Classes */

CREATE TABLE ARTICLE(
pubKey				VARCHAR(150)     		,
articleJournal		VARCHAR(200)	    	,
articleBooktitle	VARCHAR(400)	    	,
articleNumber		VARCHAR(50)    			,
articlePages		VARCHAR(100)    		,
articleVolume		VARCHAR(100)	    	,
articleCrossref		VARCHAR(200)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE PROCEEDING(
pubKey				VARCHAR(150)     		,
proceedAddress		VARCHAR(100)	    	,
proceedJournal		VARCHAR(200)	    	,
proceedBooktitle	VARCHAR(400)    		,
proceedNumber		VARCHAR(50)    			,
proceedPages		VARCHAR(100)	    	,
proceedSeries		VARCHAR(300)	    	,
proceedVolume		VARCHAR(100)	    	,
proceedType			VARCHAR(200)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE INPROCEEDING(
pubKey				VARCHAR(150)			,
inproBooktitle		VARCHAR(400)    		,
inproNumber			VARCHAR(50)    			,
inproPages			VARCHAR(100)	    	,
inproCrossref		VARCHAR(200)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE BOOK(
pubKey				VARCHAR(150)			,
bookBooktitle		VARCHAR(400)    		,
bookPages			VARCHAR(100)	    	,
bookSeries			VARCHAR(300)	    	,
bookVolume			VARCHAR(100)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE INCOLLECTION(
pubKey				VARCHAR(150)			,
incolChapter		SMALLINT    			,
incolBooktitle		VARCHAR(400)    		,
incolNumber			VARCHAR(50)    			,
incolPages			VARCHAR(100)	    	,
incolCrossref		VARCHAR(200)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE THESIS(
pubKey				VARCHAR(150)			,
thesisNumber		VARCHAR(50)    			,
thesisPages			VARCHAR(100)	    	,
thesisSeries		VARCHAR(300)	    	,
thesisVolume		VARCHAR(100)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE WWW(
pubKey				VARCHAR(150)			,
wwwBooktitle		VARCHAR(400)    		,

PRIMARY KEY (pubKey));


CREATE TABLE AUTHORSHIP(
pubKey				VARCHAR(150)     		,
personFullName		VARCHAR(100)	 		,

PRIMARY KEY (pubKey,personFullName));

CREATE TABLE EDITORSHIP(
pubKey				VARCHAR(150)     		,
personFullName		VARCHAR(100)	 		,

PRIMARY KEY (pubKey,personFullName));

CREATE TABLE CITERSHIP(
citingPubKey		VARCHAR(150)     		,
citedPubKey			VARCHAR(150)	 		,

PRIMARY KEY (citingPubKey,citedPubKey));

CREATE TABLE PUB_SCHOOL(
schoolName			VARCHAR(300)     		,
pubKey				VARCHAR(150)	 		,

PRIMARY KEY (schoolName,pubKey));


/* ========================================================================= */
/* Import Data                                                               */
/* ========================================================================= */

USE dblpDB;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/alias.csv'
INTO TABLE ALIAS
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(personFullName, personKey);

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/article.csv'
INTO TABLE ARTICLE
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/authorship.csv'
INTO TABLE AUTHORSHIP
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/book.csv'
INTO TABLE BOOK
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/citership.csv'
INTO TABLE CITERSHIP
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/editorship.csv'
INTO TABLE EDITORSHIP
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/incollection.csv'
INTO TABLE INCOLLECTION
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/inproceeding.csv'
INTO TABLE INPROCEEDING
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;


LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/person.csv'
INTO TABLE PERSON
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/proceeding.csv'
INTO TABLE PROCEEDING
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/pub_school.csv'
INTO TABLE PUB_SCHOOL
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/publication.csv'
INTO TABLE PUBLICATION
CHARACTER SET latin1
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/pubmonth.csv'
INTO TABLE PUBMONTH
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/thesis.csv'
INTO TABLE THESIS
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/www.csv'
INTO TABLE WWW
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;


/* ========================================================================= */
/* Alter Tables                                                              */
/* ========================================================================= */


CREATE TABLE TEMP_PERSON(
personKey			VARCHAR(150)     		,
personFullName		VARCHAR(100)	 		,

PRIMARY KEY (personKey,personFullName));

INSERT INTO TEMP_PERSON(personFullName, personKey)
SELECT personFullName, personKey FROM ALIAS
UNION
SELECT personFullName, personKey FROM PERSON;

CREATE INDEX idx_helper ON AUTHORSHIP(personFullName);
CREATE INDEX idx_helper ON EDITORSHIP(personFullName);
CREATE INDEX idx_helper ON TEMP_PERSON(personFullName);

CREATE TABLE TEMP_AUTHORSHIP AS
SELECT
*
FROM AUTHORSHIP
LEFT JOIN TEMP_PERSON
USING(personFullName);

DROP TABLE AUTHORSHIP;

CREATE INDEX idx_helper1 ON TEMP_AUTHORSHIP(pubKey);
CREATE INDEX idx_helper2 ON TEMP_AUTHORSHIP(personKey);

CREATE TABLE AUTHORSHIP(
pubKey				VARCHAR(150)     		,
personKey		   VARCHAR(200)	 		,

PRIMARY KEY (pubKey,personKey));

INSERT IGNORE INTO AUTHORSHIP SELECT pubKey, personKey FROM TEMP_AUTHORSHIP;
DROP TABLE TEMP_AUTHORSHIP;

CREATE TABLE TEMP_EDITORSHIP AS
SELECT
*
FROM EDITORSHIP
LEFT JOIN TEMP_PERSON
USING(personFullName);

DROP TABLE EDITORSHIP;

CREATE TABLE EDITORSHIP LIKE TEMP_EDITORSHIP;
ALTER TABLE EDITORSHIP DROP personFullName;
ALTER TABLE EDITORSHIP ADD PRIMARY KEY (pubKey, personKey);
INSERT IGNORE INTO EDITORSHIP SELECT pubKey, personKey FROM TEMP_EDITORSHIP;

DROP TABLE TEMP_EDITORSHIP;
DROP TABLE TEMP_PERSON;

UPDATE PERSON SET personFullName = SUBSTRING_INDEX(personFullName,' 0', 1) WHERE personFullName LIKE '%0%';
UPDATE PERSON SET personLastName = SUBSTRING_INDEX(personFullName,' ', -1)
WHERE INSTR(personFullName, ' ') <> 0;
UPDATE PERSON SET personFirstName = SUBSTRING_INDEX(personFullName, personLastName, 1);
UPDATE PERSON SET personFirstName = SUBSTRING_INDEX(personFirstName, ' ', 1);
UPDATE PERSON SET personFirstName = personFullName WHERE personLastName IS NULL;

ALTER TABLE PERSON DROP personFullName;

UPDATE ALIAS SET personFullName = SUBSTRING_INDEX(personFullName,' 0', 1) WHERE personFullName LIKE '%0%';
UPDATE ALIAS SET aliasLastName = SUBSTRING_INDEX(personFullName,' ', -1)
WHERE INSTR(personFullName, ' ') <> 0;
UPDATE ALIAS SET aliasFirstName = SUBSTRING_INDEX(personFullName, aliasLastName, 1);
UPDATE ALIAS SET aliasFirstName = SUBSTRING_INDEX(aliasFirstName, ' ', 1);
UPDATE ALIAS SET aliasFirstName = personFullName WHERE aliasLastName IS NULL;

ALTER TABLE ALIAS DROP personFullName;

CREATE INDEX idx_helper ON SCHOOL(schoolName);
CREATE INDEX idx_helper ON PUB_SCHOOL(schoolName);

INSERT INTO SCHOOL (schoolName)
SELECT DISTINCT schoolName
FROM PUB_SCHOOL;

CREATE TABLE TEMP_PUB_SCHOOL AS
SELECT
*
FROM PUB_SCHOOL
LEFT JOIN SCHOOL
USING(schoolName);

DROP TABLE PUB_SCHOOL;

CREATE TABLE PUB_SCHOOL AS
SELECT pubKey, schoolId
FROM TEMP_PUB_SCHOOL;

DROP TABLE TEMP_PUB_SCHOOL;

INSERT INTO PUBLISHER (publisherName)
SELECT DISTINCT publisherName
FROM PUBLICATION
WHERE publisherName != '';

CREATE INDEX idx_helper ON PUBLICATION(publisherName);
CREATE INDEX idx_helper ON PUBLISHER(publisherName);

CREATE TABLE TEMP_PUBLICATION AS
SELECT
*
FROM PUBLICATION
LEFT JOIN PUBLISHER
USING(publisherName);

DROP TABLE PUBLICATION;

CREATE TABLE PUBLICATION AS
SELECT *
FROM TEMP_PUBLICATION;

ALTER TABLE PUBLICATION DROP publisherName;

DROP TABLE TEMP_PUBLICATION;

ALTER TABLE PUBLISHER DROP INDEX idx_helper;
ALTER TABLE SCHOOL DROP INDEX idx_helper;


/* ========================================================================= */
/* Set Constraints                                                           */
/* ========================================================================= */

ALTER TABLE ALIAS
ADD FOREIGN KEY (personKey) REFERENCES PERSON(personKey),
MODIFY COLUMN aliasFirstName VARCHAR(100) NOT NULL;

ALTER TABLE PUBLICATION
ADD PRIMARY KEY(pubKey),
ADD FOREIGN KEY (publisherId) REFERENCES PUBLISHER(publisherId);

ALTER TABLE PUBMONTH
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey);

ALTER TABLE ARTICLE
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
ADD FOREIGN KEY (articleCrossref) REFERENCES PUBLICATION(pubKey);

ALTER TABLE PROCEEDING
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey);

ALTER TABLE INPROCEEDING
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
ADD FOREIGN KEY (inproCrossref) REFERENCES PUBLICATION(pubKey);

ALTER TABLE BOOK
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey);

ALTER TABLE INCOLLECTION
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
ADD FOREIGN KEY (incolCrossref) REFERENCES PUBLICATION(pubKey);

ALTER TABLE THESIS
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey);

ALTER TABLE WWW
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey);

ALTER TABLE PUB_SCHOOL
ADD PRIMARY KEY(schoolId, pubKey),
ADD FOREIGN KEY (schoolId) REFERENCES SCHOOL(schoolId),
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey);

ALTER TABLE EDITORSHIP
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
ADD FOREIGN KEY (personKey) REFERENCES PERSON(personKey);

ALTER TABLE AUTHORSHIP
ADD FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
ADD FOREIGN KEY (personKey) REFERENCES PERSON(personKey);


DELETE FROM CITERSHIP
WHERE citedPubKey = '...';
DELETE FROM CITERSHIP
WHERE citedPubKey = '';
DELETE FROM CITERSHIP
WHERE citedPubKey = 'persons/Ley93';

ALTER TABLE CITERSHIP
ADD FOREIGN KEY (citingPubKey) REFERENCES PUBLICATION(pubKey),
ADD FOREIGN KEY (citedPubKey) REFERENCES PUBLICATION(pubKey);
