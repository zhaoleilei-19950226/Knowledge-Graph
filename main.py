import data_extract
import data_calculating
import metric_calculating
from collections import Counter
str=input()
string=data_extract.data_extractpositive(str)
print(string)
strchange=[]
for i in string:
    if (i not in strchange):
        strchange.append(i)
decisionlist=[]
decisionlisttemp=[]
stringtemp=""
for i in strchange:
    #stringtemp = stringtemp + "a.name='" + i + "' or "
    #print("MATCH(a) where " + stringtemp + "'return a")
    stringtemp=data_extract.data_extractnegative(i)
    decisionlist.append(stringtemp)
    decisionlisttemp.append(stringtemp)
print(decisionlist)
k=metric_calculating.decison_ranking(decisionlist)
t=metric_calculating.concept_ranking(decisionlisttemp)
print(k)
print(t)

