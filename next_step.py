from py2neo import Graph,Node, Relationship
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
conceptofdecision=[]
decisionlist=[]
commonconcept=[]
for i in decisionlist:
    data=graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) where a.name='"+i+"' return d.name").data()
    datatemp=[]
    for i in data:
        for k,v in i.items():
            if(v in commonconcept):
                datatemp.append(v)
    conceptofdecision.append(datatemp)
concepthavebeeneused=[]
conceptnotbeenused=[]
for i in conceptofdecision[0]:
    if(i not in concepthavebeeneused):
        conceptnotbeenused.append(i)
