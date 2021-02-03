#统计每个概念到关联的decision的总距离
def concept_linkdecisionnum(decisionlisttemp):
    #定义空的字典

    outdecisioncount={}
    #定义空的list存储所有的concept
    conceptlist=[]
    for i in decisionlisttemp:
        for j in range(2,len(i)-1,4):
            if(i[j] not in conceptlist):
                conceptlist.append(i[j])
    #统计每个概念关联的decision
    for i in conceptlist:
        count=0
        for j in decisionlisttemp:
            if (i in j):
                count=count+1
        outdecisioncount[i]=count

    return outdecisioncount

def concept_decisiondis(decisionlisttemp):
    outconceptdis={}
    # 定义空的list存储所有的concept
    conceptlist = []

    for i in decisionlisttemp:
        for j in range(2,len(i)-1,4):
            if(i[j] not in conceptlist):
                conceptlist.append(i[j])
        # 获取每个decision块的内容

    for i in decisionlisttemp:
        strtemp = i[0]
        # 获取单独的decision
        # 定义一个list用于存储每个block有多少个concept
        listblockconcept = []
        blocklist = ['people', 'timestamp', 'activity', 'step', 'component', 'part', 'parameter', 'assumption',
                         'variable', 'constraints', 'bounds', 'goal']
        # 统计每块有多少个概念
        for p in blocklist:
            listblockconcept.append(i.count(p))
        # 用于存储每个block和其他block有多少共同的concept
        blocklistconceptcommon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(2, len(i) - 1, 4):
            if (i.count(i[j]) > 1):
                for s in range(0, 11, 1):
                     if (i[j - 1] == blocklist[s]):
                        blocklistconceptcommon[s] = blocklistconceptcommon[s] + 1
            # 定义每个block的weightlist

        weightlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for z in range(0, len(weightlist)):
            weightlist[z] = (listblockconcept[z] + 1) / (blocklistconceptcommon[z] + 1)
        # 获取每个concept的tf-idf值

        for f in range(0, len(blocklist) - 1, 1):
            for b in range(3, len(i) , 4):
                if (i[b - 2] == blocklist[f] and float(i[b]) > 0):
                    i[b] = weightlist[f] / float(i[b])

    #计算总距离
    for i in range(0,len(conceptlist),1):
        sumdistance=0
        sumdistancetemp = 100000000
        for j in decisionlisttemp:
            for k in range(3,len(j)-1,4):
                if (conceptlist[i]==j[k-1] and float(j[k])<=sumdistancetemp ):
                    sumdistancetemp=float(j[k])
                    sumdistance=sumdistance+sumdistancetemp
        outconceptdis[conceptlist[i]]=sumdistance

    return outconceptdis