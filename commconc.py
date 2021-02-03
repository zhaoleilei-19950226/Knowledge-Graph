from py2neo import Graph,Node, Relationship
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
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
        for k,v in j.items():
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

data3=graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) return a.name").data()
data3temp=[]
for i in data3:
    for k,v in i.items():
        if(v not in data3temp):
            data3temp.append(v)
comcon=[]
conceptnum=[]
for i in data3temp:
    data4 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) where a.name='"+i+"' return d.name").data()
    data4temp=[]
    count=0
    for j in data4:
        for k,v in j.items():
            if (v not in data4temp):
                data4temp.append(v)
    for s in data4temp:
        if(s in commonconceptslist):
            count=count+1
    comcon.append((i,count))
    conceptnum.append((i,len(data4temp)))
for i in comcon:
    print(i[1])
print("______________")
for i in conceptnum:
    print(i[1])