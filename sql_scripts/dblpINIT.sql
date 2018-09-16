/* INIT */
/* DROP DATABASE dblpDB */

CREATE DATABASE IF NOT EXISTS dblpDB;

use dblpDB;

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
personFirstName			VARCHAR(100)	    NOT NULL,
personLastName			VARCHAR(100)		,

PRIMARY KEY (personKey));

CREATE TABLE ALIAS(
aliasId					INT     			AUTO_INCREMENT,
aliasFirstName			VARCHAR(100)	    NOT NULL,
aliasLastName			VARCHAR(100)		,
personKey				VARCHAR(200)     	NOT NULL,

PRIMARY KEY (aliasId),
FOREIGN KEY (personKey) REFERENCES PERSON(personKey));


/* ========================================================================= */
/* Publications                                                              */
/* ========================================================================= */
CREATE TABLE PUBLICATION(
pubKey				VARCHAR(200)     		,
pubTitle			VARCHAR(1000)	    	NOT NULL,
pubYear				SMALLINT    			,
pubMdate	    	TINYINT					,
pubType            	VARCHAR(50)				,
publisherId			INT						,

PRIMARY KEY (pubKey),
FOREIGN KEY (publisherId) REFERENCES PUBLISHER(publisherId));

CREATE TABLE PUBMONTH(
pubKey					VARCHAR(200)		,
pubMonth				VARCHAR(50)			,

PRIMARY KEY (pubKey,pubMonth),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));

/* Sub Classes */

CREATE TABLE ARTICLE(
pubKey				VARCHAR(200)     		,
articleJournal		VARCHAR(200)	    	,
articleBooktitle	VARCHAR(400)	    	,
articleNumber		INT    					,
articlePages		INT    					,
articleVolume		VARCHAR(100)	    	,
articleCrossRef		VARCHAR(200)	    	,


PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
FOREIGN KEY (articleCrossRef) REFERENCES PUBLICATION(pubKey));

CREATE TABLE PROCEEDING(
pubKey				VARCHAR(200)     		,
proceedAddress		VARCHAR(100)	    	,
proceedJournal		VARCHAR(200)	    	,
proceedBooktitle	VARCHAR(400)    		,
proceedNumber		INT    					,
proceedPages		VARCHAR(100)	    	,
proceedSeries		VARCHAR(300)	    	,
proceedVolume		VARCHAR(100)	    	,
proceedType			VARCHAR(200)	    	,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));

CREATE TABLE INPROCEEDING(
pubKey				VARCHAR(150)			,
inproBooktitle		VARCHAR(400)    		,
inproNumber			INT    					,
inproPages			VARCHAR(100)	    	,
inproCrossRef		VARCHAR(200)	    	,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
FOREIGN KEY (inproCrossRef) REFERENCES PUBLICATION(pubKey));

CREATE TABLE BOOK(
pubKey				VARCHAR(150)			,
bookBooktitle		VARCHAR(400)    		,
bookPages			VARCHAR(100)	    	,
bookSeries			VARCHAR(300)	    	,
bookVolume			VARCHAR(100)	    	,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));

CREATE TABLE INCOLLECTION(
pubKey				VARCHAR(150)			,
incolChapter		SMALLINT    			,
incolBooktitle		VARCHAR(400)    		,
incolNumber			INT    					,
incolPages			VARCHAR(100)	    	,
incolCrossRef		VARCHAR(200)	    	,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
FOREIGN KEY (incolCrossRef) REFERENCES PUBLICATION(pubKey));

CREATE TABLE THESIS(
pubKey				VARCHAR(150)			,
thesisNumber		INT    					,
thesisPages			VARCHAR(100)	    	,
thesisSeries		VARCHAR(300)	    	,
thesisVolume		VARCHAR(100)	    	,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));

CREATE TABLE WWW(
pubKey				VARCHAR(150)			,
wwwBooktitle		VARCHAR(400)    		,

PRIMARY KEY (pubKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));


/* ========================================================================= */
/* Associative Tables                                                        */
/* ========================================================================= */

CREATE TABLE AUTHORSHIP(
pubKey				VARCHAR(200)     		,
personKey			VARCHAR(200)	 		,

PRIMARY KEY (pubKey,personKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
FOREIGN KEY (personKey) REFERENCES PERSON(personKey));

CREATE TABLE EDITORSHIP(
pubKey				VARCHAR(200)     		,
personKey			VARCHAR(200)	 		,

PRIMARY KEY (pubKey,personKey),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey),
FOREIGN KEY (personKey) REFERENCES PERSON(personKey));

CREATE TABLE CITERSHIP(
citingPubKey		VARCHAR(200)     		,
citedPubKey			VARCHAR(200)	 		,

PRIMARY KEY (citingPubKey,citedPubKey),
FOREIGN KEY (citingPubKey) REFERENCES PUBLICATION(pubKey),
FOREIGN KEY (citedPubKey) REFERENCES PUBLICATION(pubKey));

CREATE TABLE PUB_SCHOOL(
schoolId			INT     				,
pubKey				VARCHAR(200)	 		,

PRIMARY KEY (schoolId,pubKey),
FOREIGN KEY (schoolId) REFERENCES SCHOOL(schoolId),
FOREIGN KEY (pubKey) REFERENCES PUBLICATION(pubKey));
