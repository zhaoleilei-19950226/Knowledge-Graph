from py2neo import Graph,Node, Relationship
import pandas as pd
##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
data_1 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d)" +"return a.name").data()
data_1list=[]
connected_decision={}
connected_concepts={}
concept_decision={}
for i in data_1:
    for k,v in i.items():
        if(v not in data_1list):
            data_1list.append(v)
for i in data_1list:
    listtemp=[]
    data_1_div= graph.run("MATCH(a)-[]->()-[]->()-[]->(c)<-[]-()<-[]-()<-[]-(d) where a.name='"
                          + i + "'return d.name").data()
    for j in data_1_div:
        if(j not in listtemp):
            listtemp.append(j)
    connected_decision[i]=len(listtemp)-1

data_2 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d)" +"return a.name").data()
data_2list=[]

for i in data_2:
    for k,v in i.items():
        if(v not in data_2list):
            data_2list.append(v)
for i in data_2list:
    listtemp=[]
    data_2_div= graph.run("MATCH(a)-[]->()-[]->()-[]->(c) where a.name='"
                          + i + "'return c.name").data()
    for j in data_2_div:
        for k,v in j.items():
            if(v not in listtemp):
                listtemp.append(v)
    connected_concepts[i]=len(listtemp)-1

modelname=[]
connected_decisionnum=[]
connected_conceptsnum=[]
for k,v in connected_decision.items():
    modelname.append(k)
    connected_decisionnum.append(v)
for k,v in connected_concepts.items():
    connected_conceptsnum.append(v)

dataframe = pd.DataFrame({"modelname":modelname,"connected_decision":connected_decisionnum,"connected_concepts":connected_conceptsnum})
dataframe.to_csv("D:\\knowledegegraph\\research\\connected_decisions.csv", index=False, sep=',')

