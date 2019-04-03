import pandas as pd
import pickle
# using jenkinsapi
from jenkinsapi.jenkins import Jenkins
p_data=[{1:'dell',2:'lenovo',3:'hp',4:'vaio'}]
df = pd.DataFrame(p_data)


J = Jenkins('http://localhost:8080', username='paras', password='roundglass')

# create a pickle file, buid_number as name
filename = "/home/paras/.jenkins/workspace/test_m/report.pkl"
with open(filename ,"wb") as f:
    pickle.dump(df,f)
