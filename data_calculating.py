from collections import Counter
import numpy as np
#计算与其他decision有多少个共同的concept
from py2neo import Graph,Node, Relationship
##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
def link_decisioncount(decisionlist):
    decisionnamelist=[]
    data_1 = []
    outdecision = {}
    outdecisiontt={}
    ##可以使用data()方法获取查获结果
    for str in decisionlist:
        listtemp=[]
        data_1 = graph.run(
            "MATCH(a)-[]->()-[]->()-[]->()<-[]-()<-[]-()<-[]-(d) where a.name='" + str[0] + "'return d.name").data()
        #data_1 = graph.run(
            #"MATCH(a)-[]->()-[]->()-[]->()<-[]-()<-[]-()<-[]-(d) where a.name='" + str + "'return d.name").data()

        for i in data_1:
            if(i not in listtemp):
                listtemp.append(i)
        outdecisiontt[str[0]]=len(listtemp)-1

    data_list = []
    for i in data_1:
        for k, v in i.items():
            data_list.append(v)
    #将和某个decision关联的decision统计出来
    for i in decisionlist:
        decisionnamelisttemp=[]
        for j in range(2,len(i),4):
            for p in decisionlist:
                if((i[j] in p) and (i!=p)):
                    decisionnamelisttemp.append(p[0])
        decisionnamelist.append(decisionnamelisttemp)
    #过滤重复的decision并统计关联数

    for i in decisionlist:
        for j in decisionnamelist:
            outdecision[i[0]]=len(Counter(j))

    return outdecisiontt
#计算有多少与其他decision有多少个共同的concept
def link_conceptcount(decisionlist):
    outconceptcount={}
    outdecisiontt={}

    ##可以使用data()方法获取查获结果
    for str in decisionlist:
        listtemp = []
        data_1 = graph.run(
            "MATCH(a)-[]->()-[]->()-[]->(c)<-[]-()<-[]-()<-[]-(d) where a.name='" + str[0] + "' return c.name").data()

        for i in data_1:
            if (i not in listtemp):
                listtemp.append(i)
        outdecisiontt[str[0]] = len(listtemp) - 1
    for i in decisionlist:
        count=0
        concepttemp=[]
        for j in range(2,len(i),4):
            if(i[j] not in concepttemp):
                concepttemp.append(i[j])

        for k in concepttemp:
            for m in decisionlist:
                if (k in m and i!=m):
                    count=count+1
        outconceptcount[i[0]]=count
    return outdecisiontt
#计算decision到其他decision之间的总距离
def concept_linkdecisiondis(decisionlist):
    #字典输出，每个decision到其他deecision的总距离
    outdecisiondis={}
    #获取每个decision块的内容
    for i in decisionlist:
        strtemp=i[0]
        #获取单独的decision
        #定义一个list用于存储每个block有多少个concept
        listblockconcept=[]
        blocklist=['people','timestamp','activity','step','component','part','parameter','assumption',
                   'variable','constraints','bounds','goal']
        #统计每块有多少个概念
        for p in blocklist:
            listblockconcept.append(i.count(p))
        #用于存储每个block和其他block有多少共同的concept
        blocklistconceptcommon=[0,0,0,0,0,0,0,0,0,0,0,0]
        for j in range(2,len(i)-1,4):
            if(i.count(i[j])>1):
                for s in range(0,11,1):
                    if(i[j-1]==blocklist[s]):
                        blocklistconceptcommon[s]=blocklistconceptcommon[s]+1
        #定义每个block的weightlist
        weightlist=[0,0,0,0,0,0,0,0,0,0,0,0]
        for z in range(0,len(weightlist)):
            weightlist[z]=(listblockconcept[z]+1)/(blocklistconceptcommon[z]+1)
        #获取每个concept的tf-idf值
        for f in range(0, len(blocklist), 1):
            for b in range(3,len(i),4):
                if(i[b-2]==blocklist[f] and float(i[b])>0):

                    i[b]=weightlist[f]/float(i[b])
        #定义list用于存储commconcept
        commonconcept=[]
        for j in range(2, len(i), 4):
            for p in decisionlist:
                if ((i[j] in p) and (i != p)):
                    commonconcept.append(i[j])
        # 计算总距离，定义总距离量sumdistane
        commonconcepttemp=[]
        for i in commonconcept:
            if (i not in commonconcepttemp):
                commonconcepttemp.append(i)
        sumdistance = 0
        for j in range(0,len(commonconcepttemp),1):
            for k in decisionlist:
                sumdistacetemp=10000000000000000.0
                for s in range(2,len(k)-1,4):
                    if(commonconcepttemp[j]==k[s] and float(k[s+1])<=sumdistacetemp):
                        sumdistacetemp=float(k[s+1])
                        sumdistance=sumdistance+sumdistacetemp
        outdecisiondis[strtemp]=sumdistance
    return outdecisiondis

#获取一个概念连接了多少的decision
def concept_linkdecisionnum(decisionlist):
    #定义空的字典
    outdecisioncount={}
    #定义空的list存储所有的concept
    conceptlist=[]

    for i in decisionlist:
        for j in range(2,len(i),4):
            if(i[j] not in conceptlist):
                conceptlist.append(i[j])
    #统计每个概念关联的decision
    for i in conceptlist:
        count=0
        for j in decisionlist:
            if (i in j):
                count=count+1
        outdecisioncount[i]=count

    return outdecisioncount

#统计每个概念到关联的decision的总距离
def concept_decisiondis(decisionlist):
    outconceptdis={}
    # 定义空的list存储所有的concept
    conceptlist = []
    for i in decisionlist:
        for j in range(2, len(i), 4):
            if (i[j] not in conceptlist):
                conceptlist.append(i[j])

    #计算总距离
    for i in range(0,len(conceptlist),1):
        sumdistance=0
        sumdistancetemp = 100000000
        for j in decisionlist:
            for k in range(2,len(j),4):
                if (conceptlist[i]==j[k] and float(j[k+1])<=sumdistancetemp ):
                    sumdistancetemp=float(j[k+1])
        sumdistance=sumdistance+sumdistancetemp
        outconceptdis[conceptlist[i]]=sumdistance
    return outconceptdis
