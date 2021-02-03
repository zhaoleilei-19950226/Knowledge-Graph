from py2neo import Graph
import metric_calculating
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
def conditions_test(conditionlist,decisionname):
    count=0
    HR_dic={}
    HR_dic1={}
    HR_dic2={}
    HR_dic3 = {}
    clist=[]
    orilist=[]
    counttemp=0
    count1=0
    counttemp1=0
    count2=0
    counttemp2=0
    count3 = 0
    counttemp3 = 0
    for i in conditionlist:
        decisionlist=[]
        N = len(i)
        for j in i:
            data_1 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) where d.name='" + j + "'return a.name").data()
            data_1list=[]
            for dic in data_1:
                if(dic not in data_1list):
                    data_1list.append(dic)
            for t in data_1list:
                for k, v in t.items():
                    decisionlist.append(v)
        decisionlistuse=[]
        for d in decisionlist:
            if(decisionlist.count(d)==N ):
                decisionlistuse.append(d)
        decisionlistfinal=[]
        ##可以使用data()方法获取查获结果
        for str in decisionlistuse:
            data_2 = graph.run(
                "MATCH(a)-[]->(b)-[]->(c)-[r]->(d) where a.name='" + str + "'return a.name,c.name,d.name,r.tfidf").data()
            data_list = []
            for i in data_2:
                for k, v in i.items():
                    data_list.append(v)
            decisionlistfinal.append(data_list)

        k = metric_calculating.decison_ranking(decisionlistfinal)
        finaldecision=[]
        for t in k:
            finaldecision.append(t[0])

        c=finaldecision.index(decisionname)
        ctemp=decisionlistuse.index(decisionname)
        #if(c<ctemp):
            #count=count+1
        #if (c > ctemp):
            #counttemp = counttemp + 1
        #if (c+1<=3):
            #count = count + 1
        #if (ctemp+1<=3):
            #counttemp = counttemp + 1
        if (c+1<=1):
            count1 = count1 + 1
        if (ctemp+1<=1):
            counttemp1 = counttemp1 + 1
        if (c+1<=2):
            count2 = count2 + 1
        if (ctemp+1<=2):
            counttemp2 = counttemp2 + 1
        if (ctemp+1<=3):
            counttemp3 = counttemp3 + 1
        #if (c/len(finaldecision)<0.3):
            #count=count+1
        #if(c/len(decisionlistuse)<0.3):
            #count=count+1
        #HR.append((c,decisionlistuse.index(decisionname)))
    HR=(count,counttemp)
    HR1=(count1,counttemp1)
    HR2=(count2,counttemp2)
    HR3=(count3,counttemp3)
    #HR=(count/len(conditionlist),counttemp/len(conditionlist))
    HR_dic1[decisionname]=HR1
    HR_dic2[decisionname] = HR2
    HR_dic3[decisionname] = HR3
    return HR_dic1,HR_dic2,HR_dic3

