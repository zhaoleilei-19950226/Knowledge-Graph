import data_calculating
import math
import data_calculationconcept
import pandas as pd
#给decision排序
def decison_ranking(decisionlist):
    dic1temp=data_calculating.link_decisioncount(decisionlist)
    dic2temp=data_calculating.link_conceptcount(decisionlist)
    dic3temp=data_calculating.concept_linkdecisiondis(decisionlist)
    dicplus=[dic1temp,dic2temp,dic3temp]
    decisionname=[]
    dclist=[]
    ncclist=[]
    sclist=[]
    for k,v in dic1temp.items():
        decisionname.append(k)
        dclist.append(v)
    for k,v in dic2temp.items():
        ncclist.append(v)
    for k,v in dic3temp.items():
        sclist.append(v)

    decisionlisttemp=[]
    for k,v in dic1temp.items():
        decisionlisttemp.append(k)
    for k,v in dic3temp.items():
        dic3temp[k]=-v
    for d in dicplus:
        sqr=0
        for k, v in d.items():
            sqr = sqr + v * v
        for k, v in d.items():
            d[k]= v / (math.sqrt(sqr)+0.000001)
        maxnum = 0
        for k, v in d.items():
            if (v >= maxnum):
                maxnum = v
        #建立di+矩阵
        for k,v in d.items():
           d[k]=(v-maxnum)*(v-maxnum)

    dc=[]
    ncc=[]
    sc=[]
    for k,v in dic1temp.items():
        dc.append(v)
    for k,v in dic2temp.items():
        ncc.append(v)
    for k,v in dic3temp.items():
        sc.append(v)
    #创建list用于存储d+


    dplus=[]
    for i in range(0,len(dc),1):
        dplus.append(math.sqrt(dc[i]+ncc[i]+sc[i]))
    dic1 = data_calculating.link_decisioncount(decisionlist)
    dic2 = data_calculating.link_conceptcount(decisionlist)
    dic3 = data_calculating.concept_linkdecisiondis(decisionlist)

    dicminus = [dic1, dic2, dic3]
    for k,v in dic1.items():
        decisionlist.append(k)
    for k,v in dic3.items():
        dic3temp[k]=-v
    #计算d-
    for d in dicminus:
        for k, v in d.items():
            v = -v
        sqr = 0
        for k, v in d.items():
            sqr = sqr + v * v
        for k, v in d.items():
            d[k] = v / (math.sqrt(sqr)+0.00000001)
        minnum = 1000000
        for k, v in d.items():
            if (v <= minnum):
                minum = v
        # 建立di+矩阵
        for k, v in d.items():
            v = (v - minnum) * (v - minnum)
    dc = []
    ncc = []
    sc = []
    for k, v in dic1.items():
        dc.append(v)
    for k, v in dic2.items():
        ncc.append(v)
    for k, v in dic3.items():
        sc.append(v)
    # 创建list用于存储d+
    dminus = []
    for i in range(0, len(dic1) , 1):
        dminus.append(math.sqrt(dc[i] + ncc[i] + sc[i]))
    #计算c
    maxd=0
    mind=1000000
    for i in dplus:
        if(i<=mind):
            mind=i
    for i in dminus:
        if(i>=maxd):
            maxd=i

    c=[]
    for i in range(0,len(dic1),1):
        c.append(dplus[i]/(mind+0.000001)-dminus[i]/(maxd+0.000001))
    dataframe = pd.DataFrame({"decision":decisionname,"DC": dclist, "NCC": ncclist, "SC": sclist,"OC":c})
    dataframe.to_csv("D:\\knowledegegraph\\research\\decisions.csv", index=False, sep=',')
    outdic={}
    for i in range(0,len(decisionlisttemp),1):
        outdic[decisionlisttemp[i]]=c[i]
    f = zip(outdic.keys(), outdic.values())
    c = sorted(f)
    d_order = sorted(outdic.items(), key=lambda x: x[1], reverse=False)
    print(d_order)
    return d_order


#给concept排序
def concept_ranking(decisionlisttemp):
    dic4temp = data_calculationconcept.concept_linkdecisionnum(decisionlisttemp)
    dic5temp = data_calculationconcept.concept_decisiondis(decisionlisttemp)
    dicplus = [dic4temp, dic5temp]
    conceptname=[]
    decisionlisttemptemp = []
    dclist = []

    sclist = []
    for k, v in dic4temp.items():
        conceptname.append(k)
        dclist.append(v)

    for k, v in dic5temp.items():
        sclist.append(v)
    for k, v in dic4temp.items():
        decisionlisttemptemp.append(k)

    for k, v in dic5temp.items():
        dic5temp[k] = -v
    for d in dicplus:
        sqr = 0
        for k, v in d.items():
            sqr = sqr + v * v
        for k, v in d.items():
            d[k] = v / math.sqrt(sqr)
        maxnum = 0
        for k, v in d.items():
            if (v >= maxnum):
                maxnum = v
        # 建立di+矩阵
        for k, v in d.items():
            d[k] = (v - maxnum) * (v - maxnum)

    dc = []
    sc = []
    for k, v in dic4temp.items():
        dc.append(v)
    for k, v in dic5temp.items():
        sc.append(v)
    # 创建list用于存储d+
    dplus = []
    for i in range(0, len(dc), 1):
        dplus.append(math.sqrt(dc[i]  + sc[i]))
    dic4 = data_calculationconcept.concept_linkdecisionnum(decisionlisttemp)
    dic5 = data_calculationconcept.concept_decisiondis(decisionlisttemp)

    dicminus = [dic4, dic5]

    for k, v in dic5.items():
        dic5temp[k] = -v
    # 计算d-
    for d in dicminus:
        for k, v in d.items():
            v = -v
        sqr = 0
        for k, v in d.items():
            sqr = sqr + v * v
        for k, v in d.items():
            d[k] = v / math.sqrt(sqr)
        minnum = 1000000
        for k, v in d.items():
            if (v <= minnum):
                minum = v
        # 建立di+矩阵
        for k, v in d.items():
            v = (v - minnum) * (v - minnum)
    dc = []
    sc = []
    for k, v in dic4.items():
        dc.append(v)
    for k, v in dic5.items():
        sc.append(v)
    # 创建list用于存储d+
    dminus = []
    for i in range(0, len(dic4), 1):
        dminus.append(math.sqrt(dc[i] + sc[i]))
    # 计算c
    maxd = 0
    mind = 1000000
    for i in dplus:
        if (i <= mind):
            mind = i
    for i in dminus:
        if (i >= maxd):
            maxd = i

    c = []
    for i in range(0, len(dic4), 1):
        c.append(dplus[i] / (mind+0.0001) - dminus[i] / (maxd+0.0001))
    dataframe = pd.DataFrame({"concept":conceptname,"DC": dclist,"SC": sclist,"OC": c})
    dataframe.to_csv("D:\\knowledegegraph\\research\\concepts.csv", index=False, sep=',')
    outdic = {}
    for i in range(0, len(decisionlisttemptemp), 1):
        outdic[decisionlisttemptemp[i]] = c[i]
    f = zip(outdic.keys(), outdic.values())
    c = sorted(f)

    return outdic