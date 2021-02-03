from itertools import permutations
from itertools import combinations
from itertools import product

def conditions_get(factors_list):
    list_final=[]
    factors_listuse=[]


    for i in factors_list:
        if(i not in factors_listuse):
            factors_listuse.append(i)
    for i in range(1,len(factors_listuse)+1,1):
        for j in list(permutations(factors_listuse, i)):
            if(j not in list_final):
                list_final.append(j)
    """
    for i in range(1, len(factors_list), 1):
        for j in list(product(factors_list, i)):
            count=0
            print(j)
            for k in j:
                for t in j:
                    if(k==t):
                        count=count+1
                        print(count)
            if (j not in list_final and count==1):
                list_final.append(j)
    """
    return list_final
