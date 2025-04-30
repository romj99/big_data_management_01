// Match papers published in conferences
MATCH (conf:Conference)-[:HAS_EDITION_C]->(ed:ConferenceEdition)<-[:PUBLISHED_IN_C]-(p:Paper)
// Match papers that are cited
MATCH (p)<-[c:CITES]-()
// Count citations grouping by paper and conference
WITH conf.name AS confName, p, count(c) AS citationCount
// Order by conference and citation descending, keeping most cited papers first
ORDER BY confName, citationCount DESC
// Keep only the top 3 most cited papers per conference
WITH confName, collect({paper: p, citations: citationCount})[0..3] AS top3
// Ungroup the top 3 papers to return them in separate rows
UNWIND top3 AS entry
// Return the conference ID, paper title, and citation count
RETURN
    confName       AS Conference,
    entry.paper.title  AS Paper,
    entry.citations    AS CitationCount
// Order by conference and citation count descending
ORDER BY CitationCount DESC, Conference;