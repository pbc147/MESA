import fnmatch
import os
import numpy
import math
M=[0.1,1,5,10,15,30]
Z=[0.01,0.015,0.02]
owd=os.getcwd()

list=open(owd+'/list.txt','a+')
list.write('Mass,\tZ,\tLog_10(dt),\tProfiles\n\n')
for i in range(len(M)):
    for j in range(len(Z)):
        if not(os.path.isdir(owd+"/M_"+str(M[i])+"/Z_"+str(Z[j]).replace('.','_'))):
            list.write(str(M[i])+',\t'+str(Z[j])+',\t'+str(math.floor((3508*M[i]**(-0.0002902)-3501))))
            os.makedirs(owd+"/M_"+str(M[i])+"/Z_"+str(Z[j]).replace('.','_'))
            os.system("cp -r "+owd+"/template/. "+owd+"/M_"+str(M[i])+"/Z_"+str(Z[j]).replace('.','_')+"/")
            os.chdir(owd+"/M_"+str(M[i])+"/Z_"+str(Z[j]).replace('.','_'))
            with open('./inlist_project', 'r') as file:
                filedata = file.read()
            filedata = filedata.replace('%#Mass%#', str(M[i]))
            filedata = filedata.replace('%#Met%#', str(Z[j]))
            filedata = filedata.replace('%#Tim%#', str(10**math.floor((3508*M[i]**(-0.0002902)-3501)))) 
# This formula gives an appropriate maximum timestep for masses in the required range such that the
# central hydrogen mass fraction does not change too much between each timestep.
            with open('./inlist_project', 'w') as file:
                file.write(filedata)
            os.system("./run.sh")
            list.write(',\t\t'+str(len(fnmatch.filter(os.listdir('./LOGS/'), 'X_*.data')))+'\n')
        else:
            os.chdir(owd+"/M_"+str(M[i])+"/Z_"+str(Z[j]).replace('.','_'))
            os.system("./re")
            os.system('python3 ./run.py')
        os.chdir(owd)    





