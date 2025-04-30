// find those authors that published in a conference edition of the type conference
MATCH (conf:Conference)-[:HAS_EDITION_C]->(ed:ConferenceEdition),
(ed)<-[:PUBLISHED_IN_C]-(p:Paper)<-[:AUTHORED]-(a:Author)
// Group by conference name and author name, 
// and count the number of editions the author appeared in the same conference
WITH 
    conf.name          AS conference,
    a.name             AS author,
COUNT(DISTINCT ed.name) AS editionsCount
// Keep only those authors that published in at least 4 editions of the same conf
WHERE editionsCount >= 4
RETURN conference, author, editionsCount
ORDER BY conference, editionsCount DESC;