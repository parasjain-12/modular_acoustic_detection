import pandas as pd
import pickle
# using jenkinsapi
from jenkinsapi.jenkins import Jenkins


J = Jenkins('http://localhost:8080', username='paras', password='roundglass')
build_no=str(J['master'].get_last_build())[-2:]
print "current BUILD_NUMBER :",build_no

# create a pickle file, buid_number as name
filename = "/home/paras/.jenkins/workspace/test_m/%s.pkl" %build_no
with open(filename ,"wb") as f:
    pickle.dump(df,f)
