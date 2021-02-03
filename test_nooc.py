from py2neo import Graph
import metric_calculating
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
def conditions_test(conditionlist,decisionname):
    count=0
    HR_dic={}
    for i in conditionlist:
        decisionlist=[]
        N=len(i)

        print(i)
        print(decisionname)
        for j in i:
            data_1 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) where d.name='" + j + "'return a.name").data()
            data_1list=[]
            for dic in data_1:
                if(dic not in data_1list):
                    data_1list.append(dic)
            for s in data_1list:
                for k, v in s.items():
                    decisionlist.append(v)
        decisionlistuse=[]
        print(N)
        print(decisionlist)
        for d in decisionlist:
            if(decisionlist.count(d)==N):
                decisionlistuse.append(d)
        print(decisionlistuse)
        ##可以使用data()方法获取查获结果

        c = decisionlistuse.index(decisionname)

        if ( c + 1 <= 3):
            count = count + 1

    HR=count
    HR_dic[decisionname]=HR
    return HR_dic

