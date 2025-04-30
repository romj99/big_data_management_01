// Calculate per‑paper citation counts
MATCH (a:Author)-[:AUTHORED]->(p:Paper)
OPTIONAL MATCH (p)<-[:CITES]-()
WITH a, p, count(*) AS citations

// Get all that author's citation counts into a list
WITH a, collect(citations) AS citationList

// Order the list in ascending order by using a custom method
UNWIND citationList AS citationCount
WITH a, citationCount
ORDER BY citationCount ASC

// Reverse the list (ascending order to descending order)
WITH a, collect(citationCount) AS sortedList

// Unwind positions and keep only those where citationCount >= rank
UNWIND range(0, size(sortedList)-1) AS idx
WITH a, idx + 1 AS h, sortedList[idx] AS citationCount
WHERE citationCount >= h

// The h‑index is the maximum valid h, defaulting to 0 if none
RETURN a.name AS Author, coalesce(max(h), 0) AS HIndex
ORDER BY HIndex DESC, Author;