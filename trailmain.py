import concept_get
import conditions_get
import conditions_test
import trials_coding
import pandas as pd
import conditions_getnew
import test_nooc
commoncept=trials_coding.commoncept_get()[0]
condic=trials_coding.commoncept_get()[1]
conceptdic=concept_get.concept_get(commoncept,condic)
HR_dic1={}
HR_dic2={}
HR_dic3={}
for k,v in conceptdic.items():
    conditions=conditions_getnew.conditions_get(v)
    print(conditions)
    #print(len(conditions))
    #print(conditions,k)

    HR_dic=conditions_test.conditions_test(conditions,k)

    HR_dic1[k]=HR_dic[0]
    HR_dic2[k]=HR_dic[1]
    HR_dic3[k] = HR_dic[2]

dataframe = pd.DataFrame(HR_dic1)
dataframe.to_csv("D:\\knowledegegraph\\research\\test\\HR4snew7_4_1.csv", index=False, sep=',')
dataframe1 = pd.DataFrame(HR_dic2)
dataframe.to_csv("D:\\knowledegegraph\\research\\test\\HR4snew7_4_2.csv", index=False, sep=',')
dataframe2 = pd.DataFrame(HR_dic3)
dataframe.to_csv("D:\\knowledegegraph\\research\\test\\HR4snew7_4_3.csv", index=False, sep=',')