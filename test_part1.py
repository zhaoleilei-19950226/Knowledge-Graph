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

for k,v in conceptdic.items():
    conditions=conditions_getnew.conditions_get(v)


    HR_dic=conditions_test.conditions_test(conditions,k)



