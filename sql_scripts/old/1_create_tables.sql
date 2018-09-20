/* INIT */

DROP DATABASE dblpDB;

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
publisherName		VARCHAR(300)		,

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
articleNumber		VARCHAR(50)    					,
articlePages		VARCHAR(100)    			,
articleVolume		VARCHAR(100)	    	,
articleCrossref		VARCHAR(200)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE PROCEEDING(
pubKey				VARCHAR(150)     		,
proceedAddress		VARCHAR(100)	    	,
proceedJournal		VARCHAR(200)	    	,
proceedBooktitle	VARCHAR(400)    		,
proceedNumber		VARCHAR(50)    					,
proceedPages		VARCHAR(100)	    	,
proceedSeries		VARCHAR(300)	    	,
proceedVolume		VARCHAR(100)	    	,
proceedType			VARCHAR(200)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE INPROCEEDING(
pubKey				VARCHAR(150)			,
inproBooktitle		VARCHAR(400)    		,
inproNumber			VARCHAR(50)    					,
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
incolNumber			VARCHAR(50)    					,
incolPages			VARCHAR(100)	    	,
incolCrossref		VARCHAR(200)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE THESIS(
pubKey				VARCHAR(150)			,
thesisNumber		VARCHAR(50)    					,
thesisPages			VARCHAR(100)	    	,
thesisSeries		VARCHAR(300)	    	,
thesisVolume		VARCHAR(100)	    	,

PRIMARY KEY (pubKey));

CREATE TABLE WWW(
pubKey				VARCHAR(150)			,
wwwBooktitle		VARCHAR(400)    		,

PRIMARY KEY (pubKey));


/* ========================================================================= */
/* Associative Tables                                                        */
/* ========================================================================= */

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
schoolName			VARCHAR(300)     				,
pubKey				VARCHAR(150)	 		,

PRIMARY KEY (schoolName,pubKey));
