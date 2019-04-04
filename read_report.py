import pickle
# using jenkinsapi
import pandas as pd
from jenkinsapi.jenkins import Jenkins

J = Jenkins('http://localhost:8080', username='paras', password='roundglass')

# to get current BUILD_NUMBER/home/paras/.jenkins/workspace/test_m/
build_no=str(J['test_m'].get_last_build())[-2:]
print "current BUILD_NUMBER :",build_no

# to read pickle file of current build

filename1 = "/home/paras/.jenkins/workspace/test_m/%s.csv" %build_no
#filename1 = "/home/paras/.jenkins/workspace/test_m/29.csv"

final_df1 = pd.read_csv(filename1)


# to get previous BUILD_NUMBER
last_build_no=str(J['test_m'].get_last_good_build())[-2:]
print "Previous BUILD_NUMBER :",last_build_no

# to read pickle file of previous build
filename2 = "/home/paras/.jenkins/workspace/test_m/%s.csv" %last_build_no

#filename2 = "/home/paras/.jenkins/workspace/test_m/29.csv"

final_df2=pd.read_csv(filename2)



final_df1.drop(['support'], axis=1,inplace = True)
final_df2.drop(['support'], axis=1,inplace = True)
final_df1.drop(['Unnamed: 0'], axis=1,inplace = True)
final_df2.drop(['Unnamed: 0'], axis=1,inplace = True)
print "\nPrevious Results :\n",final_df1
#print final_df1,"\n"
print "\nCurrent Results :\n",final_df2
#print final_df2,"\n"

# columns=['Motor_Sound','Explosion_Sound','Human_Sound','Nature_Sound', \
#               'Domestic_Animals','Tools','macro_avg','micro_avg','weighted_avg']
print final_df2.iloc[0][2:]
print "\n============ Motor_Sounds =============="
motor_sound=(final_df2.iloc[0][2:] - final_df1.iloc[0][2:]) *100
#print motor_sound
for key, value in motor_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        
print "\n========== Explosion_Sounds ============"
explosion_sound=(final_df2.iloc[1][2:] - final_df1.iloc[1][2:]) *100
#print explosion_sound
for key, value in explosion_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============ Human_Sound =============="
human_sound=(final_df2.iloc[2][2:] - final_df1.iloc[2][2:]) *100
#print human_sound
for key, value in human_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n=========== Nature_Sound ============="
nature_sound=(final_df2.iloc[3][2:] - final_df1.iloc[3][2:]) *100
#print nature_sound
for key, value in nature_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n========== Domestic_Animals ============"
domestic_animals=(final_df2.iloc[4][2:] - final_df1.iloc[4][2:]) *100
#print domestic_animals
for key, value in domestic_animals.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n=============== Tools ================="
tools=(final_df2.iloc[5][2:] - final_df1.iloc[5][2:]) *100
#print tools
for key, value in tools.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============= Macro_Avg ==============="
macro_avg=(final_df2.iloc[6][2:] - final_df1.iloc[6][2:]) *100
#print macro_avg
for key, value in macro_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============== Micro_Avg ==============="
micro_avg=(final_df2.loc[7][2:] - final_df1.loc[7][2:]) *100
#print micro_avg
for key, value in micro_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============ Weighted_Avg =============="
weighted_avg=(final_df2.loc[8][2:] - final_df1.loc[8][2:]) *100
#print weighted_avg
for key, value in weighted_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"     
