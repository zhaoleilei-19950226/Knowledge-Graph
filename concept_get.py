from py2neo import Graph
graph = Graph('http://localhost:7474', username='neo4j', password='zl337')
def concept_get(commonconcept_list,condic):
    data_1 = graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) return a.name").data()
    data_1list=[]
    for i in data_1:
        for k,v in i.items():
            data_1list.append(v)
    decision_concept_dic={}
    for i in data_1list:
        data_2=graph.run("MATCH(a)-[]->(b)-[]->(c)-[]->(d) where a.name='"+i+"' return d.name").data()
        concept_list=[]
        conceptnumdic={}
        for j in data_2:
            for k,v in j.items():
                if(v in commonconcept_list and v not in concept_list):
                    concept_list.append(v)
        for countnum in concept_list:
            conceptnumdic[countnum]=condic[countnum]
        dic = sorted(conceptnumdic.items(), key=lambda kv: (kv[1], kv[0]))
        concept_listuse=[]
        for k,v in dic:
            concept_listuse.append(k)
        N=7
        if(len(concept_listuse)>=N):
            decision_concept_dic[i]=concept_listuse[len(concept_listuse)-N:len(concept_listuse)]
        if (len(concept_listuse)<N):
            decision_concept_dic[i] = concept_listuse
    return decision_concept_dic

