import pickle
# using jenkinsapi
import pandas as pd
from jenkinsapi.jenkins import Jenkins

J = Jenkins('http://localhost:8080', username='paras', password='roundglass')

# to get current BUILD_NUMBER/home/paras/.jenkins/workspace/test_m/
build_no=str(J['test_m'].get_last_build())[-2:]
print "current BUILD_NUMBER :",build_no

# to read pickle file of current build
filename = "/home/paras/.jenkins/workspace/test_m/%s.pkl" %build_no
with open(filename ,"rb") as f1:
    data1=pickle.load(f1)
print "\ncurrent BUILD data :",data1

# to get previous BUILD_NUMBER
last_build_no=str(J['test_m'].get_last_good_build())[-2:]
print "Previous BUILD_NUMBER :",last_build_no

# to read pickle file of previous build
filename = "/home/paras/.jenkins/workspace/test_m/%s.pkl" %last_build_no
with open(filename ,"rb") as f2:
    data2=pickle.load(f2)
print "\nprevious BUILD data :",data2

df1=pd.DataFrame(data1)
#print "\nPrevious Results :"
#print df1,"\n"

df2=pd.DataFrame(data2)

final_df1=df1.drop(['support'])
final_df2=df2.drop(['support'])
print "\nPrevious Results :\n",final_df1
#print final_df1,"\n"
print "\nCurrent Results :\n",final_df2
#print final_df2,"\n"

# columns=['Motor_Sound','Explosion_Sound','Human_Sound','Nature_Sound', \
#               'Domestic_Animals','Tools','macro_avg','micro_avg','weighted_avg']

print "\n============ Motor_Sounds =============="
motor_sound=(final_df2.loc[:,'0'] - final_df1.loc[:,'0']) *100
#print motor_sound
for key, value in motor_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        
print "\n========== Explosion_Sounds ============"
explosion_sound=(final_df2.loc[:,'1'] - final_df1.loc[:,'1']) *100
#print explosion_sound
for key, value in explosion_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============ Human_Sound =============="
human_sound=(final_df2.loc[:,'2'] - final_df1.loc[:,'2']) *100
#print human_sound
for key, value in human_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n=========== Nature_Sound ============="
nature_sound=(final_df2.loc[:,'3'] - final_df1.loc[:,'3']) *100
#print nature_sound
for key, value in nature_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n========== Domestic_Animals ============"
domestic_animals=(final_df2.loc[:,'4'] - final_df1.loc[:,'4']) *100
#print domestic_animals
for key, value in domestic_animals.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n=============== Tools ================="
tools=(final_df2.loc[:,'5'] - final_df1.loc[:,'5']) *100
#print tools
for key, value in tools.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============= Macro_Avg ==============="
macro_avg=(final_df2.loc[:,'macro avg'] - final_df1.loc[:,'macro avg']) *100
#print macro_avg
for key, value in macro_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============== Micro_Avg ==============="
micro_avg=(final_df2.loc[:,'micro avg'] - final_df1.loc[:,'micro avg']) *100
#print micro_avg
for key, value in micro_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============ Weighted_Avg =============="
weighted_avg=(final_df2.loc[:,'weighted avg'] - final_df1.loc[:,'weighted avg']) *100
#print weighted_avg
for key, value in weighted_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"     

