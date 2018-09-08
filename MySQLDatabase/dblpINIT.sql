/* INIT */
CREATE DATABASE IF NOT EXISTS dblpDB;

DROP TABLE IF EXISTS INCOLLECTION;
DROP TABLE IF EXISTS BOOK;
DROP TABLE IF EXISTS INPROCEEDING;
DROP TABLE IF EXISTS PROCEEDING;
DROP TABLE IF EXISTS ARTICLE;
DROP TABLE IF EXISTS EDITORSHIP;
DROP TABLE IF EXISTS AUTHORSHIP;
DROP TABLE IF EXISTS PUBLICATION;
DROP TABLE IF EXISTS PERSON;
DROP TABLE IF EXISTS ALIAS;
DROP TABLE IF EXISTS PUBLISHER;
USE dblpDB;

/* Persons */
CREATE TABLE PUBLISHER(
publisherId				INT     			AUTO_INCREMENT,
publisherName			VARCHAR(250)	    NOT NULL,

PRIMARY KEY (publisherId));

CREATE TABLE ALIAS(
aliasId					INT     			AUTO_INCREMENT,
aliasFirstName			VARCHAR(100)	    NOT NULL,
aliasLastName			VARCHAR(100)	    NOT NULL,

PRIMARY KEY (aliasId));

CREATE TABLE PERSON(
personId				INT     			AUTO_INCREMENT,
personKey				VARCHAR(150)		,
primaryAliasId			INT	    			,

CONSTRAINT UNIQUE (personKey),
PRIMARY KEY (personId),
FOREIGN KEY (primaryAliasId) REFERENCES ALIAS(aliasId));

/* Publications */
CREATE TABLE PUBLICATION(
pubKey				VARCHAR(150)     		,
pubTitle			VARCHAR(1000)	    	NOT NULL,
pubYear				SMALLINT    			,
pubMonth	    	TINYINT					,
pubType            	VARCHAR(50)				,
pubCrossRef			VARCHAR(150)			,
publisherId			INT						,

PRIMARY KEY (pubKey),
FOREIGN KEY (publisherId) REFERENCES PUBLISHER(publisherId),
FOREIGN KEY (pubCrossRef) REFERENCES PUBLICATION(pubKey));

/* Associative Tables */
CREATE TABLE AUTHORSHIP(
pubKey				VARCHAR(150)     		,
personId			INT	 					,

PRIMARY KEY (pubKey,personId),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
FOREIGN KEY (personId) REFERENCES PERSON(personId));

CREATE TABLE EDITORSHIP(
pubKey				VARCHAR(150)     		,
personId			INT	 					,

PRIMARY KEY (pubKey,personId),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
FOREIGN KEY (personId) REFERENCES PERSON(personId));

/* Sub Classes */

CREATE TABLE ARTICLE(
pubKey				VARCHAR(150)     		,
articleVolume		VARCHAR(100)	    	,
articleNumber		INT    					,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));

CREATE TABLE PROCEEDING(
pubKey				VARCHAR(150)     		,
proceedVolume		VARCHAR(100)	    	,
proceedSeries		VARCHAR(200)    		,
proceedISBN			CHAR(18)				,

CONSTRAINT UNIQUE (proceedISBN),
PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));

CREATE TABLE INPROCEEDING(
pubKey				VARCHAR(150)			,
inproPages			VARCHAR(20)	    		,
inproNumber			INT    					,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));

CREATE TABLE BOOK(
pubKey				VARCHAR(150)			,
bookTitle			VARCHAR(500)	    	,
bookSeries			VARCHAR(200)			,
bookISBN			CHAR(18)				,

CONSTRAINT UNIQUE (bookISBN),
PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));

CREATE TABLE INCOLLECTION(
pubKey				VARCHAR(150)			,
collectTitle		VARCHAR(500)	    	,
collectPages		VARCHAR(20)				,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));