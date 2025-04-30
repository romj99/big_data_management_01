CALL gds.pageRank.stream(
    'citation-net',
    {
        maxIterations: 50,
        dampingFactor: 0.85
    }
    )
    YIELD nodeId, score

    WITH gds.util.asNode(nodeId) AS paper, score

    RETURN 
    paper.title AS title,
    paper.year AS year,
    paper.pages AS pages,
    paper.url AS url,
    paper.DOI AS DOI,
    score AS score
    ORDER BY score DESC
    LIMIT 8;