/////////////
// 1. Constraints and indexes
/////////////

CREATE CONSTRAINT paper_id_unique IF NOT EXISTS
  FOR (p:Paper) REQUIRE p.paper_id IS UNIQUE;

CREATE CONSTRAINT author_id_unique IF NOT EXISTS
  FOR (a:Author) REQUIRE a.author_id IS UNIQUE;

CREATE CONSTRAINT keyword_unique IF NOT EXISTS
  FOR (k:Keyword) REQUIRE k.keyword IS UNIQUE;

CREATE CONSTRAINT conference_id_unique IF NOT EXISTS
  FOR (c:Conference) REQUIRE c.conf_id IS UNIQUE;

CREATE CONSTRAINT conference_edition_node_key IF NOT EXISTS
  FOR (e:ConferenceEdition) REQUIRE (e.conf_id, e.year) IS NODE KEY;

CREATE CONSTRAINT journal_id_unique IF NOT EXISTS
  FOR (j:Journal) REQUIRE j.journal_id IS UNIQUE;

CREATE CONSTRAINT journal_volume_node_key IF NOT EXISTS
  FOR (v:JournalVolume) REQUIRE (v.journal_id, v.volume_number, v.year) IS NODE KEY;

CREATE CONSTRAINT venue_id_unique IF NOT EXISTS
  FOR (v:Venue) REQUIRE v.venue_id IS UNIQUE;

CREATE CONSTRAINT review_id_unique IF NOT EXISTS
  FOR (r:Review) REQUIRE r.review_id IS UNIQUE;



/////////////
// 2. Nodes
/////////////

// 2.1 Authors
LOAD CSV WITH HEADERS FROM 'file:///csv/authors.csv' AS row
MERGE (a:Author { author_id: row.author_id })
  SET a.full_name        = row.full_name,
      a.country_of_birth = row.country_of_birth,
      a.date_of_birth    = date(row.date_of_birth),
      a.is_phd           = toBoolean(row.is_phd);

// 2.2 Papers
LOAD CSV WITH HEADERS FROM 'file:///csv/papers.csv' AS row
MERGE (p:Paper { paper_id: row.paper_id })
  SET p.title    = row.title,
      p.year     = toInteger(row.year),
      p.pages    = row.pages,
      p.abstract = row.abstract;

// 2.3 Keywords
LOAD CSV WITH HEADERS FROM 'file:///csv/keywords.csv' AS row
MERGE (k:Keyword { keyword: row.keyword });

// 2.4 Conferences
LOAD CSV WITH HEADERS FROM 'file:///csv/conferences.csv' AS row
MERGE (c:Conference { conf_id: row.conf_id })
  SET c.name = row.name,
      c.type = row.type;

// 2.5 Conference Editions
LOAD CSV WITH HEADERS FROM 'file:///csv/conference_editions.csv' AS row
MERGE (e:ConferenceEdition { edition_id: row.edition_id })
  SET e.conf_id    = row.conf_id,
      e.year       = toInteger(row.year),
      e.start_date = date(row.start_date),
      e.end_date   = date(row.end_date);

// 2.6 Venues
LOAD CSV WITH HEADERS FROM 'file:///csv/venues.csv' AS row
MERGE (v:Venue { venue_id: row.venue_id })
  SET v.city    = row.city,
      v.country = row.country;

// 2.7 Journals
LOAD CSV WITH HEADERS FROM 'file:///csv/journals.csv' AS row
MERGE (j:Journal { journal_id: row.journal_id })
  SET j.name = row.name;

// 2.8 Journal Volumes
LOAD CSV WITH HEADERS FROM 'file:///csv/journal_volumes.csv' AS row
MERGE (vol:JournalVolume { volume_id: row.volume_id })
  SET vol.journal_id    = row.journal_id,
      vol.volume_number = toInteger(row.volume_number),
      vol.year          = toInteger(row.year);

// 2.9 Reviews
LOAD CSV WITH HEADERS FROM 'file:///csv/reviews.csv' AS row
MERGE (r:Review { review_id: row.review_id })
  SET r.review_text = row.review_text,
      r.score       = toInteger(row.score),
      r.date        = date(row.date);


/////////////
// 3. Relationships
/////////////

// 3.1 Authorship
LOAD CSV WITH HEADERS FROM 'file:///csv/authorship.csv' AS row
MATCH (a:Author {author_id: row.author_id}), (p:Paper {paper_id: row.paper_id})
MERGE (a)-[:AUTHORED {isCorresponding: toBoolean(row.is_corresponding)}]->(p);

// 3.2 Paper–Keyword
LOAD CSV WITH HEADERS FROM 'file:///csv/paper_keywords.csv' AS row
MATCH (p:Paper {paper_id: row.paper_id}), (k:Keyword {keyword: row.keyword})
MERGE (p)-[:HAS_KEYWORD]->(k);

// 3.3 Citations
LOAD CSV WITH HEADERS FROM 'file:///csv/paper_cites.csv' AS row
MATCH (p1:Paper {paper_id: row.citing_paper_id}), (p2:Paper {paper_id: row.cited_paper_id})
MERGE (p1)-[:CITES]->(p2);

// 3.4 Paper in Conference
LOAD CSV WITH HEADERS FROM 'file:///csv/paper_in_conference.csv' AS row
MATCH (p:Paper {paper_id: row.paper_id}), (e:ConferenceEdition {edition_id: row.edition_id})
MERGE (p)-[:PUBLISHED_IN]->(e);

// 3.5 Paper in Journal
LOAD CSV WITH HEADERS FROM 'file:///csv/paper_in_journal.csv' AS row
MATCH (p:Paper {paper_id: row.paper_id}), (v:JournalVolume {volume_id: row.volume_id})
MERGE (p)-[:PUBLISHED_IN]->(v);

// 3.6 Conference → Edition
LOAD CSV WITH HEADERS FROM 'file:///csv/conference_has_edition.csv' AS row
MATCH (c:Conference {conf_id: row.conf_id}), (e:ConferenceEdition {edition_id: row.edition_id})
MERGE (c)-[:HAS_EDITION]->(e);

// 3.7 Edition → Venue
LOAD CSV WITH HEADERS FROM 'file:///csv/edition_held_at.csv' AS row
MATCH (e:ConferenceEdition {edition_id: row.edition_id}), (v:Venue {venue_id: row.venue_id})
MERGE (e)-[:HELD_AT]->(v);

// 3.8 Journal → Volume
LOAD CSV WITH HEADERS FROM 'file:///csv/journal_has_volume.csv' AS row
MATCH (j:Journal {journal_id: row.journal_id}), (vol:JournalVolume {volume_id: row.volume_id})
MERGE (j)-[:HAS_VOLUME]->(vol);

// 3.9 Review Assignments
LOAD CSV WITH HEADERS FROM 'file:///csv/review_assignments.csv' AS row
MATCH (a:Author {author_id: row.reviewer_id}), 
      (r:Review {review_id: row.review_id}), 
      (p:Paper {paper_id: row.paper_id})
MERGE (a)-[:REVIEWED]->(r)
MERGE (r)-[:OF]->(p);
