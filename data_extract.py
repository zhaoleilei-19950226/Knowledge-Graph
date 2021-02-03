#coding:utf-8
from py2neo import Graph,Node, Relationship
from pandas import DataFrame
import m_array4d

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
def data_extractpositive(str):
    ##可以使用data()方法获取查获结果
    data_1 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) where d.name='"+str+"'return a.name").data()
    data_list=[]
    for i in data_1:
        for k,v in i.items():
            data_list.append(v)
    return data_list

def data_extractnegative(string):
    data_1=[]
    ##可以使用data()方法获取查获结果
    stringtemp=""

    data_1 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[r]->(d) where a.name='"+string+"'return a.name,c.name,d.name,r.tfidf").data()

    data_list=[]
    for i in data_1:
        for k,v in i.items():
            data_list.append(v)
    return data_list

