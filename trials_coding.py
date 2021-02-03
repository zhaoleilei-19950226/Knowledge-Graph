from py2neo import Graph
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
def commoncept_get():
    data_1 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) return d.name").data()
    data_1list=[]
    for i in data_1:
        for k,v in i.items():
            data_1list.append(v)
    decisionlist={}
    for i in data_1list:
        data_2temp=[]
        data_2=graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) where d.name='"+i+"' return a.name").data()
        for j in data_2:
            if (j not in data_2temp):
                data_2temp.append(j)
        decisionlist[i]=len(data_2temp)

    dic=sorted(decisionlist.items(), key = lambda kv:(kv[1], kv[0]))
    commonconceptslist=[]
    condic={}
    for k,v in dic:
        if(v>=3):
            commonconceptslist.append(k)
            condic[k]=v
    return commonconceptslist,condic

