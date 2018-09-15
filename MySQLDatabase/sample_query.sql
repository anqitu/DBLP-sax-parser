LOAD DATA LOCAL INFILE '/Users/anqitu/Workspaces/NTU/CZ4031/CZ4031-Project1-Querying-Databases-Efficiently/DBLP-sax-parser/csv/alias.csv'
INTO TABLE `ALIAS`
FIELDS TERMINATED BY '|'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(personKey, personFullName)

DELETE FROM PUBLISHER

INSERT INTO PUBLICATION
VALUES ('aaaab', 'abc', '1999', '1999-10-05', 'article', 'ackg');



INSERT INTO PERSON (`personKey`, `personFullName`)
VALUES ('personA', 'Anqi Tu');
INSERT INTO PERSON (`personKey`, `personFullName`)
VALUES ('personB', 'Clarence');
INSERT INTO PERSON (`personKey`, `personFullName`)
VALUES ('personC', 'Clarence Fitzgerald Castillo');

UPDATE PERSON SET `personLastName` = SUBSTRING_INDEX(personFullName,' ', -1) WHERE INSTR(personFullName, ' ') <> 0;
UPDATE PERSON SET `personFirstName` = SUBSTRING_INDEX(personFullName, personLastName, 1);
UPDATE PERSON SET `personFirstName` = personFullName WHERE personLastName IS NULL;



INSERT INTO PUBLISHER (publisherName)
SELECT DISTINCT publisherName
FROM PUBLICATION


CREATE TABLE TEMP_PUB_PUBLISHERNAME AS
    SELECT
        *
    FROM PUBLICATION
    LEFT JOIN PUBLISHER USING(publisherName);

DROP TABLE PUBLICATION
