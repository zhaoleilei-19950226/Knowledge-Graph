from py2neo import Graph,Node, Relationship
import data_extract
import metric_calculating
import numpy as np
import pandas as pd
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
data_1 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) return a.name").data()
data_1list=[]
for i in data_1:
    for k,v in i.items():
        if(v not in data_1list):
            data_1list.append(v)
finaldic={}
for q in data_1list:
    print(q)
    countlist=[]
    data2=graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) where a.name='"+q+"' return d.name").data()
    datalist=[]
    for j in data2:
        for k,v in j.items():
            if(v not in datalist):
                datalist.append(v)
    for s in datalist:
        count = 0
        str = s
        string = data_extract.data_extractpositive(str)
        strchange = []
        for i in string:
            if (i not in strchange):
                strchange.append(i)
        decisionlist1 = []
        decision1ist1temp=[]
        for ss in strchange:
            stringtemp = data_extract.data_extractnegative(ss)
            decisionlist1.append(stringtemp)
            decision1ist1temp.append(stringtemp)
        t1=metric_calculating.decison_ranking(decisionlist1)
        tt1 = metric_calculating.concept_ranking(decision1ist1temp)
        decision1=[]
        for tul in t1:
            decision1.append(tul[0])
        count = count + 1


        if(q not in decision1 or decision1.index(q)<1):
            countlist.append(count)

            continue

        concept1=[]
        for k,v in tt1.items():
            concept1.append(k)
        nextinput1=concept1[1]
        decisionlistreceive1 = []
        decisionlistreceive1temp=[]
        for i in decisionlist1:
            for j in range(2, len(i) - 1, 4):
                if (i[j] == nextinput1):
                    decisionlistreceive1.append(i)
                    decisionlistreceive1temp.append(i)
        t2 = metric_calculating.decison_ranking(decisionlistreceive1)
        decision2 = []
        for tul in t2:
            decision2.append(tul[0])
        count = count + 1

        if (q not in decision2 or decision2.index(q) <1):
            countlist.append(count)

            continue

        tt2 = metric_calculating.concept_ranking(decisionlistreceive1temp)
        concept2 = []
        for k, v in tt2.items():
            concept2.append(k)
        nextinput2 = concept2[1]
        decisionlistreceive2 = []
        decisionlistreceive2temp=[]
        for i in decisionlistreceive1:
            for j in range(2, len(i) - 1, 4):
                if (i[j] == nextinput2):
                    decisionlistreceive2.append(i)
                    decisionlistreceive2temp.append(i)
        t3 = metric_calculating.decison_ranking(decisionlistreceive2)
        decision3 = []
        for tul in t3:
            decision3.append(tul[0])
        count = count + 1

        if (q not in decision3 or decision3.index(q) < 1 ):
            countlist.append(count)

            continue
        tt3 = metric_calculating.concept_ranking(decisionlistreceive2temp)

        concept3 = []
        for k, v in tt3.items():
            concept3.append(k)
        nextinput3 = concept3[1]
        decisionlistreceive3 = []
        decisionlistreceive3temp=[]
        for i in decisionlistreceive2:
            for j in range(2, len(i) - 1, 4):
                if (i[j] == nextinput3):
                    decisionlistreceive3.append(i)
                    decisionlistreceive3temp.append(i)
        t4 = metric_calculating.decison_ranking(decisionlistreceive3)
        decision4 = []
        for tul in t4:
            decision4.append(tul[0])
        count = count + 1

        if (q not in decision4 or decision4.index(q) < 1 ):
            countlist.append(count)

            continue

    finaldic[q]=np.mean(countlist)
dataframe = pd.DataFrame(finaldic,index=[0])
dataframe.to_csv("D:\\knowledegegraph\\research\\test\\firstpart.csv", index=False, sep=',')



