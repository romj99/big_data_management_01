// Gather, per journal, all papers published in 2022 or 2023
MATCH (j:Journal)-[:HAS_VOLUME]->(vol:JournalVolume)<-[:PUBLISHED_IN_J]-(p:Paper)
WHERE vol.year IN [2022, 2023]
WITH j, collect(p) AS prevPapers, size(collect(p)) AS numPrevPapers

// Count incoming citations in 2024 to any of those papers
UNWIND prevPapers AS oldPaper
MATCH (citing:Paper)-[:CITES]->(oldPaper)
WHERE citing.year = 2024
WITH j, numPrevPapers, count(citing) AS numCitations

// Compute impact factor, guard against division by zero
RETURN
j.name            AS Journal,
numCitations      AS Citations2024,
numPrevPapers     AS Papers2022_23,
CASE
    WHEN numPrevPapers > 0
    THEN toFloat(numCitations) / numPrevPapers
    ELSE NULL
END               AS ImpactFactor2024
ORDER BY ImpactFactor2024 DESC;