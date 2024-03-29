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
