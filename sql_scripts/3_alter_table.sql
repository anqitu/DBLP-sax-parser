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

CREATE TABLE AUTHORSHIP AS
    SELECT
        personKey, pubKey
    FROM TEMP_AUTHORSHIP
    WHERE personKey IS NOT NULL;

DROP TABLE TEMP_AUTHORSHIP;

CREATE TABLE TEMP_EDITORSHIP AS
SELECT
*
FROM EDITORSHIP
LEFT JOIN TEMP_PERSON
USING(personFullName);

DROP TABLE EDITORSHIP;

CREATE TABLE EDITORSHIP AS
SELECT personKey, pubKey
FROM TEMP_EDITORSHIP
WHERE personKey IS NOT NULL;

ALTER TABLE EDITORSHIP
ADD PRIMARY KEY (personKey, pubKey);

DROP TABLE TEMP_EDITORSHIP;
DROP TABLE TEMP_PERSON;

UPDATE PERSON SET personFullName = SUBSTRING_INDEX(personFullName,' 0', 1) WHERE personFullName LIKE '%0%';
UPDATE PERSON SET personLastName = SUBSTRING_INDEX(personFullName,' ', -1)
WHERE INSTR(personFullName, ' ') <> 0;
UPDATE PERSON SET personFirstName = SUBSTRING_INDEX(personFullName, personLastName, 1);
UPDATE PERSON SET personFirstName = personFullName WHERE personLastName IS NULL;

ALTER TABLE PERSON DROP personFullName;

UPDATE ALIAS SET personFullName = SUBSTRING_INDEX(personFullName,' 0', 1) WHERE personFullName LIKE '%0%';
UPDATE ALIAS SET aliasLastName = SUBSTRING_INDEX(personFullName,' ', -1)
WHERE INSTR(personFullName, ' ') <> 0;
UPDATE ALIAS SET aliasFirstName = SUBSTRING_INDEX(personFullName, aliasLastName, 1);
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
