import pickle
# using jenkinsapi
from jenkinsapi.jenkins import Jenkins

J = Jenkins('http://localhost:8080', username='paras', password='roundglass')

# to get current BUILD_NUMBER
build_no=str(J['test_m'].get_last_build())[-2:]
print "current BUILD_NUMBER :",build_no

# to read pickle file of current build
filename = "home/user/.jenkins/workspace/test_m/%s.pkl" %build_no
with open(filename ,"rb") as f1:
    new_data1=pickle.load(f1)
print "\ncurrent BUILD data :",new_data1

# to get previous BUILD_NUMBER
last_build_no=str(J['test_m'].get_last_good_build())[-2:]
print "Previous BUILD_NUMBER :",last_build_no

# to read pickle file of previous build
filename = "home/user/.jenkins/workspace/test_m/%s.pkl" %last_build_no
with open(filename ,"rb") as f2:
    new_data2=pickle.load(f2)
print "\nprevious BUILD data :",new_data2
