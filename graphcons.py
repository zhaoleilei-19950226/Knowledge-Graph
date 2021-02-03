import os
import codecs
import math
import operator
import nltk
import pandas as pd
import csv
import re
import string
import numpy as np
from gensim.parsing.preprocessing import remove_stopwords

def fun(filepath):  # 遍历文件夹中的所有文件，返回文件list
    arr = []
    for root, dirs, files in os.walk(filepath):
        for fn in files:
            arr.append(root+"\\"+fn)

    return arr


def wry(txt, path):  # 写入txt文件
    f = codecs.open(path, 'a', 'gbk')
    f.write(txt)
    f.close()
    return path


def read(path):  # 读取txt文件，并返回list
    f = open(path, encoding="gbk")
    data = []
    for line in f.readlines():
        data.append(line)
    return data

#def toword(txtlis):
    #wordlist=''

    #wordlisttemp='|'.join(str(i) for i in txtlis)
#    # wordlist=nltk.word_tokenize(wordlisttemp)
    #print(wordlist)
   # return wordlist



def toword(txtlis):  # 将一片文章按照‘/’切割成词表，返回list

    wordlisttemp='|'.join(str(i) for i in txtlis)
    punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
    re.sub(r"[%s]+" %punc, "",wordlisttemp)
    for c in string.punctuation:

        wordlisttemp = wordlisttemp.replace(c, "")

    wordlisttemp=remove_stopwords(wordlisttemp)
    wordlist=nltk.word_tokenize(wordlisttemp)
    wordlis = []
    txtlis='|'.join(txtlis)

    f=open(r'C:\learning\research\mycorpus.txt',encoding='utf-8')
    result={}
    for i in f.readlines():
        result[i]=txtlis.count(i.rstrip('\n'))

    resultkey=list(result.keys())

    resultvalue=list(result.values())

    for i in range(0,len(resultkey)):
        if(resultvalue[i]!=0):

            for j in range(0,resultvalue[i]):

                wordlis.append(resultkey[i])

    #for i in f.readlines():
        #if(txtlis.find(str(i).rstrip('\n'))>=1):
           # str(i).rstrip()
            #wordlis.append(str(i))

    wordlis=wordlis+wordlist




    return wordlis

def getstopword(path):  # 获取停用词表
    swlis = []
    for i in read(path):
        outsw = str(i).replace('\n', '')
        swlis.append(outsw)
    return swlis

def getridofsw(lis, swlist):  # 去除文章中的停用词
    afterswlis = []
    for i in lis:
        if str(i) in swlist:
            continue
        else:
            afterswlis.append(str(i))
    return afterswlis


def freqword(wordlis):  # 统计词频，并返回字典
    freword = {}
    for i in wordlis:
        if str(i) in freword:
            count = freword[str(i)]
            freword[str(i)] = count+1
        else:
            freword[str(i)] = 1
    return freword


def corpus(filelist, swlist):  # 建立语料库
    alllist = []
    for i in filelist:
        afterswlis = getridofsw(toword(read(str(i))), swlist)
        alllist.append(afterswlis)
    return alllist


def wordinfilecount(word, corpuslist):  # 查出包含该词的文档数
    count = 0  # 计数器
    for i in corpuslist:
        for j in i:
            if word in set(j):  # 只要文档出现该词，这计数器加1，所以这里用集合
                count = count+1
            else:
                continue
    return count


def tf_idf(wordlis, filelist, corpuslist):  # 计算TF-IDF,并返回字典
    outdic = {}
    tf = 0
    idf = 0
    dic = freqword(wordlis)
    outlis = []
    wordlistemp=[]
    f = open(r'C:\learning\research\mycorpus.txt', encoding='utf-8')

    for i in f.readlines():
            wordlistemp.append(str(i))

    for i in set(wordlis):

        tf = wordlis.count(i)/len(wordlis)  # 计算TF：某个词在文章中出现的次数/文章总词数
        # 计算IDF：log(语料库的文档总数/(包含该词的文档数+1))
        idf = math.log(len(filelist)/(wordinfilecount(str(i), corpuslist)+1))
        tfidf = tf*idf  # 计算TF-IDF


        if(i in wordlistemp):
            outdic[str(i)] = tfidf



    return outdic



def befwry(lis):  # 写入预处理，将list转为string
    outall = ''
    for i in lis:
        ech = str(i).replace("('", '').replace("',", '\t').replace(')', '')
        outall = outall+'\t'+ech+'\n'

    return outall


def main():

    swpath = r'哈工大停用词表.txt'#停用词表路径
    swlist = getstopword(swpath)  # 获取停用词表列表
    mycorpus=[]
    ff=open(r'C:\learning\research\mycorpus.txt',encoding='UTF-8')
    strtemp=ff.readlines()
    mycorpus.append(strtemp)

    filepath = r'corpous'
    filelist = fun(filepath)  # 获取文件列表

    wrypath = r'TFIDF.txt'

    corpuslist = corpus(filelist, swlist)  # 建立语料库

    outall = ''

    for i in filelist:
        afterswlis = getridofsw(toword(read(str(i))), swlist)  # 获取每一篇已经去除停用的词表
        tfidfdic = tf_idf(afterswlis, filelist, corpuslist)  # 计算TF-IDF

        print(tfidfdic)
        people=[]
        timestamp=[]
        activity=[]
        step=[]
        component=[]
        part=[]
        parameter=[]
        assumption=[]
        variable=[]
        constraints=[]
        bounds=[]
        goal=[]

        value1=[]
        value2=[]
        value3=[]
        value4=[]
        value5=[]
        value6=[]
        value7=[]
        value8=[]
        value9=[]
        value10=[]
        value11=[]
        value12=[]

        titleary = str(i).split('\\')
        title = str(titleary[-1]).replace('utf8.txt', '')
        titlesub=''
        for i in range(0,12,3):
            if(title[i]!='-'and title[i]!=' '):
                titlesub=titlesub+title[i]

        titlesub="".join(titlesub.split())
        varname = [title,title,title,title,title,
                   title,title,"action","action", "service", "process",
                   "product", "product","given","given", "find", "satisfy","satisfy","satisfy"
                   ]
        varrelation = ["has_action","has_service","has_process","has_product",
                       "has_given","has_find","has_satisfy",
                       "has_people","has_timestamp","has_activity","has_step","has_component",
                       "has_part","has_parameter","has_assume","has_variable","has_constraints",
                       "has_bounds","has_goal"]
        varnamebeh=["action",'service',"process","product","given","find","satisfy",
                    "people","timestamp","activity","step","component","part",
                    "parameter","assumption","variable","constraints","bounds","goal"]

        IDmark=[titlesub,titlesub,titlesub,titlesub,titlesub,titlesub,titlesub,
                titlesub+"action",titlesub+"action",titlesub+"service",titlesub+"process",
                titlesub+"product",titlesub+"product",titlesub+"given",titlesub+"given",
                titlesub+"find",titlesub+"satisfy",titlesub+"satisfy",titlesub+"satisfy"]
        Idmarkbeh=[titlesub+"action",titlesub+'service',titlesub+"process",titlesub+"product",
                   titlesub+"given",titlesub+"find",titlesub+"satisfy",
                    titlesub+"people",titlesub+"timestamp",titlesub+"activity",titlesub+"step",
                   titlesub+"component",titlesub+"part",
                    titlesub+"parameter",titlesub+"assumption",titlesub+"variable",
                   titlesub+"constraints",titlesub+"bounds",titlesub+"goal"]
        valueorigin=['null','null','null','null','null','null','null','null','null','null'
                     ,'null','null','null','null','null','null','null','null','null','null']
        conceptlabel=[]
        pathtemp='C:\\learning\\research\\corpous\\'+title
        with open(pathtemp, "r") as f:  # 设置文件对象
            strtemp = f.read()
        strtemp = "".join((re.sub("\n", " ", strtemp)))
        str1= re.findall(r"People(.+?)Timestamp", strtemp)
        str1= "".join(str1)

        str2 = re.findall(r"Timestamp(.+?)Service", strtemp)
        str2 = "".join(str2)
        str3 = re.findall(r"Activity(.+?)Process", strtemp)
        str3 = "".join(str3)
        str4 = re.findall(r"Step(.+?)Product", strtemp)
        str4 = "".join(str4)
        str5 = re.findall(r"Component(.+?)Part", strtemp)
        str5 = "".join(str5)
        str6 = re.findall(r"Part(.+?)Given", strtemp)
        str6= "".join(str6)
        str7 = re.findall(r"Parameter(.+?)Assume", strtemp)
        str7 = "".join(str7)
        str8 = re.findall(r"Assume(.+?)Find", strtemp)
        str8 = "".join(str8)
        str9 = re.findall(r"Part(.+?)Given", strtemp)
        str9 = "".join(str9)
        str10 = re.findall(r"Variable(.+?)Satisfy", strtemp)
        str10 = "".join(str10)
        str11 = re.findall(r"Constraints(.+?)Goal", strtemp)
        str11 = "".join(str11)
        str12 = re.findall(r"Goal(.+?)Modelend", strtemp)
        str12 = "".join(str12)

        for k, v in tfidfdic.items():

            if (str1.find(k.rstrip('\n')) >= 1):


                    k.rstrip('\n')
                    people.append(k)
                    value1.append(v)

            if (str2.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    timestamp.append(k)
                    value2.append(v)

            if (str3.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    activity.append(k)
                    value3.append(v)

            if (str4.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    step.append(k)
                    value4.append(v)

            if (str5.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    component.append(k)
                    value5.append(v)

            if (str6.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    part.append(k)
                    value6.append(v)

            if (str7.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    parameter.append(k)
                    value7.append(v)

            if (str8.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    assumption.append(k)
                    value8.append(v)

            if (str9.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    variable.append(k)
                    value9.append(v)

            if (str10.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    constraints.append(k)
                    value10.append(v)

            if (str11.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    bounds.append(k)
                    value11.append(v)

            if (str12.find(k.rstrip('\n')) >= 1):

                    k.rstrip('\n')
                    goal.append(k)
                    value12.append(v)

        a=max(len(people),len(timestamp),len(activity),
                      len(step),len(component),len(part),
                      len(parameter),len(assumption),len(variable),
                      len(constraints),len(bounds),len(goal))
        sumvalue1=0
        for i in value1:
            sumvalue1=sumvalue1+i
        peoplemean=0
        if(len(value1)>0):
            peoplemean=sumvalue1/len(value1)
        peoplemeansqu = peoplemean * peoplemean+peoplemean
        peoplethreshold=0
        if (len(people)<5):
            j=0
            for i in value1:
                if (i>peoplemeansqu):
                    j=j+1
            if(j==0):
                peoplethreshold=peoplemean
            if(j!=0):
                peoplethreshold=peoplemeansqu
        if (len(people)>=5):
            j=0
            for i in value1:
                if (i>peoplemeansqu):
                    j=j+1
            if(j<2):
                peoplethreshold=peoplemean
            if(j>=2):
                peoplethreshold=peoplemeansqu
        for i in people:
            if (value1[people.index(i)]<peoplethreshold):
                i="null"

        sumvalue2 = 0
        for i in value2:
            sumvalue2 = sumvalue2+ i
        timestampmean=0
        if(len(value2)>0):
            timestampmean = sumvalue2 / len(value2)
        timestampmeansqu=timestampmean*timestampmean+timestampmean
        timestampthreshold=0
        if (len(timestamp)<5):
            j=0
            for i in value2:
                if (i>timestampmeansqu):
                    j=j+1
            if(j==0):
                timestampthreshold=timestampmean
            if(j!=0):
                timestampthreshold=timestampmeansqu
        if (len(timestamp)>=5):
            j=0
            for i in value2:
                if (i>timestampmeansqu):
                    j=j+1
            if(j<2):
                timestampthreshold=timestampmean
            if(j>=0):
                timestampthreshold=timestampmeansqu
        for i in timestamp:
            if (value2[timestamp.index(i)]<timestampthreshold):
                i="null"
        sumvalue3 = 0
        for i in value3:
            sumvalue3 = sumvalue3 + i
        activitymean = 0
        if (len(value3) > 0):
            activitymean = sumvalue3 / len(value3)
        activitymeansqu=activitymean*activitymean+activitymean
        activitythreshold=0
        if (len(activity)<5):
            j=0
            for i in value3:
                if (i>activitymeansqu):
                    j=j+1
            if(j==0):
                activitythreshold=activitymean
            if(j!=0):
                activitythreshold=activitymeansqu
        if (len(activity)>=5):
            j=0
            for i in value3:
                if (i>activitymeansqu):
                    j=j+1
            if(j<2):
                activitythreshold=activitymean
            if(j>=0):
                activitythreshold=activitymeansqu
        for i in activity:
            if (value3[activity.index(i)]<activitythreshold):
                i="null"

        sumvalue4 = 0
        for i in value4:
            sumvalue4 = sumvalue4 + i
        stepmean = 0
        if (len(value4) > 0):
            stepmean = sumvalue4 / len(value4)
        stepmeansqu = stepmean * stepmean+stepmean
        stepthreshold = 0
        if (len(step) < 5):
            j = 0
            for i in value4:
                if (i > stepmeansqu):
                    j = j + 1
            if (j == 0):
                stepthreshold = stepmean
            if (j != 0):
                stepthreshold = stepmeansqu
        if (len(step)>=5):
            j=0
            for i in value4:
                if (i>stepmeansqu):
                    j=j+1
            if(j<2):
                stepthreshold=stepmean
            if(j>=0):
                stepthreshold=stepmeansqu
        for i in step:
            if (value4[step.index(i)] < stepthreshold):
                i = "null"
        sumvalue5 = 0
        for i in value5:
            sumvalue5 = sumvalue5 + i
        componentmean = 0
        if (len(value5) > 0):
            componentmean = sumvalue5 / len(value5)

        componentmeansqu = componentmean * componentmean+componentmean
        componentthreshold = 0
        if (len(component) < 5):
            j = 0
            for i in value5:
                if (i > componentmeansqu):
                    j = j + 1
            if (j == 0):
                componentthreshold = componentmean
            if (j != 0):
                componentthreshold = componentmeansqu
        if (len(component)>=5):
            j=0
            for i in value5:
                if (i>componentmeansqu):
                    j=j+1
            if(j<2):
                componentthreshold=componentmean
            if(j>=0):
                componentthreshold=componentmeansqu
        for i in component:
            if (value5[component.index(i)] < componentthreshold):
                i = "null"
        sumvalue6 = 0
        for i in value6:
            sumvalue6 = sumvalue6 + i
        partmean = 0
        if (len(value6) > 0):
            partmean = sumvalue6 / len(value6)

        partmeansqu = partmean * partmean+partmean
        partthreshold = 0
        if (len(part) < 5):
            j = 0
            for i in value6:
                if (i > partmeansqu):
                    j = j + 1
            if (j == 0):
                partthreshold = partmean
            if (j != 0):
                partthreshold = partmeansqu
        if (len(part)>=5):
            j=0
            for i in value6:
                if (i>partmeansqu):
                    j=j+1
            if(j<2):
                partthreshold=partmean
            if(j>=0):
                partthreshold=partmeansqu
        for i in part:
            if (value6[part.index(i)] < partthreshold):
                i = "null"
        sumvalue7 = 0
        for i in value7:
            sumvalue7 = sumvalue7 + i
        parametermean = 0
        if (len(value7) > 0):
            parametermean = sumvalue7 / len(value7)

        parametermeansqu = parametermean * parametermean+parametermean
        parameterthreshold = 0
        if (len(parameter) < 5):
            j = 0
            for i in value7:
                if (i > parametermeansqu):
                    j = j + 1
            if (j == 0):
                parameterthreshold = parametermean
            if (j != 0):
                parameterthreshold = parametermeansqu
        if (len(parameter)>=5):
            j=0
            for i in value7:
                if (i>parametermeansqu):
                    j=j+1
            if(j<2):
                parameterthreshold=parametermean
            if(j>=0):
                parameterthreshold=parametermeansqu
        for i in parameter:
            if (value7[parameter.index(i)] < parameterthreshold):
                i = "null"
        sumvalue8 = 0
        for i in value8:
            sumvalue8 = sumvalue8 + i
        assumptionmean = 0
        if (len(value8) > 0):
            assumptionmean = sumvalue8 / len(value8)
        assumptionmeansqu = assumptionmean * assumptionmean+assumptionmean
        assumptionthreshold = 0
        if (len(assumption) < 5):
            j = 0
            for i in value8:
                if (i > assumptionmeansqu):
                    j = j + 1
            if (j == 0):
                assumptionthreshold = assumptionmean
            if (j != 0):
                assumptionthreshold = assumptionmeansqu
        if (len(assumption)>=5):
            j=0
            for i in value8:
                if (i>assumptionmeansqu):
                    j=j+1
            if(j<2):
                assumptionthreshold=assumptionmean
            if(j>=0):
                assumptionthreshold=assumptionmeansqu
        for i in assumption:
            if (value8[assumption.index(i)] < assumptionthreshold):
                i = "null"
        sumvalue9 = 0
        for i in value9:
            sumvalue9 = sumvalue9 + i
        variablemean = 0
        if (len(value9) > 0):
            variablemean = sumvalue9 / len(value9)
        variablemeansqu = variablemean * variablemean+variablemean
        variablethreshold = 0
        if (len(variable) < 5):
            j = 0
            for i in value9:
                if (i > variablemeansqu):
                    j = j + 1
            if (j == 0):
                variablethreshold = variablemean
            if (j != 0):
                variablethreshold = variablemeansqu
        if (len(variable)>=5):
            j=0
            for i in value9:
                if (i>variablemeansqu):
                    j=j+1
            if(j<2):
                variablethreshold=variablemean
            if(j>=0):
                variablethreshold=variablemeansqu
        for i in variable:
            if (value9[variable.index(i)] < variablethreshold):
                i = "null"
        sumvalue10 = 0
        for i in value10:
            sumvalue10 = sumvalue10+ i
        constraintsmean = 0
        if (len(value10) > 0):
            constraintsmean = sumvalue10 / len(value10)
        constraintsmeansqu = constraintsmean * constraintsmean+constraintsmean
        constraintsthreshold = 0
        if (len(constraints) < 5):
            j = 0
            for i in value10:
                if (i > constraintsmeansqu):
                    j = j + 1
            if (j == 0):
                constraintsthreshold = constraintsmean
            if (j != 0):
                constraintsthreshold = constraintsmeansqu
        if (len(constraints)>=5):
            j=0
            for i in value10:
                if (i>constraintsmeansqu):
                    j=j+1
            if(j<2):
                constraintsthreshold=constraintsmean
            if(j>=0):
                constraintsthreshold=constraintsmeansqu
        for i in constraints:
            if (value10[constraints.index(i)] < constraintsthreshold):
                i = "null"
        sumvalue11 = 0
        for i in value11:
            sumvalue11 = sumvalue11 + i
        boundsmean = 0
        if (len(value11) > 0):
            boundsmean = sumvalue11 / len(value11)
        boundsmeansqu = boundsmean * boundsmean+boundsmean
        boundsthreshold = 0
        if (len(bounds) < 5):
            j = 0
            for i in value11:
                if (i > boundsmeansqu):
                    j = j + 1
            if (j == 0):
                boundsthreshold = boundsmean
            if (j != 0):
                boundsthreshold = boundsmeansqu
        if (len(bounds)>=5):
            j=0
            for i in value11:
                if (i>boundsmeansqu):
                    j=j+1
            if(j<2):
                boundsthreshold=boundsmean
            if(j>=0):
                boundsthreshold=boundsmeansqu
        for i in bounds:

            if (value11[bounds.index(i)] < boundsthreshold):

                bounds[bounds.index(i)]="null"
        sumvalue12= 0
        for i in value12:
            sumvalue12 = sumvalue12 + i
        goalmean = 0
        if (len(value12) > 0):
            goalmean = sumvalue12 / len(value12)
        goalmeansqu = goalmean * goalmean+goalmean
        goalthreshold = 0
        if (len(goal) < 5):
            j = 0
            for i in value12:
                if (i > goalmeansqu):
                    j = j + 1
            if (j == 0):
                goalthreshold = goalmean
            if (j != 0):
                goalthreshold = goalmeansqu
        if (len(goal)>=5):
            j=0
            for i in value12:
                if (i>goalmeansqu):
                    j=j+1
            if(j<2):
                goalthreshold=goalmean
            if(j>=0):
                goalthreshold=goalmeansqu
        for i in goal:

            if (value12[goal.index(i)] < goalthreshold):

                i = "null"

        for i in people:
            if(i!="null"):
                varname.append('people')
                IDmark.append(titlesub + 'people')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value1[people.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in timestamp:
            if(i!="null"):
                varname.append('timestamp')
                IDmark.append(titlesub + 'timestamp')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value2[timestamp.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)

        for i in activity:
            if(i!="null"):
                varname.append('activity')
                IDmark.append(titlesub + 'activity')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value3[activity.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)

        for i in step:
            if(i!="null"):
                varname.append('step')
                IDmark.append(titlesub + 'step')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value4[step.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in component:
            if(i!="null"):
                varname.append('component')
                IDmark.append(titlesub + 'component')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value5[component.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)

        for i in part:
            if(i!="null"):
                varname.append('part')
                IDmark.append(titlesub + 'part')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value6[part.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in parameter:
            if(i!="null"):
                varname.append('parameter')
                IDmark.append(titlesub + 'parameter')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value7[parameter.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in assumption:
            if(i!="null"):
                varname.append('assumption')
                IDmark.append(titlesub + 'assumption')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value8[assumption.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in variable:
            if(i!="null"):
                varname.append('variable')
                IDmark.append(titlesub + 'variable')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value9[variable.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in constraints:
            if(i!="null"):
                varname.append('constraints')
                IDmark.append(titlesub + 'constraints')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value10[constraints.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in bounds:
            if(i!="null"):
                varname.append('bounds')
                IDmark.append(titlesub + 'bounds')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value11[bounds.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in goal:
            if(i!="null"):
                varname.append('goal')
                IDmark.append(titlesub + 'goal')
                varrelation.append('has_concept')
                varnamebeh.append(i)
                valueorigin.append(value12[goal.index(i)])
                sss = titlesub + i
                ssss = ''
                for c in sss:
                    if (c != " " and c != '-'):
                        ssss = ssss + c
                Idmarkbeh.append(ssss)
        for i in range(len(people),a):
            people.append('null')
            value1.append('null')
        for i in range(len(timestamp),a):
            timestamp.append('null')
            value2.append('null')
        for i in range(len(activity),a):
            activity.append('null')
            value3.append('null')
        for i in range(len(step),a):
            step.append('null')
            value4.append('null')
        for i in range(len(component),a):
            component.append('null')
            value5.append('null')
        for i in range(len(part),a):
            part.append('null')
            value6.append('null')
        for i in range(len(parameter),a):
            parameter.append('null')
            value7.append('null')
        for i in range(len(assumption),a):
            assumption.append('null')
            value8.append('null')
        for i in range(len(variable),a):
            variable.append('null')
            value9.append('null')
        for i in range(len(constraints),a):
            constraints.append('null')
            value10.append('null')
        for i in range(len(bounds),a):
            bounds.append('null')
            value11.append('null')
        for i in range(len(goal),a):
            goal.append('null')
            value12.append('null')

        #dataframe=pd.DataFrame(list(zip(people,value1,timestamp,value2,activity,value3,
                                        #step,value4,component,value5,part,value6,
                                        #parameter,value7,assumption,value8,variable,value9,
                                       # constraints,value10,bounds,value11,goal,value12)),
                               #columns=['people','value1', 'timestamp','value2','activity','value3',
                                      #  'step','value4','component','value5','part','value6',
                                       # 'parameter','value7','assumption','value8','variable','value9',
                                       # 'constraints','value10','bounds','value11','goal','value12'])
        dataframe = pd.DataFrame({'people': people,'value1':value1,
                                  'timestamp': timestamp,'value2':value2,
                                  'activity': activity,'value3':value3,
                                  'step': step,'value4':value4,
                                  'component': component,'value5':value5,
                                  'part': part,'value6':value6,
                                  'parameter': parameter,'value7':value7,
                                  'assumption': assumption,'value8':value8,
                                  'variable': variable,'value9':value9,
                                  'constraints': constraints,'value10':value10,
                                  'bounds': bounds,'value11':value11,
                                  'goal': goal,'value12':value12})

        # 将DataFrame存储为csv,index表示是否显示行名，default=True



        dataframe.to_csv("C:\learning\\research\\blockidentification\\"+title + ".csv", index=False, sep=',')
        echout = title+'\n'+befwry(tfidfdic)

        #conceptsselection
        IDmarktemp = []
        for i in IDmark:
            i = "".join((re.sub(" ", " ", i)))
            i = "".join((re.sub("\n", " ", i)))
            IDmarktemp.append(i)
        Idmarkbehtemp = []
        for i in Idmarkbeh:
            i = "".join((re.sub(" ", " ", i)))
            i = "".join((re.sub("\n", " ", i)))
            Idmarkbehtemp.append(i)
        varnametemp = []
        for i in varname:
            i = "".join((re.sub(" ", " ", i)))
            i = "".join((re.sub("\n", " ", i)))
            varnametemp.append(i)
        varrelationtemp = []
        for i in varrelation:
            i = "".join((re.sub(" ", " ", i)))
            i = "".join((re.sub("\n", " ", i)))
            varrelationtemp.append(i)
        varnamebehtemp = []
        for i in varnamebeh:
            i = "".join((re.sub(" ", " ", i)))
            i = "".join((re.sub("\n", " ", i)))
            varnamebehtemp.append(i)
        dataframe = pd.DataFrame({':START_ID':IDmarktemp,':END_ID':Idmarkbehtemp,
                                  'start': varnametemp, ':TYPE': varrelationtemp,
                                 'end': varnamebehtemp })

        # 将DataFrame存储为csv,index表示是否显示行名，default=True

        dataframe.to_csv("C:\\learning\\research\\triplegenerations\\"+title + "triples.csv", index=False, sep=',')
        dataframe = pd.DataFrame({'concepts':varnamebeh })

        # 将DataFrame存储为csv,index表示是否显示行名，default=True

        dataframe.to_csv("C:\\learning\\research\\segmantation\\"+title + "seg.csv", index=False, sep=',')

        ID=[]
        name=[]
        IDtemp=IDmark+Idmarkbeh
        nodename=varname+varnamebeh
        for i in IDtemp:
            if not i in ID:
                i.rstrip()
                i = "".join((re.sub("\n", " ", i)))
                ID.append(i)
        for i in nodename:
            if not i in name:

                i.rstrip()
                i = "".join((re.sub("\n", " ", i)))
                name.append(i)



        for i in range(0,len(ID)):

            conceptlabel.append('concepts')
        dataframe = pd.DataFrame({'id:ID': ID, 'concept': name, 'value':valueorigin,':'
                                                                                    'LABEL':conceptlabel})
        dataframe.to_csv("C:\learning\\research\\nodes\\"+titlesub+".csv", index=False, sep=',')


        concept = []
        value = []
        for k, v in tfidfdic.items():
            concept.append(k)
            value.append(v)

        dataframe = pd.DataFrame({'concepts': concept,'value':value})
        dataframe.to_csv("C:\\learning\\research\\importanceevulation\\"+title + "eva.csv", index=False, sep=',')
        print(title+' is ok!')
        outall = outall+echout
    print(wry(outall, wrypath)+' is ok!')


if __name__ == '__main__':
    main()
