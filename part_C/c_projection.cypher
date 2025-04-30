CALL gds.graph.project(
'citation-net',
['Paper'],
{
    CITES: {
    type: 'CITES',
    orientation: 'NATURAL'
    }
}
);