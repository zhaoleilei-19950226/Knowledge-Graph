import data_extract
import data_calculating
import metric_calculating
from collections import Counter
#循环1
str=input()
string=data_extract.data_extractpositive(str)
strchange=[]
for i in string:
    if (i not in strchange):
        strchange.append(i)
decisionlist=[]
decisionlisttemp=[]
stringstring=""
print(strchange)
for i in strchange:
    stringstring = stringstring + "a.name='" + i + "' or "
    stringtemp=data_extract.data_extractnegative(i)
    decisionlist.append(stringtemp)
    decisionlisttemp.append(stringtemp)
metric_calculating.decison_ranking(decisionlist)
metric_calculating.concept_ranking(decisionlisttemp)
print("MATCH(a) where " + stringstring + "'return a")
#循环2
stringstring=""
str1=input()
decisionlistreceive1=[]
decisionlistreceivetemp1=[]
for i in decisionlist:
    for j in range(2,len(i)-1,4):
        if (i[j]==str1):
            decisionlistreceive1.append(i)

            decisionlistreceivetemp1.append(i)
print(len(decisionlistreceive1))
for i in decisionlistreceive1:
    stringstring = stringstring + "a.name='" + i[0] + "' or "
metric_calculating.decison_ranking(decisionlistreceive1)
metric_calculating.concept_ranking(decisionlistreceivetemp1)
print("MATCH p=(a)-[]->()-[]->()-[]->() where " + stringstring + "'return p")
#循环3
str2=input()
decisionlistreceive2=[]
decisionlistreceivetemp2=[]
for i in decisionlistreceive1:
    for j in range(2,len(i)-1,4):
        if (i[j]==str2):
            decisionlistreceive2.append(i)
            decisionlistreceivetemp2.append(i)
metric_calculating.decison_ranking(decisionlistreceive2)
metric_calculating.concept_ranking(decisionlistreceivetemp2)

#循环3
str3=input()
decisionlistreceive3=[]
decisionlistreceivetemp3=[]
for i in decisionlistreceive2:
    for j in range(2,len(i)-1,4):
        if (i[j]==str3):
            decisionlistreceive3.append(i)
            decisionlistreceivetemp3.append(i)
metric_calculating.decison_ranking(decisionlistreceive3)
metric_calculating.concept_ranking(decisionlistreceivetemp3)