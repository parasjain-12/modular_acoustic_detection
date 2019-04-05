import pickle
# using jenkinsapi
import pandas as pd
from jenkinsapi.jenkins import Jenkins

J = Jenkins('http://localhost:8080', username='paras', password='roundglass')

# to get current BUILD_NUMBER/home/paras/.jenkins/workspace/test_m/
build_no=str(J['test_m'].get_last_build())[-2:]
print "current BUILD_NUMBER :",build_no

filename12 = '/home/paras/.jenkins/workspace/test_m/%s.txt' %build_no
f = open(filename12,'w')
name_file = '%s.txt' %build_no

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
f.write("\n============ Motor_Sounds ==============\n")

motor_sound=(final_df2.iloc[0][2:] - final_df1.iloc[0][2:]) *100
#print motor_sound
for key, value in motor_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x = key,"increased by", format(value).replace("-",""),"%"
        print >>f, x 
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        x=key," decreased by", format(value).replace("-",""),"%"
        print >>f,x
        
print "\n========== Explosion_Sounds ============"
f.write("\n========== Explosion_Sounds ============\n")

explosion_sound=(final_df2.iloc[1][2:] - final_df1.iloc[1][2:]) *100
#print explosion_sound
for key, value in explosion_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x = key,"increased by", format(value).replace("-",""),"%"
        print >>f,x
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        x= key," decreased by", format(value).replace("-",""),"%"
        print >>f,x

print "\n============ Human_Sound =============="
f.write("\n============ Human_Sound ==============\n")
human_sound=(final_df2.iloc[2][2:] - final_df1.iloc[2][2:]) *100
#print human_sound
for key, value in human_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x = key,"increased by", format(value).replace("-",""),"%"
        print >>f,x
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        x =key," decreased by", format(value).replace("-",""),"%"
        print >>f,x

print "\n=========== Nature_Sound ============="
f.write("\n=========== Nature_Sound =============\n")
nature_sound=(final_df2.iloc[3][2:] - final_df1.iloc[3][2:]) *100
#print nature_sound
for key, value in nature_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x=key,"increased by", format(value).replace("-",""),"%"
        print >>f,x
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        x = key," decreased by", format(value).replace("-",""),"%"
        print >>f,x

print "\n========== Domestic_Animals ============"
f.write("\n========== Domestic_Animals ============\n")

domestic_animals=(final_df2.iloc[4][2:] - final_df1.iloc[4][2:]) *100
#print domestic_animals
for key, value in domestic_animals.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x = key,"increased by", format(value).replace("-",""),"%"
        print >>f,x
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        x = key," decreased by", format(value).replace("-",""),"%"
        print >>f,x

print "\n=============== Tools ================="
f.write("\n=============== Tools =================\n")
tools=(final_df2.iloc[5][2:] - final_df1.iloc[5][2:]) *100
#print tools
for key, value in tools.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x = key,"increased by", format(value).replace("-",""),"%"
        print >>f,x
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        x = key," decreased by", format(value).replace("-",""),"%"
        print >>f,x

print "\n============= Macro_Avg ==============="
f.write("\nn============= Macro_Avg ===============\n")
macro_avg=(final_df2.iloc[6][2:] - final_df1.iloc[6][2:]) *100
#print macro_avg
for key, value in macro_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x=key,"increased by", format(value).replace("-",""),"%"
        print >>f,x
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        x=key," decreased by", format(value).replace("-",""),"%"
        print >>f,x

print "\n============== Micro_Avg ==============="
f.write("\nn============== Micro_Avg ===============\n")
micro_avg=(final_df2.loc[7][2:] - final_df1.loc[7][2:]) *100
#print micro_avg
for key, value in micro_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x=key,"increased by", format(value).replace("-",""),"%"
        print >>f,x
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        x = key," decreased by", format(value).replace("-",""),"%"
        print >>f,x

print "\n============ Weighted_Avg =============="
f.write("\n============ Weighted_Avg ==============\n")
weighted_avg=(final_df2.loc[8][2:] - final_df1.loc[8][2:]) *100
#print weighted_avg
for key, value in weighted_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
        x = key,"increased by", format(value).replace("-",""),"%"
        print >>f,x
    else:
        print key," decreased by", format(value).replace("-",""),"%" 
        x= key," decreased by", format(value).replace("-",""),"%" 
        print >>f,x
import config
from slackclient import SlackClient
token  = "xoxp-601323582535-600179716996-601332785047-41a3802ba14f65579bdb90437cd89869"
sc = SlackClient(token)
def upload_file(filename, content, channel):
        
    '''
    upload a long text as a file
    '''
    ret = sc.api_call("files.upload", filename=filename, channels=channel, file= (str.encode(content)))

ch = '#jenkins'
con = 'Compared result '
fil = 'filename12'
upload_file(fil,con,ch)
#files.upload(token,file1)
